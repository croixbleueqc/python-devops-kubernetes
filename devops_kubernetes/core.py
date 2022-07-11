# Copyright 2020 Croix Bleue du Québec

# This file is part of python-devops-kubernetes.

# python-devops-kubernetes is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# python-devops-kubernetes is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with python-devops-kubernetes.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import logging
from contextlib import asynccontextmanager

from kubernetes_asyncio import client
from kubernetes_asyncio import config as k8sconfig
from kubernetes_asyncio import watch
from kubernetes_asyncio.client.api.core_v1_api import CoreV1Api


class Core(object):
    @classmethod
    async def create(cls, config):
        self = Core(config)
        await self.init()
        return self

    def __init__(self, config):
        self.config = config

    async def init(self):
        pass

    @asynccontextmanager
    async def context(self, cluster):
        ctx = await Core.Context.create(self.config["clusters"][cluster])
        try:
            yield ctx
        finally:
            await ctx.close()

    class Context(object):
        """
        Context permits to communicate with a specific kubernetes cluster.
        This is a dedicated context for the caller
        """

        @classmethod
        async def create(cls, config):
            self = Core.Context()
            await self.init(config)
            return self

        async def init(self, config):
            self.api = await k8sconfig.new_client_from_config(
                config_file=config["config_file"]
            )

        async def list_pods(self, namespace):
            v1 = CoreV1Api(self.api)
            ret = await v1.list_namespaced_pod(namespace)
            return ret.items

        async def close(self):
            await self.api.close()

        async def pods(self, namespace, raw=True):
            v1 = CoreV1Api(self.api)
            w = watch.Watch()

            try:
                async for event in w.stream(v1.list_namespaced_pod, namespace):
                    logging.debug("yield a pod")
                    yield {
                        "type": event["type"],
                        "key": event["object"].metadata.uid,
                        "value": event["raw_object"] if raw else event["object"],
                    }
            except asyncio.CancelledError:
                logging.debug("cancelled error")
                raise

        async def delete_pod(self, name, namespace):
            v1 = client.CoreV1Api(self.api)
            await v1.delete_namespaced_pod(name, namespace)

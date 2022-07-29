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
from concurrent.futures import thread
import logging
from contextlib import asynccontextmanager

from kubernetes import client, watch
from kubernetes import config as k8sconfig


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
            self.init(config)
            return self

        def init(self, config):
            k8sconfig.load_kube_config(config_file=config["config_file"])
            self.api = client.CoreV1Api()

        async def list_pods(self, namespace):
            thread = self.api.list_namespaced_pod(namespace, async_req=True)
            ret = thread.get()
            return ret.items

        async def list_all_pods(self):
            thread = self.api.list_pod_for_all_namespaces(async_req=True)
            ret = thread.get()
            return ret.items

        async def close(self):
            pass

        async def pods(self, namespace, raw=True):
            w = watch.Watch()

            try:
                for event in w.stream(self.api.list_namespaced_pod, namespace):
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
            thread = self.api.delete_namespaced_pod(name, namespace, async_req=True)
            return thread.get()

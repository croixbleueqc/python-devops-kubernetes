DevOps Kubernetes (Asyncio)
===========================

Python library to abstract kubernetes with asyncio.

The main purpose is to build a backend or a frontend on top of Kubernetes.

The abstraction layer is really small at this time (alpha version)

Installation
------------

This package is available for Python 3.7+.

.. code:: bash

    pip3 install --user .

Configuration
-------------

Configuration can be done via a dict object. The configuration is passed to the library to initialize all components.

.. code:: bash

    {
        "clusters": {
            "cluster1": {
                "config_file": "/path/to/kubeconfig/for/cluster1"
            }
        }
    }

Usage
-----

This library is based on asyncio so await/async constraints applied. To make code examples more readeable, we will omit some codes that are relevant to asyncio itself to execute a coroutine.

Initialize DevOps kubernetes lib
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    import asyncio
    import json

    from devops_kubernetes.core import Core

    async def main():
        with open("config.json", "r") as f:
            config = json.loads(f.read())

        core = await Core.create(config)
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

Usage
^^^^^

.. code:: python

    # watch all pods from a namespace
    async with self.core.context("cluster1") as ctx:
        async for event in ctx.pods("default"):
            yield event

    # delete a pod on a specific namespace
    async with self.core.context("cluster1") as ctx:
            await ctx.delete_pod("pod_name", "default")

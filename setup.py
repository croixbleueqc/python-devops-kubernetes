#!/usr/bin/env python3

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

from setuptools import setup, find_packages

setup(
    name="devops_kubernetes",
    version="0.0.1",
    python_requires=">=3.7",
    packages=find_packages(exclude=["tests"]),
    install_requires=["kubernetes_asyncio"],
    # Metadata
    author="Croix Bleue du Quebec",
    author_email="devops@qc.croixbleue.ca",
    license="LGPL-3.0-or-later",
    description="kubernetes abstraction for DevOps",
    long_description=open("README.rst").read(),
    url="https://github.com/croixbleueqc/python-devops-kubernetes",
    keywords=["asyncio", "kubernetes"],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    test_suite="tests",
)

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
    install_requires=["kubernetes"],
    python_requires=">=3.10",
    packages=find_packages(exclude=["tests"]),
    # Metadata
    author="Croix Bleue du Quebec",
    author_email="devops@qc.croixbleue.ca",
    license="LGPL-3.0-or-later",
    description="kubernetes abstraction for DevOps",
    long_description=open("README.rst").read(),
    url="https://github.com/croixbleueqc/python-devops-kubernetes",
    keywords=["asyncio", "kubernetes"],
)

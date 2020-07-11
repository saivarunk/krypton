#  Copyright 2020 Varun Kruthiventi
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# setup.py file for krypton

from setuptools import setup, find_packages

from krypton.core.constants import KRYPTON_VERSION


# read the contents of your README file for long_description
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='krypton-ml',
    version=KRYPTON_VERSION,
    author="Varun Kruthiventi",
    author_email="varunk@ieee.org",
    description="Model Server for ML and DL Models built using FastAPI",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="Model Serving, Model Server, Machine Learning, Deep Learning, FastAPI",
    url="https://github.com/saivarunk/krypton",
    project_urls={
        "Bug Tracker": "https://github.com/saivarunk/krypton/issues",
        "Documentation": "https://github.com/saivarunk/krypton",
        "Source Code": "https://github.com/saivarunk/krypton",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "aiofiles==0.5.0",
        "click==7.1.2",
        "pyfiglet==0.8.post1",
        "colored==1.4.2",
        "fastapi==0.58.0",
        "uvicorn==0.11.5",
        "pydantic==1.5.1"
    ],
    python_requires='>=3.7.*',
    entry_points='''
        [console_scripts]
        krypton=krypton.cli.main:cli
    ''',
)

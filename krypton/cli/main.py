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

import click
import colored
import pyfiglet
import uvicorn

from colored import stylize

from krypton.core.settings import settings


@click.group()
def cli():
    '''
    This is the root cli object
    '''
    pass


@click.command()
def server():
    '''
    Start the krypton web server
    '''
    # Todo - Migrate Krypton Bootup figlet to fastapi hooks
    print(stylize(pyfiglet.figlet_format("krypton", font="slant"), colored.fg("cyan")))
    print(stylize("Model Server for ML and DL Models built with FastAPI", colored.fg("cyan")))
    # Start FastAPI Server
    uvicorn.run(
        "krypton.backend:app",
        host=settings.APP_HOSTNAME,
        port=settings.APP_PORT,
        reload=settings.DEBUG,
        debug=settings.DEBUG,
        log_level=settings.LOG_LEVEL
    )


# Add Child scripts to main cli group
cli.add_command(server)

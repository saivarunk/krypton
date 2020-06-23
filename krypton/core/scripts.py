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

import os

from typing import Callable

from krypton.core.settings import settings


def setup_app_dir(path):
    # if the path is the default one, get root profile path of user
    # and create directory for krypton
    if path == '~/krypton':
        path = os.path.join(os.path.expanduser('~'), 'krypton')

    # create a folder for model yaml specs to be added by the users
    models_path = os.path.join(path, 'models')

    if not os.path.isdir(path):
        os.mkdir(path)
        print(f"Created Krypton Root Directory at :{path}")

    if not os.path.isdir(models_path):
        os.mkdir(models_path)
        print(f"Created Krypton Model Directory at :{models_path}")


def setup_krypton() -> Callable:
    """
    This function takes care of all the tasks that needs to be taken care before the Krypton application boots up.

    :return: Callable
    """
    def _setup() -> None:
        # create krypton directory in the path specified in APP_ROOT
        setup_app_dir(settings.APP_ROOT)

    return _setup

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

import gc
import os
import importlib.util

from typing import Callable

from krypton.core.settings import settings
from krypton.backend.models.interfaces.krypton_model import KryptonModel
from krypton.backend.models.store.repository import model_repository


def load_models_memory(model_files):
    for file in model_files:
        model_file_name = file.get('model_file')
        model_path = file.get('abs_path')
        spec = importlib.util.spec_from_file_location("model", model_path)
        app_callable = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(app_callable)

        # Check for model attribute on app_callable
        if not hasattr(app_callable, 'model'):
            raise Exception(f"Model file {model_file_name} doesnt have a callable model")

        # Check if app_callable.model is a implementation of KryptonModel
        # If yes, call the model_repository to load model
        if issubclass(type(app_callable.model), KryptonModel):
            model_repository.add_model(app_callable.model)
        else:
            raise Exception(f"Model callable in model file: {model_file_name} is not a implementation of KryptonModel")

        del app_callable, spec
        gc.collect()


def scan_model_files(path, model_folder):
    # check for valid python files in path variable
    _valid_file_extension = '.py'

    if path == '~/krypton':
        path = os.path.join(os.path.expanduser('~'), 'krypton')

    models_path = os.path.join(path, model_folder)
    return [{'model_file': f, 'abs_path': os.path.join(path, models_path, f)} for f in os.listdir(models_path) if
            f.endswith(_valid_file_extension)]


def setup_app_dir(path, model_folder):
    # if the path is the default one, get root profile path of user
    # and create directory for krypton
    if path == '~/krypton':
        path = os.path.join(os.path.expanduser('~'), 'krypton')

    # create a folder for model yaml specs to be added by the users
    models_path = os.path.join(path, model_folder)

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
        setup_app_dir(settings.APP_ROOT, settings.APP_MODEL_FOLDER)

    return _setup


def load_models() -> Callable:
    """
    This function scans the APP_ROOT directory for valid Krypton callables
    and loads all of them into the application memory
    :return: Callable
    """

    def _setup_models() -> None:
        # scan for valid python files in APP_ROOT directory
        # check for 'model' callable in each file
        # check if the model already exists in memory usisng the model name (use get_model_name)
        # if it doesn't exist, import it into memory and call load_model method in each model
        model_files = scan_model_files(settings.APP_ROOT, settings.APP_MODEL_FOLDER)
        load_models_memory(model_files)

    return _setup_models

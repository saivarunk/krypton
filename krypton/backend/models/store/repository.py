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

import copy

from typing import List

from ..interfaces.krypton_model import KryptonModel


class ModelRepository:
    """
    This class is used to create a Krypton ModelRepository. It will hold few cutom methods written
    on top of python dict
    """

    # This iss the main dict which holds the krypton model objects in memory
    __models = dict()

    def __init__(self):
        pass

    def add_model(self, model: KryptonModel):
        name = model.model_name
        if not name:
            raise Exception(f"Model file {model.__class__} doesn't have a proper name !")

        # clean the name to make it url friendly
        name = name.lower().replace(' ', '-').replace('.', '')
        if name in self.__models:
            raise Exception(f"Model with name: {name} already exists in Krypton Repository")

        # Do a deepcopy so that object from importlib can be cleanup after this method is called
        self.__models[name] = copy.deepcopy(model)
        # Call load_model method from the model callable to import ML/DL model into memory
        self.__models[name].load_model()

    def get_model(self, name: str) -> KryptonModel:
        """
        This method returns krypton model from the repository
        :param name: model_name
        :return: object of type KryptonModel
        """
        if name not in self.__models:
            return None
        return self.__models[name]

    def get_models(self) -> List[dict]:
        return [{'model': model, 'endpoint': f'/api/v1/models/{model}/predict', 'status': 'Available'}
                for model in self.__models]

    def delete_model(self, name: str):
        del self.__models[name]


# This object will be used by the loader scripts and fastapi controller
model_repository = ModelRepository()

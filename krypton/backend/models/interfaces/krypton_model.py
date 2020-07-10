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

from abc import ABCMeta, abstractmethod, abstractproperty

from fastapi import Request

class KryptonModel(metaclass=ABCMeta):
    """
    This is a interface class that can be used by developers to enable
    Krypton model server to serve the models.
    """

    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def model(self):
        """
        Abstract property to enforce the implementation attribute 'model'
        """
        pass

    @property
    @abstractmethod
    def model_name(self):
        """
        Abstract property to enforce the implementation attribute 'model_name'
        """
        pass

    @abstractmethod
    def load_model(cls):
        """
        This method is used to load the model into the __model attribute of the class.
        Any subclass inheriting this class is expected to implement this method.
        """
        pass

    @abstractmethod
    def predict(cls, request: Request):
        """
        This method is called by the Krypton model server to serve the predictions during
        the API calls. Any subclass inheriting this class is expected to implement this method.
        """
        pass

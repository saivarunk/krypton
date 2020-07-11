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

import spacy

from krypton import KryptonModel
from fastapi.responses import JSONResponse


class SpacyDemo(KryptonModel):
    model_name = 'spacy_ner_demo'
    model = None

    def load_model(self):
        self.model = spacy.load("en_core_web_sm")

    async def predict(self, request):
        request_json = await request.json()
        data = request_json.get('data')
        doc = self.model(data)
        response = {
            'noun_phrases': [chunk.text for chunk in doc.noun_chunks],
            'verbs': [token.lemma_ for token in doc if token.pos_ == "VERB"],
            'entities': [{'ents': entity.text, 'label': entity.label_} for entity in doc.ents]
        }
        return JSONResponse(status_code=200, content=response)


model = SpacyDemo()

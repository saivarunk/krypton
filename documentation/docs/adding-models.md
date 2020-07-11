# Adding Models

Once the models directory is created by the cli, you can start adding models to krypton by creating model 
files in the directory by using the Krypton's ```KryptonModel``` class.

You can use this example, which has a Spacy based implementation of Krypton Model script.

```python
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
```

- Krypton server expects every model script to have a class implemented based on KryptonModel base class.
- It expects the class to implement ```load_model``` and ```predict``` methods - mandatory.
- It expects the class to have the attributes ```model_name``` and ```model``` - mandatory.
- ```predict``` method is expected to be an async function to support FastAPI's request object.
- ```load_model``` method is called during the startup of Krypton model server. The server will try to call this 
method to load the model into memory and make it available for API requests.
- ```model_name``` attribute is used by the server 
- ```predict``` method is called during the the execution of API requests for the specific model. A single parameter, 
`request` which is of type `Request`  from `fastapi` module is injected into the method during API calls. 
This request object contains the request parameters like body, parsed form-data (can be used for file uploads), 
json body and even headers of the request. Please refer Starlette's [documentation](https://www.starlette.io/requests/) for details about Request class.

# Adding Models

Once the models directory is created by the cli, you can start adding models to krypton by creating model 
files in the directory by using the Krypton's ```KryptonModel``` class.

You can use this example, which has a Spacy based implementation of Krypton Model script.

### Spacy Example 

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
The sample used in this model example is taken from [Spacy.io](https://spacy.io/)

### Implementation

#### Model Class

Krypton server expects every model script to have a class implemented based on KryptonModel base class.
It can be imported from krypton root package ```from krypton import KryptonModel```

- The class should implement ```load_model``` and ```predict``` methods - this is mandatory.
- The class should have the attributes ```model_name``` and ```model``` - this is mandatory.
- ```predict``` method is expected to be an async function to support FastAPI's request object  - this is mandatory.
- ```load_model``` method is called during the startup of Krypton model server. The server will try to call this 
method to load the model into memory and make it available for API requests.

- ```model_name``` attribute is used by the server 
- ```predict``` method is called during the the execution of API requests for the specific model. A single parameter, 
`request` which is of type `Request`  from `fastapi` module is injected into the method during API calls. 
This request object contains the request parameters like body, parsed form-data (can be used for file uploads), 
json body and even headers of the request. Please refer Starlette's [documentation](https://www.starlette.io/requests/) 
for details about Request class.
- The developer can carryout the necessary computations for making the predictions using ```model``` attribute and 
then return a valid response. This response has to be a valid response object that can be handled by FastAPI.

#### model callable

Krypton server expects every model script to have a object with name ```model``` which needs to be instantiated with 
any class, that implements ```KryptonModel```.

Without the ```model``` callable, the Krypton server would throw expcetion while booting.


### Model dependencies

The developer needs to make sure that the model specific dependencies are added to the Python environment where 
krypton module was installed.

It is always recommended to use a new virtualenv for using Krypton.

### Apply Changes

Once you have added a model script, you can restart the server by using the ```krypton server``` command again. 
After restarting the krypton server, all the model scripts present in the ```~/krypton/models``` will be loaded into 
server.
  
Check the next page on how to get list of models available and access the model endpoints.
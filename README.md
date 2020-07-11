# krypton

Model Server for ML and DL Models built using FastAPI

Visit [https://kryptonml.com](https://kryptonml.com) for latest documentation.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![GitHub](https://img.shields.io/github/license/saivarunk/krypton?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/saivarunk/krypton?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/saivarunk/krypton?style=flat-square)
[![Agile Board](https://img.shields.io/badge/YouTrack-Agile%20Board-brightgreen?style=flat-square)](https://krypton.myjetbrains.com/youtrack/agiles/115-0/116-2)

<img src="assets/krypton_small.png" width="700">

### Note
- This project is in development stage. You can expect rapid changes in the internals of the project.
- Would love to hear valuable feedback, and it will be duly acknowledged.
- Any one who has experienced an issue / want to report a bug can create a issue here in [Github](https://github.com/saivarunk/krypton/issues)

### Setup

The krypton module can be installed from the PyPI repository using
```bash
pip install krypton-ml
```

Once the package is installed, you can start the Krypton Model server using Krypton CLI
```bash
krypton server
```

- For the first time, the krypton model server would try to create directory at ```~/krypton/models``` by default.
- This will vary depending upon the kind of os you are using.

The location can look like these for each operating system:

- Mac:  ```/Users/<user_name>/krypton/models```
- Linux: ```/home/<user_name>/krypton/models```
- Windows: ```C:\Users\<user_name>\krypton\models```

This path can be modified to a custom location by setting ```KRYPTON_APP_ROOT``` value to any valid 
location where you want krypton server to setup the ```models``` directory.

The server would be started at ```PORT``` 7000 by default, and it can be accessed at ```http://localhost:7000```

![Krypton CLI](assets/krypton_cli.png)

### Adding models to krypton-server

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

### Work in progress
- Authentication for API's (Basic Auth, API Key based auth)
- Metrics using statsd exporter
- Configurable logging options

### Make Prediction on a model

Once the krypton server is up and running, you can access the list of models by making a GET request on this endpoint.

#### Request
```bash
curl --location --request POST 'http://<hostname>:<port>/api/v1/models/<model_name>/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "data": "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."
}'
```

#### Sample Response
```json
{
    "noun_phrases": [
        "Sebastian Thrun",
        "self-driving cars",
        "Google",
        "few people",
        "the company",
        "him"
    ],
    "verbs": [
        "start",
        "work",
        "drive",
        "take"
    ],
    "entities": [
        {
            "ents": "Sebastian Thrun",
            "label": "PERSON"
        },
        {
            "ents": "Google",
            "label": "ORG"
        },
        {
            "ents": "2007",
            "label": "DATE"
        }
    ]
}
```

The sample used in this model example is taken from [Spacy.io](https://spacy.io/)
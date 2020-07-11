# Examples

### Docker

Krypton can be run inside a Docker container. Below is one example which uses our ```spacy_ner_example``` model.

```Dockerfile```
```Docker
FROM python:3.8.3-alpine3.12

WORKDIR /app

# Install system dependencies for uvloop
RUN apk update \
    && apk add --virtual build-dependencies \
        build-base \
        gcc

# Copy your model script to any dirrectory
COPY spacy.py /app/krypton/models/

# Install krypton
RUN pip install krypton-ml

# install spacy and language model
RUN pip install spacy
RUN python -m spacy download en_core_web_sm

EXPOSE 7000

CMD ["krypton", "server"]
```

Make sure that you have a copy of [```spacy.py```](https://github.com/saivarunk/krypton/blob/develop/samples/spacy.py)
file in the current directory.

Build the Docker image

```bash
docker build -t krypton-spacy .
```

Run the Docker Image
```bash
docker run -p 7000:7000 -e KRYPTON_APP_ROOT=/app/krypton -t krypton-spacy
```
!!! Info
    You can observe that we are passing a variable ```KRYPTON_APP_ROOT``` with value /app/krypton. Since in the 
    Dockerfile we have copied the model to a custom directory, we are changing Krypton's default app root folder.
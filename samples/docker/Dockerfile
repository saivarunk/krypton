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
# RUN pip install spacy
# RUN python -m spacy download en_core_web_sm

EXPOSE 7000

CMD ["krypton", "server"]

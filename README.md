<!-- omit in toc -->
# ITCS Workshop by Union Investment

This Repository hosts the files neccessary for the ITCS Workshop by Union Investment.

In the first part of the workshop we want to develop an API, based on the phenomenal python library fastapi.
We then let the API run in a Container. The Container will be pushed into a private Container Registry.
From the Registry the Container Image will be pushed into an Azure App Service.
As a Deployment Handler we use GitHub Actions.

<!-- omit in toc -->
## Table of Contents

- [FastApi](#fastapi)
- [Container](#container)

## FastApi

[Official Documentation](https://fastapi.tiangolo.com/tutorial/request-files/)

```python
# starting pipenv
pipenv shell

# running fastapi (main.py) on uvicorn
uvicorn main:app --reload

# if python-multipart is somehow missing
pip3 uninstall python-multipart
pip3 install python-multipart

uvicorn main:app --reload
```

You will know be able of accessing your API on 127.0.0.1:8000.

## Container

*some docker commands..*

```bash
# building the image
docker build -f ./Dockerfile -t fastapi:1.0

# running the container
docker run -p 8000:8000 -t fastapi-cd:1.0

# list all available docker images on your computer
docker images

# list all running containers
docker container ls

# stopping a container
docker stop **containername / containerid

# removing a container image
docker rm **containername / containerid

```

---
***Copyright © 2021 Union IT-Services GmbH. All rights reserved.***

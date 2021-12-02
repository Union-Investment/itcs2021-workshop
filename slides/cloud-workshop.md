---
marp: true
---
<!-- backgroundColor: white -->
<!--
theme: gaia
paginate: false
-->

## Software Development in Cloud Environments
#### Workshop ITCS - Union Investment
Frankfurt, 03.12.2021 - Sven Schürmann & Carina Esau

#

1. [Welcome](#welcome)
2. [Modern Software Development](#modern)
3. [Containerization](#container)
4. [CI/CD](#cicd)
5. [Wrap Up](#wrapup)

---


# Welcome

- Wer sind wir
- Wie funktioniert die Entwicklungsumgebung
- Was machen wir heute

*Hier Bild einfügen über die Strecke*

**Fastapi**=>**Containerimage**=>**Pipeline (GitHubAction)**=>**AppService**

---


# Modern Software Development


- Entwicklungsumgebungen in der Cloud verhindern zeitaufwändige Konfigurationen
- Ablösung von Monolithen durch Microservices
- Container erlauben Flexibilität und Skalierbarkeit
- Hoher Grad an Automatisierung (CI / CD)
- API first


---

# Hands on: FastApi

``` python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

[Dokumentation zu FastApi](https://fastapi.tiangolo.com/tutorial/request-files/)

---

# Containerization

---

# CI/CD

---

# Wrap Up

*vllt hier das bild zum Ablauf und beim Welcome nur grob betitelt*

----

# Thanks for taking part in the workshop!
## We'd like to welcome you on our virtual area at ITCS. Feel free to have a chat with us!

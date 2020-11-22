## API Doc
You can refer to the rich document by adding the following path to the base path of the url

* /doc
* /redoc

You can refer to openapi v3 json by adding the following

* /openapi.json

## Run localy

### 1. Start Server

Run `poetry run uvicorn server.app:app --host 0.0.0.0 --reload`

### 2. Check API Doc

Connect to the `http://localhost:8000/docs` from your browser

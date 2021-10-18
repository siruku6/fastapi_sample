# fastapi_sample
trying to use fastapi

# Setup Development Environment

```bash
$ git clone https://github.com/siruku6/fastapi_sample.git
$ cd fastapi_sample
$ pipenv install
```

# Check api behaviour

Run `uvicorn main:app --reload --host 0.0.0.0`,  
then you can access [FastAPI Swagger UI](http://0.0.0.0:8000/docs) with your browser.

```bash
# Test
$ curl 0.0.0.0:8000
```

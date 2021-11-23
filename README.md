# fastapi_sample
trying to use fastapi

# Setup Development Environment

## How to run server on Docker container

```bash
$ git clone https://github.com/siruku6/fastapi_sample.git
$ cd fastapi_sample
$ docker-compose build
$ docker-compose up
```

## How to run server localy

```bash
$ git clone https://github.com/siruku6/fastapi_sample.git
$ cd fastapi_sample
$ poetry install

# Run server
$ python main.py
# or
$ uvicorn main:app --reload --host 0.0.0.0
```

# Check api behaviour

You can access [FastAPI Swagger UI](http://localhost:8000/docs) with your browser.
And also running following commands can show you the behvaiour of API.

```bash
# Test
$ curl localhost:8000

# Other trial
$ curl -X POST http://localhost:8000/2/
{"message":"Received time taking job."}

$ curl -X GET http://localhost:8000/2/
{"message":"2は実行中です"}

$ curl -X DELETE http://localhost:8000/2/
{"message":"2の中止処理を受け付けました"}
```

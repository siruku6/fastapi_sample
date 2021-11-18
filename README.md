# fastapi_sample
trying to use fastapi

# Setup Development Environment

```bash
$ git clone https://github.com/siruku6/fastapi_sample.git
$ cd fastapi_sample
$ pipenv install
```

# Check api behaviour

Run `uvicorn main:app --reload --host 0.0.0.0` or `python server.py`  
then you can access [FastAPI Swagger UI](http://localhost:8000/docs) with your browser.

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

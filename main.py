import datetime
from pydantic import BaseModel
from typing import Dict, Optional
import time
from fastapi import FastAPI, BackgroundTasks, HTTPException

from rec import receive_api_request


class LongLastingJob(BaseModel):
    job_id: int
    is_cancelled: bool = False

    def __call__(self):
        try:
            _job = self
            for i in range(10):
                print(
                    f'{datetime.datetime.now():%H:%M:%S}',
                    'job[{}]: Running...({} / 10)'.format(self.job_id, i + 1)
                )
                time.sleep(1)

                if self.is_cancelled:
                    del _job
                    break
        except BaseException as error:
            print(error)
            del _job
        finally:
            print('job[{}]: 時間のかかる処理が終わりました'.format(self.job_id))



class JobsPool(BaseModel):
    jobs: Dict[int, LongLastingJob] = {}


app = FastAPI()
pool = JobsPool()


@app.get('/')
def hello():
    time.sleep(2)
    return {"text": "hello world!"}


@app.get('/get/{path}') # methodとendpointの指定
def path_and_query_params(
    path: str,
    # query: int,
    default_none: Optional[str] = None
):
    hoge_id: int = receive_api_request()
    return {"text": f"hello, {path} and {hoge_id}"}


@app.post('/{job_id}/', status_code=202)
def start(job_id: int, background_tasks: BackgroundTasks):

    # NOTE: This processing (job) is going to run on background.
    job = LongLastingJob(job_id=job_id)
    pool.jobs[job_id] = job
    background_tasks.add_task(job)

    return {"message": "Received time taking job."}


@app.delete('/{job_id}/', status_code=202)
def stop(job_id: int):
    t = pool.jobs.get(job_id)
    if t is None:
        raise HTTPException(400, detail="job is not exists.")

    t.is_cancelled = True
    del pool.jobs[job_id]
    return {"message": f"{job_id}の中止処理を受け付けました"}


@app.get('/{job_id}/', status_code=200)
def status(job_id: int):
    if job_id in pool.jobs:
        return {"message": f"{job_id}は実行中です"}
    else:
        return {"message": f"{job_id}は実行していません"}



# How to execute
# $ curl -X POST http://localhost:8000/2/
# {"message":"Received time taking job."}
# $ curl -X GET http://localhost:8000/2/
# {"message":"2は実行中です"}
# $ curl -X DELETE http://localhost:8000/2/
# {"message":"2の中止処理を受け付けました"}

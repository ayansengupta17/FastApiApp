from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit=10, published:bool=True, sort: Optional[str] = None):

    if published:
        return {"data": f"{limit} published blogs from DB"}
    else:
        return {"data":f"{limit}  blogs from DB"}


@app.get('/blog/unpublished')
def unpublished():
    return {"data": "all unpublished blogs"}


@app.get('/blog/{id}')
def show(id:int):
    return {"data": id}


@app.get('/blog/{id}/comments')
def show(id, limit=10):
    return limit



class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]




@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"blog is created with title {blog.title}"}




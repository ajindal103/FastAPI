from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {'data': 'blog list'}

@app.get('/blog')
def show_blogs(sort: Optional[str] = None, published: bool = False):
    if published:
        return {'data': 'Fetched published blogs'}
    else:
        return {'data': 'Fetched unpublished blogs'}
    
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None

@app.post('/blog')
def add_blog(request: Blog):
    return {'data': f'Blog Created: {request.title}'}
    
@app.get('/blog/{id}')
def show_blog(id: int):
    return {'data': f'Blog: {id} fetched'}

@app.get('/blog/{id}/comments')
def show_blog_comments(id: int):
    return {'data': f'Comments for Blog: {id} fetched'}

@app.get('/about')
def about():
    return "About Page"
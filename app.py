from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Text,Optional
from datetime import datetime
from uuid import uuid4 as uuid
app = FastAPI()

posts = [
    
]

#Post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    autor: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False

@app.get('/')
def read_root():
    return {'welcome':'Welcome to my API'}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post: Post):
    post.id = str(uuid())
    posts.append(post.model_dump())
    return posts[-1]

@app.get('/posts/{post_id}')
def get_post(post_id:str):
    for post in posts:
        if post['id'] == post_id:
            return post
    raise HTTPException(status_code=404,detail="Post not Found")

@app.delete('/posts/{post_id}')
def post_delete(post_id:str):
    for index,post in enumerate(posts):
        if post['id'] == post_id:
            posts.pop(index)
            return {'message':'Post has been deleted successfully'}
    
    raise HTTPException(status_code=404,detail="Post not Found")


@app.put('/posts/{post_id}')
def update_post(post_id:str,updatedPost: Post):
    for index,post in enumerate(posts):
        if post['id'] == post_id:
            posts[index]['title'] = updatedPost.title
            posts[index]['content'] = updatedPost.content
            posts[index]['author'] = updatedPost.autor
            return {'message':'Post has been updated successfully'}
        
    raise HTTPException(status_code=404,detail="Post not Found")
    



    
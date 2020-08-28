## Simple news board API. 

## It contains:

1. CRUD API managing posts and functionality of 'amount of upvotes'.

2. CRUD API managing comments. \

3. Endpoint to upvote the post.

4. Recurring job running once a day (I would use crontab) wasn't implemented...needed a little bit more time as I was doing some moments in task the first time.

### Postman:

{{base_url}}=127.0.0.1:8000

1. collection Account. The base URL for the API is http://127.0.0.1:8000.

- https://www.getpostman.com/collections/aa3f24a6fa5799400f17

functionality:

  -- user signup
  
  -- user login
  
  
2. collection Posts.

- https://www.getpostman.com/collections/9eab52c14672049eb954

- API for managing news (posts). The base URL for the API is http://127.0.0.1:8000.

functionality:

 -- get all posts
  
 -- create post
  
 -- update post
  
 -- delete post
 
 -- upvote post
  
  
3. collection Comments.
 
- https://www.getpostman.com/collections/7b6f32bd8e87c3711b58
 
- API for managing comments. The base URL for the API is http://127.0.0.1:8000.
  
functionality:

 -- get all comments
  
 -- create comment
  
 -- update comment
  
 -- delete comment
  

### Heroku: https://maberrnews.herokuapp.com/

### Additional:

- The code is formatted with BLACK.

- Flake8 linter passes.

### Docker

- added Dockerfile and docker-compose.yml
  
  to run:
  
  -- $ sudo docker-compose up

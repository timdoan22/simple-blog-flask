from flask import Flask, render_template
from post import Post
import requests

blog_posts = requests.get('https://api.npoint.io/024ab59e1e34f61cf47f').json()
post_objects = []
for post in blog_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', blog_posts=post_objects)

@app.route('/post/<int:index>')
def get_blog(index):
    blog_post = None
    for post in post_objects:
        if post.id == index:
            blog_post = post
        
    return render_template('blog_entry.html', blog_entry=blog_post)

if __name__ == "__main__":
    app.run(debug=True)

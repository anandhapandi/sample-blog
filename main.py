from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated database of blog posts
posts = [
    {
        'id': 1,
        'title': 'First Blog Post',
        'content': 'This is the content of the first blog post.',
    },
    {
        'id': 2,
        'title': 'Another Blog Post',
        'content': 'Here is some more content for another blog post.',
    },
    {
        'id': 3,
        'title': 'Third Blog Post',
        'content': 'This is the third blog post in our demo app.',
    }
]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle the form submission for adding a new post
        title = request.form.get('title')
        content = request.form.get('content')
        new_post = {
            'id': len(posts) + 1,
            'title': title,
            'content': content
        }
        posts.append(new_post)
        return redirect(url_for('home'))
    
    # Render the homepage and pass the list of posts
    return render_template('home.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        return "Post not found", 404
    return render_template('post.html', post=post)

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = {
            'id': len(posts) + 1,
            'title': title,
            'content': content
        }
        posts.append(new_post)
        return redirect(url_for('home'))
    return render_template('add_post.html')

if __name__ == '__main__':
    app.run(debug=True)


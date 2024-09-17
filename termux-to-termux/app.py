from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []
posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    if username not in users:
        users.append(username)
    return redirect(url_for('index'))

@app.route('/post', methods=['POST'])
def post():
    user = request.form['user']
    content = request.form['content']
    if user in users:
        posts.append({'user': user, 'content': content})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, url_for, request, redirect
from markupsafe import escape


app = Flask(__name__)
app.run(debug=True)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>, This is Yaser"
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route("/test")
def api_call():
    return "This is an API call"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!. This is good"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>/<int:test_id>')
def show_subpath(subpath, test_id):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)} | and id is {test_id}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.json["values"]["username"]
        password = request.json["values"]["password"]
        message = request.json["values"]["message"]["text"]
        return {
            "status":200,
            "message":f"Here is your username: {username} then your password: {password} and your message is {message}",
        }
    else:
        return "put your credentials pls"

@app.route("/json", methods=["GET", "POST", "PUT"])
def json():
    return {
        "response":200,
        "fields":{
            'username':'y.alattas',
            'token':'hereIsYourRandomToken',
            'expires_at':'2020-09-25'
        }
    }

@app.route('/query', methods=["GET", "POST"])
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')

    # if key doesn't exist, returns a 400, bad request error
    framework = request.args['framework']

    # if key doesn't exist, returns None
    website = request.args.get('website')

    return '''
              <h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)

# allow both GET and POST requests
# allow both GET and POST requests
@app.route('/query-api', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        language = request.json['language']
        framework = request.json['framework']
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''
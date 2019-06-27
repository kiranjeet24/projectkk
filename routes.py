from app import app
@app.route('/')
@app.route('/index')
def index():
    user={'username':'david'}
    return'''
    <html>
    <head>
    <title>MY APPLICATION</title>
    </head>
    <body bgcolor='pink'>
    <h1>Hello,'''+user['username']+'''!</h1>
    </body>
    </html>'''
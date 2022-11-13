from flask import render_template
from app import app
from flask import request
import time
from flask import request, current_app, g
@app.before_request
def before_request():
    g.start_time = time.time()


# After request handler
@app.after_request
def after_request(response):
    global start_time
    t = time.time() - g.start_time
    current_app.logger.debug(f"Time used: {time.time() - g.start_time}")

    return response


@app.route('/')
def home():

    return render_template("index.html")
    
    
@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST':
        ans = []
        for i in range(1000):
            tmp = i ** (1000)
            ans.append(tmp)

        return f'{ans}'
    else:
        return 'Hello Dcnlab'


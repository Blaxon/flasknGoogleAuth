from flask import Flask

import functools
import json
import os

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import google_auth


app = Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)

app.register_blueprint(google_auth.app)


@app.route('/')
def hello_world():  # orig: use this get file css/js/icon...
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        return '<div>You are currently logged in as ' + \
               user_info['given_name'] + \
               '<div><pre>' + \
               json.dumps(user_info, indent=4) + \
               "</pre>"

    return 'You are not currently logged in.'


@app.route('/bot/availableEndpoints')
def get_endpoints():
    return ''


@app.route('/bot/getUserid')
def get_userid():
    return ''


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

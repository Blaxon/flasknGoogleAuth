export FN_AUTH_REDIRECT_URI=http://localhost:8040/google/auth
export FN_BASE_URI=http://localhost:8040
export FN_CLIENT_ID=THE CLIENT ID WHICH YOU CREATED EARLIER
export FN_CLIENT_SECRET=THE CLIENT SECRET WHICH YOU CREATED EARLIER

export FLASK_APP=app.py
export FLASK_DEBUG=1
export FN_FLASK_SECRET_KEY=happysecret

python -m flask run -p 8040
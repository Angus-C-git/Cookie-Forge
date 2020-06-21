from flask import Flask, session
from flask.sessions import SecureCookieSessionInterface


app = Flask("Cookie Forge")
app.secret_key = "$hallICompareTHEE2aSummersday"

# 1. this is what I was looking for
session_serializer = SecureCookieSessionInterface().get_signing_serializer(app)

@app.route("/")
def home():
	return f"<h1>Welcome To The Cookie Forge [Alpha--]</h1><br><a href='./forge'>Forge</a><br><a href='./usage'>Usage</a>"

@app.route("/forge")
def test():
    session = {"role": "Admin", "username": "admin"}
    # 2. and this is how I needed to use it
    session_cookie = session_serializer.dumps(dict(session))
    print(session_cookie)
    return f"<h1 align='center'>Forged Cookie:</h1></br><p>{session_cookie}</p><br><a href=/forge>Forge Another</a>"

@app.route("/usage")
def usage():
	return f"<h1>Usage</h1><br><p>Change the Flask secret_key variable in the source to your liking and refresh, the `session` varible can be smilarly adjusted.</p>"

if __name__ == "__main__":
	app.run(debug=True)
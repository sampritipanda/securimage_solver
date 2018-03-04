from flask import Flask, request, abort, send_file
import shellescape
import captcha_api
import os

app = Flask(__name__)

@app.route("/predict")
def predict():
    url = shellescape.quote(request.args.get("url").encode())
    sessid = request.args.get("sessid").encode()
    if not set(sessid).issubset(set('0123456789abcdefghijklmnopqrstuvwxyz')):
        abort(404)

    command = 'curl {} -H "Cookie: PHPSESSID={}" > /tmp/captcha.png'.format(url, sessid)
    os.system("rm /tmp/captcha.png")
    print command
    os.system(command)
    return captcha_api.predict('/tmp/captcha.png')

@app.route("/current_image")
def current_image():
    return send_file('/tmp/captcha.png')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

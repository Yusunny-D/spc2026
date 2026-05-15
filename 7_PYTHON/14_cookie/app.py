from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/set-cookie")
def set_cookie():
    res = make_response("Cookie has been set!")
    res.set_cookie("my-edu", "spc2026")
    return res

@app.route('/get-cookie')
def get_cookie():
    cookie = request.cookies.get('my-edu')
    print(cookie)


    return f'안녕, {cookie}야'

if __name__=="__main__":
    app.run(debug=True)
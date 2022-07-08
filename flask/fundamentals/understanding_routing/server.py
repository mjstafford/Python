from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/dojo")
def say_dojo():
    return "Dojo!"

@app.route("/say/<string:name>")
def say_name(name):
    return f"Hi {name}!"

@app.route("/repeat/<int:num>/<string:name>")
def say_words(num, name):
    return f"{name * num}"

@app.route("/<path:wrong>")
def wrong_url(wrong):
    return f"{wrong} is not a correct url path"



if __name__=="__main__":
    app.run(debug=True)
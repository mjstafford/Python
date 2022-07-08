from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
def blue():
    return render_template("index.html", look="original")
    # return render_template("play.html")

@app.route("/play/<int:num>")
def blue_and_multiplied(num):
    return render_template("index.html", num=num, look="multiply")
    # return render_template("play_num.html", num=num)

@app.route("/play/<int:num>/<string:color>")
def color_and_multiplied(num, color):
    return render_template("index.html", num=num, color=color, look="last")
    # return render_template("play_num_color.html", num=num, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
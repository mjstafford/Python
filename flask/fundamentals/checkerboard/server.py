from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def checkers():
    return render_template("index.html")

@app.route("/4")
def checkers_four():
    return render_template("index_four.html")

@app.route("/<int:rows>/<int:columns>")
def checkers_rows_cols(rows,columns):
    return render_template("index_rows_cols.html", rows=rows, cols=(int(columns/2)))

@app.route("/<int:rows>/<int:columns>/<string:color1>/<string:color2>")
def checkers_rows_cols_colors(rows,columns, color1, color2):
    return render_template("index_rows_cols_colors.html", rows=rows, cols=(int(columns/2)), color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)

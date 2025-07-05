from flask import *
from math import *
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def calc():
    exp = request.form.get("expression", "")
    res = ""
    a = 0
    but = request.form.get("button")
    if request.method == 'POST':
        if but == "=":
            try:
                res = eval(exp)
            except:
                res = "UNDEFINED"
        elif but == "C" or but == "c":
            exp = ""
            res = ""
        elif but == "root":
            try:
                a = int(exp)
                res = sqrt(a)
            except:
                res = "first eval the equation"
        else:
            exp = exp+but
    return render_template("index.html", exp=exp, res=res)


if __name__ == "__main__":
    app.run(debug=True)

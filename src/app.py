from flask import *

app = Flask(__name__)

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        query = request.form.get("query")
        return redirect(url_for("search_results", query=query))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)

from flask import Flask, request, make_response
app = Flask(__name__)
@app.route("/")
def index():
    print"do something"
    response = make_response("index")
    response.set_cookie("name1","itcast")
    response.set_cookie("name2","itcast",max_age=3600)
    return response
if __name__ == "__main__":
    print app.url_map
    app.run(debug=True)

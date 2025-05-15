from flask import Flask, request, render_template

app = Flask("test server", static_url_path="/static", static_folder="static")

db = {
    "Karin": {
        "age": 23,
        "height": 1.70
    },
    "John": {
        "age": 25,
        "height": 1.80
    }
}


"""
www.learn.knivkit.com/
"""
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/models")
def function1():

    """
    www.learn.knivkit.com/models
    """
    return "<p>Model</p>"

@app.route('/models_n/model')
def show_model_n():
    return f'Model input:'

@app.route('/models/<model>')
def show_model(model):
    """
    www.learn.knivkit.com/models/building1
    www.learn.knivkit.com/models/building234
    """
    print(model)
    return {"content": f'Model input: {model}'}

@app.route("/post_model", methods=["POST"])
def post_model():
    """

    requests.post(url="http://172.22.203.223:3000/post_model", json={"a": "b"})

    """
    my_input = request.get_json()
    print(my_input)
    return my_input["a"]

@app.route("/update_db", methods=["POST"])
def update_db():
    """

    requests.post(url="http://172.22.203.223:3000/post_model", json={"a": "b"})

    """
    my_input = request.get_json()
    print(my_input)
    db.update(my_input)
    print(db)
    return my_input


@app.route("/template/<name>")
def template(name):
    user_info = db.get(name)
    return render_template("1.html", info=user_info)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)





# @app.route("/template")
# def template():
#     n = {"name": 234}
#     return render_template("1.html", name="Karin")
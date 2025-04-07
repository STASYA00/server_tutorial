from flask import Flask, request

app = Flask("test server")


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
    return f'Model input: {model}'

@app.route("/post_model", methods=["POST"])
def post_model():
    """

    requests.post(url="http://172.22.203.223:3000/post_model", json={"a": "b"})

    """
    my_input = request.get_json()
    print(my_input)
    return my_input["a"]


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
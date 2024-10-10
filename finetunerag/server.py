from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


def start_server():
    app.run(host='0.0.0.0', port=3003)


# uncomment the below to run the server directly to test the application
# if __name__ == "__main__":
#     start_server()

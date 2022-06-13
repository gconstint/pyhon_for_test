from flask import Flask


# def power(n=10):
#     return ', '.join(str(2 ** i) for i in range(n))


app = Flask(__name__)


@app.route('/')
def power(n=10):
    return ', '.join(str(2 ** i) for i in range(n))


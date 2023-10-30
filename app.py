from flask import Flask

app = Flask(__name)

@app.route('/')
def hello():
    return "Bonjour"

if __name__ == '__main__':
    app.run()

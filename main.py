from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'CI/CD demo class'

#app.run(host='0.0.0.0', port=81)

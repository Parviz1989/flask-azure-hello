from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello again and again baby from Azure App Service (Python) 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

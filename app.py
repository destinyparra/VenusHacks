from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bathroom Locator is Working!</h1><p>Ready to build your campus bathroom finder!</p>"

@app.route('/map')
def map_view():
    return "<h1>Map View</h1><p>Bathroom map coming soon!</p>"

if __name__ == '__main__':
    app.run(debug=True)
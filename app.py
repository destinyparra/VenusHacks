from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; background-color:  #FFFFFF; }
            .container { max-width: 800px; margin: 0 auto; padding: 2rem; }
            h1 { color: #2c3e50; text-align: center; }
            p { color: #800080; text-align: center; font-size: 1.1rem; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Auntie Flows Crimson Compass</h1>
            <p>LOCATE PERIOD ITEMS NOW</p>
        </div>
    </body>
    </html>
    """

@app.route('/map')
def map_view():
    return """
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; background-color: #800080 }
            .container { max-width: 800px; margin: 0 auto; padding: 2rem; }
            h1 { color: #2c3e50; text-align: center; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Map View</h1>
            <p>Bathroom map coming soon!</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
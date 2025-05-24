from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# ...existing code...
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
from flask import Flask, render_template_string
import random

app = Flask(__name__)

quotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "It always seems impossible until it's done.",
    "Success is not in what you have, but who you are.",
    "You miss 100% of the shots you don’t take.",
]

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>InspireMe</title>
    <style>
        body {
            background-color: #f2f2f2;
            text-align: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 50px;
        }
        h1 {
            color: #2c3e50;
        }
        p {
            font-size: 1.4rem;
            color: #34495e;
            margin-top: 20px;
        }
        a {
            text-decoration: none;
            color: #3498db;
            margin-top: 40px;
            display: inline-block;
        }
    </style>
</head>
<body>
    <h1>✨ Welcome to InspireMe! ✨</h1>
    <p>{{ quote }}</p>
    <a href="/about">About this app</a>
</body>
</html>
"""

ABOUT_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>About InspireMe</title>
</head>
<body>
    <h1>About This App</h1>
    <p>This is me testing the CI changes I implemented.</p>
    <a href="/">Back to home</a>
</body>
</html>
"""

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template_string(TEMPLATE, quote=quote)

@app.route('/about')
def about():
    return render_template_string(ABOUT_PAGE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_quote():
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url)
        data = response.json()
        quote = data[0]['q'] + " - " + data[0]['a']
        return quote
    except Exception as e:
        print(f"Error retrieving quote: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_quote')
def get_quote_route():
    quote = get_quote()
    if quote:
        return render_template('quote.html', quote=quote)
    else:
        return "Error retrieving quote. Please try again later."

if __name__ == "__main__":
    app.run(debug=True)

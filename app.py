from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Store the history of submitted URLs in a list
url_history = []
secret_data = os.getenv("FIRSTDATA")
print(secret_data)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url_input']
        if url:  # Only add non-empty URLs to history
            url_history.append(url)
        print(f"User submitted URL: {url}")
        return redirect(url_for('index'))
    return render_template('index.html', history=url_history, secret_data=secret_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

from flask import Flask, render_template, request


app = Flask(__name__)

import json

rates = { 'USD' : 4.2534, 'AUD': 3.0156, 'CAD':3.1916, 'EUR': 4.6388}

@app.route("/currency", methods=["GET", "POST"])
def currency():
  if request.method == "POST":
    data = request.form
    code = data.get('code')
    amount = float(data.get("amount"))
   

    if code in rates:
      return render_template("index.html", amount = amount*rates[code])
    
 
  return render_template('index.html', amount=0)


if __name__ == "__main__":
  app.run(debug=True)
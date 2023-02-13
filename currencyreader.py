
import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

from flask import Flask, render_template, request


app = Flask(__name__)


import os

os.path.join(os.getcwd(), 'rates.csv')


@app.route("/currency", methods=["GET", "POST"])
def currency():
  if request.method == "POST":
    data = request.files
    code = data.get('code')
    amount = data.get("amount")
    

    if code == code["USD"]:
      return amount*4.2534
    if code == code["AUD"]:
      return amount*3.1916
    if code == code["CAD"]:
      return amount*3.1916
    if code == code["EUR"]:
      return amount*4.6388
 
  return render_template('index.html', amount=0)


if __name__ == "__main__":
  app.run(debug=True)
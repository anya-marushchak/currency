
import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

from flask import Flask, render_template, request


app = Flask(__name__)


import os

os.path.join(os.getcwd(), 'rates.csv')


@app.route("/currency", methods=["GET"])
def currency():
    return render_template('index.html')


@app.route("/amount/", methods=["POST"])
def result():
  if request.method == "POST":
    data = request.form
    code = data.get('code')
    amount = data.get("amount")


    if code == code["USD"]:
      return amount*4.2534
    if code == code[""]:
      return amount*3.1916
    if code == code[]:
      return amount*3.1916
    if code == code[]:
      return amount*4.6388
 

  return render_template('amount.html', amount=0)


if __name__ == "__main__":
  app.run()
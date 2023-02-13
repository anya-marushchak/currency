
import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/currency", methods=["GET", "POST"])
def currency():
  if request.method == "POST":
    data = request.form
    code = data.get('code')
    amount = float(data.get("amount"))
   

    if code in rates.json:
      return render_template("index.html", amount = amount*rates.json[code])
    
 
  return render_template('index.html', amount=0)


if __name__ == "__main__":
  app.run(debug=True)
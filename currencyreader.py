
import requests,json


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

for item in data:
   rates = item['rates']
   print(rates)
   for item in rates:
     bid = item['bid']
     print(bid)


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/currency", methods=["GET", "POST"])
def currency():
  if request.method == "POST":
    data = request.form
    code = data.get('code')
    amount = float(data.get("amount"))
   
    
    for item in rates:
        if code == 'USD':
            return  render_template("index.html", amount = amount*item['bid'])
        if code == 'AUD':
            return  render_template("index.html", amount = amount*item['bid'])
        
  return render_template('index.html', amount=0)


if __name__ == "__main__":
  app.run(debug=True)
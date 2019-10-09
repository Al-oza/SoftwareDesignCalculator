from flask import Flask
from flask import render_template, request, redirect
from decimal import Decimal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle = 'My Loan Calculator')

@app.route('/calc', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        form = request.form
        loanAmount = int(form['loanAmount'])
        nPayments = int(form['nPayments'])
        intRate = Decimal(form['intRate'])
        firstD = ((1+intRate)**nPayments)-1
        secondD = (((1+intRate)**nPayments)*intRate)
        calc = '${:,.2f}'.format(Decimal(loanAmount/(firstD/secondD)))
        return render_template('index.html', display=calc, pageTitle="My Loan Calculator")

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)

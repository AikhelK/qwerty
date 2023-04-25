from flask import Flask, render_template

app = Flask(__name__)

menu = [{"name": "Главная", "url": "/"},
        {"name": "Заказы", "url": "orders"},
        {"name": "Сотрудники", "url": "employers"},
        {"name": "Анализ", "url": "analysis"},]

@app.route('/')
def index():
    return render_template("index.html", menu=menu)

@app.route('/orders')
def orders():
    return render_template("orders.html", title="Заказы", menu=menu)

@app.route('/employers')
def employers():
    return render_template("employers.html", title="Сотрудники", menu=menu)

@app.route('/analysis')
def analysis():
    return render_template("analysis.html", title="Анализ", menu=menu)

if __name__ == "__main__":
    app.run(debug = True,port=3000, host='0.0.0.0')
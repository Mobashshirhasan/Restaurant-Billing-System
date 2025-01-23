from flask import Flask, request, render_template, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

app = Flask(__name__, static_url_path='/static')

class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def generate_invoice(self, prices, total_cost, payment, change):
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        c.drawString(100, height - 50, "Bill Invoice:")
        c.drawString(100, height - 70, "-----------------------------")
        
        y = height - 90
        for item, quantity in self.items.items():
            cost = quantity * prices.get(item, 0)  # Use get() with default value of 0
            c.drawString(100, y, f"{item}: {quantity} x ${prices.get(item, 'N/A')} = ${cost}")
            y -= 20
        
        c.drawString(100, y, "------------------------------")        
        y -= 20
        c.drawString(100, y, f"Total: ${total_cost}")
        y -= 20
        c.drawString(100, y, f"Payment: ${payment}")
        y -= 20
        c.drawString(100, y, f"Change: ${change}")
        y -= 40  #  Adding extra space before the thank you message

        c.drawString(100, y, "Thank You For Shopping, Please visit again!")

        c.showPage()
        c.save()
        buffer.seek(0)
        return buffer

# Prices of items in dollars
prices = {
    "samosa": 10,
    "vada pav": 10,
    "pani puri/golgappa": 20,
    "bhel puri": 30,
    "chole bhature": 75,
    "pav bhaji": 65,
    "dosa": 65,
    "idli": 40,
    "chaat": 35,
    "pakora": 35
}

# Create an instance of the Order class
order = Order()

@app.route('/')
def index():
    return render_template('index.html', prices=prices, items=order.items)

@app.route('/add_item', methods=['POST'])
def add_item():
    item = request.form['item'].lower()
    quantity = float(request.form['quantity'])
    
    if item not in prices:
        return "Item not available", 400
    
    order.add_item(item, quantity)
    return render_template('index.html', prices=prices, items=order.items)

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    try:
        total_cost = sum(quantity * prices.get(item, 0) for item, quantity in order.items.items())
        payment = float(request.form['payment'])
        if payment < total_cost:
            return "Insufficient payment", 400
        
        change = payment - total_cost
        buffer = order.generate_invoice(prices, total_cost, payment, change)
        
        return send_file(buffer, as_attachment=True, download_name="invoice.pdf", mimetype='application/pdf')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)

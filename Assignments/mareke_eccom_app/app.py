from flask import Flask, render_template, request, redirect, url_for, session
from market_ecomm.customer_signin import email_check
from market_ecomm.discount import check_coupon
from market_ecomm.market import items

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Route: Home
@app.route('/')
def home():
    return render_template('home.html', items=items)

# Route: Login
@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        session['name'] = request.form['name']
        email = request.form['email']
        if email_check(email):
            session['email'] = email
            return redirect(url_for('shop'))
        else:
            return render_template('login.html', error="Invalid Email!")
    return render_template('login.html')

# Route: Shop
@app.route('/shop', methods=['GET', 'POST'])
def shop():
    if 'cart' not in session:
        session['cart'] = {}

    if request.method == 'POST':
        item = request.form['item']
        quantity = int(request.form['quantity'])
        cart = session['cart']
        cart[item] = cart.get(item, 0) + quantity
        session['cart'] = cart

    return render_template('cart.html', cart=session['cart'], items=items)

# Route: Checkout
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', {})
    total_cost = sum(items[item] * quantity for item, quantity in cart.items())

    if request.method == 'POST':
        coupon = request.form.get('coupon')
        total_cost = check_coupon(cart, coupon)
        return render_template('checkout.html', total_cost=total_cost)

    return render_template('checkout.html', cart=cart, items=items, total_cost=total_cost)

if __name__ == '__main__':
    app.run(debug=True)

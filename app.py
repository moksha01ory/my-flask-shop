from flask import Flask, render_template, redirect, url_for , jsonify, request, session
from classes import Men, Women, Kids
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "mysecret123"
users={}
women = Women()
men = Men()
kids = Kids()

categories = {
    "Men": men,
    "Women": women,
    "Kids": kids
}

wishlist = []   # GLOBAL WISHLIST
cart = []

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/categories')
def show_categories():
    return render_template('categories.html', categories=categories.keys())

@app.route('/categories/<category>/<subcategory>')
def show_subcategory(category, subcategory):
    cat = categories.get(category)
    if not cat or subcategory not in cat.products:
        return "<h2>No products found</h2>"

    products = cat.products[subcategory]

    # Send wishlist IDs so hearts turn red
    wishlist_ids = [item["id"] for item in wishlist]

    return render_template(
        'subcategory.html',
        category=category,
        subcategory=subcategory,
        products=products,
        wishlist_ids=wishlist_ids
    )

@app.route('/product/<category>/<subcategory>/<int:product_id>')
def product_page(category, subcategory, product_id):

    cat = categories.get(category)
    if not cat:
        return "Category not found"

    product_list = cat.products.get(subcategory, [])

    product = next((p for p in product_list if p["id"] == product_id), None)

    if not product:
        return "Product not found"

    # ✅ FIX: You forgot this return statement
    return render_template("product.html",
                           product=product,
                           category=category,
                           subcategory=subcategory)


@app.route('/add_wishlist/<category>/<subcategory>/<int:product_id>')
def add_wishlist(category, subcategory, product_id):

    cat = categories.get(category)
    product_list = cat.products.get(subcategory, [])
    product = next((p for p in product_list if p["id"] == product_id), None)

    if product and product not in wishlist:
        wishlist.append(product)

    # Stay on the product page after adding to wishlist
    return redirect(url_for('product_page',
                            category=category,
                            subcategory=subcategory,
                            product_id=product_id)) 

@app.route('/add_wishlist_ajax', methods=['POST'])
def add_wishlist_ajax():
    data = request.json
    category = data.get("category")
    subcategory = data.get("subcategory")
    product_id = data.get("product_id")

    cat = categories.get(category)
    if not cat:
        return jsonify({"status": "error", "message": "Category not found"})

    product_list = cat.products.get(subcategory, [])
    product = next((p for p in product_list if p["id"] == product_id), None)

    if product:
        wishlist.append(product)
        return jsonify({"status": "success", "message": "Added to wishlist"})

    return jsonify({"status": "error", "message": "Product not found"})

@app.route('/remove_wishlist/<int:product_id>')
def remove_wishlist(product_id):
    global wishlist
    wishlist = [item for item in wishlist if item["id"] != product_id]
    return redirect(url_for("wishlist_page"))

@app.route('/toggle_wishlist/<category>/<subcategory>/<int:product_id>', methods=['POST'])
def toggle_wishlist(category, subcategory, product_id):

    cat = categories.get(category)
    product_list = cat.products.get(subcategory, [])

    product = next((p for p in product_list if p["id"] == product_id), None)
    if not product:
        return {"added": False}

    # Remove if already in wishlist
    if product in wishlist:
        wishlist.remove(product)
        return {"added": False}

    # Add if not
    wishlist.append(product)
    return {"added": True}

# ❤ WISHLIST PAGE
@app.route('/wishlist')
def wishlist_page():
    return render_template("wishlist.html", wishlist=wishlist)

@app.route('/account')
def account_page():
    username = session.get('username')
    if username:
        name = users[username]['name']
        return render_template('account.html', name=name)
    else:
        return redirect(url_for('login_page'))

@app.route('/orders')
def orders():
    return render_template('orders.html')

# SIGNUP
@app.route('/signup_page', methods=['GET', 'POST'])
def signup_page():
    global users
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        password = request.form['password']

        if username in users:
            return render_template('signup.html', error="Username already exists")

        users[username] = {
            'name': name,
            'password_hash': generate_password_hash(password)
        }

        session['username'] = username
        session['wishlist'] = []
        return redirect(url_for('account'))

    return render_template('signup.html')


# LOGIN
@app.route('/login_page', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users.get(username)
        if not user or not check_password_hash(user['password_hash'], password):
            return render_template('login.html', error="Invalid username or password")

        session['username'] = username
        if 'wishlist' not in session:
            session['wishlist'] = []
        return redirect(url_for('account'))

    return render_template('login.html')


# LOGOUT
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('wishlist', None)
    return redirect(url_for('home'))


# ACCOUNT DASHBOARD
@app.route('/account')
def account():
    username = session.get('username')
    if username:
        name = users[username]['name']
        wishlist = session.get('wishlist', [])
        return render_template('account.html', name=name, wishlist=wishlist)
    else:
        return redirect(url_for('login_page'))

@app.route('/cart')
def cart_page():
    return render_template('cart.html')

@app.route('/add_to_cart/<category>/<subcategory>/<int:product_id>')
def add_to_cart(category, subcategory, product_id):

    cat = categories.get(category)
    product_list = cat.products.get(subcategory, [])

    product = next((p for p in product_list if p["id"] == product_id), None)

    if product:
        cart.append(product)

    return redirect(url_for('cart_page'))

if __name__ == '__main__':
    app.run(debug=True)
import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        
        # Get from users table username and cash owned
        row = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])
        username = row[0]["username"]
        cash = float(row[0]["cash"])
        grand_total = cash
    
        # Get from portfolio table stocks owned and sum of shares
        portfolio = db.execute(
            "SELECT symbol, SUM(quantity) as quantity FROM portfolio WHERE username = :id GROUP BY symbol", id=session["user_id"])
    
        # Loop to assign current price and value of each stock
        for i in portfolio:
    
            # Get current price via Application Programming Interface
            quote = lookup(i["symbol"])
            i["current_price"] = round(float(quote["price"]), 2)
    
            # Set stocks value and total cash+value owned
            i["total"] = round(float(i["current_price"] * i["quantity"]), 2)
            grand_total += i["total"]
    
        # Return values, some rounded already, some rounding in return function
        return render_template("index.html", cash=f"${cash:,.2f}", username=username, portfolio=portfolio, grand_total=f"${grand_total:,.2f}")

    # User reached route via POST (as by submitting a form via POST) - wants to buy a stock or add cash or change password
    else:
        # User submitting Add money button
        add_cash = int(request.form.get("addcash"))
        old_cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        new_cash = old_cash[0]["cash"] + add_cash
        update = db.execute("UPDATE users SET cash = :newcash WHERE id = :id", newcash=new_cash, id=session["user_id"])
        
        # User submitting Buy shares button
        
        
        return redirect("/")
        

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("buy.html")

    # User reached route via POST (as by submitting a form via POST) - wants to buy a stock
    else:

        # Make symbol uppercase and lookup in API
        stock = lookup(request.form.get("symbol").upper())

        # Ensure symbol exists, if not return apology
        if not stock:
            return apology("Stock doesn't exist", 400)

        # Define nbr of shares by try to handle fractional shares in check50
        try:
            qty = int(request.form.get("shares"))
        except ValueError:
            return apology("shares must be an integer", 400)
            
        # Define variables to make it easier   
        name = stock["name"]
        price = stock["price"]
        symbol = stock["symbol"]
        cost = price * qty

        # Ensure user entered desired number of shares
        if qty > 1000000 or qty < 1 or not qty:
            return apology("Please provide real number of shares (positive integer)", 400)

        # Check if user can afford to buy stock
        money = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        if money[0]["cash"] < cost:
            return apology("You cannot aford to buy it", 400)

        else:

            # Decrease user's cash by cost of stock
            balance = money[0]["cash"] - cost
            money = db.execute("UPDATE users SET cash = :bal WHERE id = :id", bal=balance, id=session["user_id"])

            # Buy stock - add values to table portfolio
            bought = db.execute("INSERT INTO portfolio(username, symbol, price, quantity) VALUES(:username, :symbol, :price, :quantity)",
                                username=session["user_id"], symbol=symbol, price=price, quantity=f"{qty:,.2f}")
            return redirect("/")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""

    # Get username from register.html's $.get and select users table
    username = request.args.get("username")
    users = db.execute("SELECT username FROM users WHERE username = :username", username=username)
    
    # Ensure name is not taken and at has at least 1 character
    if users or len(username) < 1:
        return jsonify(False)
    else:
        return jsonify(True)
       
        
@app.route("/passw", methods=["GET"])
def passw():
    """Return true if password meets requirements, else false, in JSON format"""

    # Get password from register.html's $.get
    passw = request.args.get("password")
  
    # Ensure requirements are met
    check = 0
    y = 0
    print(len(passw))
    for i in passw:
        
        # Break loop when found big letter - no need to continue
        if i.isupper():
            break
        check += 1
        
        # False when all letters don't meet requirement
        if check == len(passw):
            return jsonify(False)

    # Ensure password has at least 1 number - mirror to for loop above
    check = 0
    for j in passw:
        if j.isdigit():
            y = 1
            break
        check += 1
        if check == len(passw):
            return jsonify(False)
            
    # Again, but for special character
    check = 0
    z = "`~!@#$%^&*()\'_+=-\"][}{';|:/.,?><\|-*/"
    for k in passw:
        if k in z:
            y = 2
            break
        check += 1
        print(check)
        if check == len(passw):
            print("sprawdzam")
            return jsonify(False)
    # Btw I could also make l=ord(k) and check it by ASCII table
            
    if y == 2 and len(passw) > 7:
        return jsonify(True)
    else:
        return jsonify(False)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Get from portfolio table all info
    portfolio = db.execute("SELECT * FROM portfolio WHERE username = :id", id=session["user_id"])
    return render_template("history.html", portfolio=portfolio)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("quote.html")

    # User reached route via POST (as by submitting a form via POST)
    else:

        # Make symbol uppercase and lookup in API
        quote = lookup(request.form.get("symbol").upper())

        # Ensure symbol exists, if not return apology
        if not quote:
            return apology("Stock doesn't exist", 400)

        # Return price of a stock
        return render_template("quoted.html", name=quote["name"], price=quote["price"], symbol=quote["symbol"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Missing username!", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Missing password!", 400)

        # Ensure password was submitted
        elif not request.form.get("confirmation"):
            return apology("Missing password confirmation!", 400)

        # Ensure password and confirmation match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Password and confirmation do not match", 400)

        else:

            # Query database and check if username already exists
            rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
            if rows:
                return apology("Username already exists", 400)

            # Hash password and add user to database
            hash = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
            rows = db.execute("INSERT INTO users(username, hash) VALUES(:username, :hash)",
                              username=request.form.get("username"), hash=hash)

            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE username = :username",
                              username=request.form.get("username"))

            # Login user automatically and remember
            session["user_id"] = rows[0]["id"]

            # Redirect user to home page
            return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        # Get from portfolio table symbols bought to pass it into select options in sell.html
        portfolio = db.execute("SELECT symbol FROM portfolio WHERE username = :id GROUP BY symbol", id=session["user_id"])
        return render_template("sell.html", portfolio=portfolio)

    # User reached route via POST (as by submitting a form via POST) - wants to sell a stock
    else:

        # Make symbol uppercase just in case and lookup in API
        stock = lookup(request.form.get("symbol").upper())

        # Ensure symbol exists, if not return apology
        if not stock:
            return apology("Stock doesn't exist", 403)
            
        # Define nbr of shares by try to handle fractional shares in check50
        try:
            qty = int(request.form.get("shares"))
        except ValueError:
            return apology("nbr of shares must be an integer", 400)

        # Define variables to make it easier)
        price = stock["price"]
        symbol = stock["symbol"]
        cost = price * qty

        # Check if user has that quantity of shares
        portfolio = db.execute(
            "SELECT symbol, SUM(quantity) as shares FROM portfolio WHERE symbol = :symbol AND username = :id GROUP BY symbol", id=session["user_id"], symbol=symbol)
        if portfolio[0]["shares"] < qty:
            return apology("You don't have that many shares to sell", 400)

        else:
            # Increase user's total cash by value of stock
            money = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
            balance = money[0]["cash"] + cost
            money = db.execute("UPDATE users SET cash = :bal WHERE id = :id", bal=balance, id=session["user_id"])

            # Sell stock - add negative value and all info to table portfolio
            sold = db.execute("INSERT INTO portfolio(username, symbol, price, quantity) VALUES(:username, :symbol, :price, :quantity)",
                              username=session["user_id"], symbol=symbol, price=price, quantity=f"{-qty:,.2f}")
            return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks."""

    # Buscar transações do usuário agrupadas por símbolo
    transactions = db.execute("""
        SELECT
            symbol,
            SUM(CASE WHEN transaction_type = 'buy' THEN shares ELSE -shares END) as total_shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_shares > 0
    """, session["user_id"])

    # Buscar saldo do usuário
    user = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = user[0]["cash"]

    # Preparar portfólio com preços atuais
    portfolio = []
    total_stocks_value = 0

    for transaction in transactions:
        symbol = transaction["symbol"]
        shares = transaction["total_shares"]

        # Buscar preço atual
        stock = lookup(symbol)
        if stock:
            current_price = stock["price"]
            total_value = shares * current_price

            portfolio.append({
                "symbol": symbol,
                "shares": shares,
                "price": current_price,
                "total": total_value
            })

            total_stocks_value += total_value

    grand_total = cash + total_stocks_value

    return render_template("index.html",
                         portfolio=portfolio,
                         cash=cash,
                         grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares_str = request.form.get("shares")

        # Validar símbolo
        if not symbol:
            return apology("must provide symbol", 400)

        # Validar quantidade de ações
        try:
            shares = int(shares_str)
            if shares <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return apology("shares must be a positive integer", 400)

        # Buscar cotação atual
        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol", 400)

        # Calcular custo total
        total_cost = stock["price"] * shares

        # Buscar saldo do usuário
        user = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        user_cash = user[0]["cash"]

        # Verificar se tem saldo suficiente
        if total_cost > user_cash:
            return apology("can't afford", 400)

        # Atualizar saldo do usuário
        new_cash = user_cash - total_cost
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, session["user_id"])

        # Registrar transação
        db.execute("""
            INSERT INTO transactions (user_id, symbol, shares, price, transaction_type)
            VALUES (?, ?, ?, ?, ?)
        """, session["user_id"], stock["symbol"], shares, stock["price"], "buy")

        flash(f"Bought {shares} shares of {stock['symbol']} for ${total_cost:,.2f}")
        return redirect("/")

    # GET request
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions."""

    transactions = db.execute("""
        SELECT
            symbol,
            shares,
            price,
            transaction_type,
            timestamp
        FROM transactions
        WHERE user_id = ?
        ORDER BY timestamp DESC
    """, session["user_id"])

    return render_template("history.html", transactions=transactions)


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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

    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("must provide symbol", 400)

        # Buscar cotação
        stock = lookup(symbol)

        if not stock:
            return apology("invalid symbol", 400)

        # Mostrar resultado
        return render_template("quoted.html", stock=stock)

    # GET request - mostrar formulário
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Usuário já está logado?
    if session.get("user_id"):
        return redirect("/")

    # Usuário submeteu formulário
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validar username
        if not username:
            return apology("must provide username", 400)

        # Validar senha
        if not password:
            return apology("must provide password", 400)

        if not confirmation:
            return apology("must confirm password", 400)

        if password != confirmation:
            return apology("passwords do not match", 400)

        # Verificar se username já existe
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if existing_user:
            return apology("username already exists", 400)

        # Gerar hash da senha
        hashed_password = generate_password_hash(password)

        # Inserir no banco de dados
        result = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                          username, hashed_password)

        if result:
            # Buscar o usuário recém-criado
            rows = db.execute("SELECT id FROM users WHERE username = ?", username)

            if rows:
                # Logar automaticamente
                session["user_id"] = rows[0]["id"]

                # Redirecionar para página inicial
                return redirect("/")

        return apology("registration failed", 400)

    # GET request - mostrar formulário
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""

    # Buscar ações que o usuário possui
    user_stocks = db.execute("""
        SELECT
            symbol,
            SUM(CASE WHEN transaction_type = 'buy' THEN shares ELSE -shares END) as total_shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_shares > 0
    """, session["user_id"])

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares_str = request.form.get("shares")

        if not symbol:
            return apology("must select a stock", 400)

        # Validar quantidade
        try:
            shares = int(shares_str)
            if shares <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return apology("shares must be a positive integer", 400)

        # Verificar se possui ações suficientes
        user_stock = None
        for stock in user_stocks:
            if stock["symbol"] == symbol:
                user_stock = stock
                break

        if not user_stock:
            return apology("you don't own that stock", 400)

        if shares > user_stock["total_shares"]:
            return apology("not enough shares", 400)

        # Buscar preço atual
        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol", 400)

        total_revenue = stock["price"] * shares

        # Atualizar saldo do usuário
        user = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        new_cash = user[0]["cash"] + total_revenue
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, session["user_id"])

        # Registrar venda
        db.execute("""
            INSERT INTO transactions (user_id, symbol, shares, price, transaction_type)
            VALUES (?, ?, ?, ?, ?)
        """, session["user_id"], symbol, shares, stock["price"], "sell")

        flash(f"Sold {shares} shares of {symbol} for ${total_revenue:,.2f}")
        return redirect("/")

    # GET request
    else:
        return render_template("sell.html", stocks=user_stocks)


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Add cash to account."""

    if request.method == "POST":
        amount_str = request.form.get("amount")

        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return apology("must provide a positive amount", 400)

        # Atualizar saldo
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?",
                  amount, session["user_id"])

        flash(f"Successfully added ${amount:,.2f} to your account!")
        return redirect("/")

    else:
        return render_template("add_cash.html")


if __name__ == "__main__":
    app.run(debug=True)

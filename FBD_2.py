from flask import Flask,  render_template, url_for, request, flash, session, redirect, abort


app = Flask(__name__)
app.config['SECRET_KEY'] = 'flgkigm530lcgg003njlgf'

menu = [{"name": "Link 1", "url": "install-flask"},
        {"name": "Link 2", "url": "first-app"},
        {"name": "Contact", "url": "contact"}]

@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html',title="Heading", menu = menu)

@app.route("/contact", methods=["POST", "GET"] )
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 3:
            flash('Messages sent', category='success')
        else:
            flash('Please enter correct data', category='error')

    print(request.form)
    return render_template('contact.html', title="Contact", menu=menu)

@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"User: {username}"

@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.form['username'] == "selfedu" and request.form['psw'] == "1111":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Authorization", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)

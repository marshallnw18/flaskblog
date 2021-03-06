from flask import render_template, url_for, flash, redirect 
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app

posts = [
    {
        'author': 'Nick Marshall',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 13, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 13, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    """
    instead of passing straight HTML into the return statement, we can use the render_template() function to
    return the home page's html template that was created in ./templates/home.html
    """
    return render_template('home.html', posts=posts) 

@app.route("/about")
def about(): 
    return render_template('about.html', title='About This Blog')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title="Login", form=form)
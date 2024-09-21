from flask import Flask, render_template


app = Flask(__name__,template_folder="templates")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return "This is the about page"

@app.route('/user/<user_name>')
def show_user_profile(user_name):
    return user_name

app.run(port=5000)

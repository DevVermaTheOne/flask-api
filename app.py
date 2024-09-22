from flask import Flask, render_template
from flask_restful import Resource, Api

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

#api
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'data':'Hello, World!'}

class Helloname(Resource):
    def get(self, name):
        return {'data': 'Hello, {}'.format(name)}
        
api.add_resource(HelloWorld, '/helloworld') # get localhost:5000/helloworld --> Hello World
api.add_resource(Helloname, '/helloworld/<string:name>') # get localhost:5000/helloworld/Person --> Hello Person


if __name__=='__main__':
    app.run(debug=True)

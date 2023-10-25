from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, PetFax!"
    
    @app.route('/pets')
    def index():
        return "These are all the pets we have available!"
    return app
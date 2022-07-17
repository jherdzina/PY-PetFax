from flask import Flask
from . import pet
from . import show
from . import facts

# factory
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    # register pet blueprint 
    
    app.register_blueprint(pet.bp)
    app.register_blueprint(show.bp)
    app.register_blueprint(facts.bp)

    # return the app 
    return app

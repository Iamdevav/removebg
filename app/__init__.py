from flask import Flask
 
def create_app():
    app = Flask(__name__)
    
    # Import and register blueprints here (if you have any)
    from . import routes
    app.register_blueprint(routes.bp)
 
    return app
# serve.py

from flask import Flask
from flask import render_template
from flask import request
from src.core import money


def create_app():
    # creates a Flask application, named app
    app = Flask(__name__)

    # a route where we will display a welcome message via an HTML template
    @app.route("/", methods=['GET'])
    def index():
        result = ""
        try:
            value_to_format = request.args.get('money')
            result = money.format_money(value_to_format)
            if result != '':
                return render_template('index.html', error =None, result=result)
            else:
                return render_template('index.html', error =None, result="{wrong value}")
        except:
            return render_template('index.html', error="Unable to process request", result="")

    return app
    

# run the application
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
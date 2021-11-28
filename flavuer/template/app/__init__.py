import os
from flask import Flask
from flask import render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(  # noqa: S106
        SECRET_KEY="dev",
    )
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Demo
    @app.route("/")
    def main_route():
        return render_template("demo.html")

    return app

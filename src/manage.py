"""Used to run the development server"""
from flask.cli import FlaskGroup

from api import APP

CLI = FlaskGroup(APP)

if __name__ == "__main__":
    CLI()

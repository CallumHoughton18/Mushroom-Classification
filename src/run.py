"""Used to run the development server"""
from api import APP

if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=8080, debug=True)

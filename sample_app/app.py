from flask import Flask
# comment 2

def create_app():

    app = Flask(__name__)

    @app.route('/predictions', methods = ['GET'])
    def getPrediction():
        return 'Pinging Model Application!!'

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0')
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes.routes import api
import os

load_dotenv()


app=Flask(__name__)
CORS(app)

app.register_blueprint(api, url_prefix='/api/products/')



if __name__=="__main__":
    port =int(os.getenv("PORT"))
    app.run(host="0.0.0.0",port=port,debug=True)
from flask import Flask,render_template,request,redirect,url_for
import json
from datetime import datetime

app = Flask(__name__, 
            static_folder='static',     # Explicitly set static folder
            static_url_path='/static')  # Ensure correct static URL path

@app.route('/')
def index():
    return render_template("index.html")
if __name__ == '__main__':
    
    app.run(debug=True)
    

    
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy  
from datetime import datetime
from werkzeug.utils import secure_filename
import numpy as np

app = Flask(__name__)

# ランダムにファイル名を得るメソッド
def picked_up():
    file_names = [
        "images/sample_00001.png",
        "images/sample_00002.png",
        "images/sample_00003.png",
        "images/sample_00004.png",
        "images/sample_00005.png",
        "images/sample_00006.png",
        "images/sample_00007.png",
        "images/sample_00008.png",
        "images/sample_00009.png",
        "images/sample_00010.png",
        "images/sample_00011.png"
    ]
    # NumPy の random.choice で配列からランダムに取り出し
    return np.random.choice(file_names)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', sample_name=picked_up())

if __name__ == '__main__':
    app.run(debug=True)
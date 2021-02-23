from flask import Flask
from flask import jsonify

import easyocr
reader = easyocr.Reader(['ch_sim','en']) 

app = Flask(__name__)

@app.route("/<path>")
def hello(path):
    global reader
    result = reader.readtext(path)
    #return jsonify(result)
    return str(result)

app.run()

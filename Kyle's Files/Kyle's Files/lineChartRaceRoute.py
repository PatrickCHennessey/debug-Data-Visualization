# Bring in Dependencies
import pandas as pd, numpy as np, datetime as dt
import pymongo
import json
import flask
from flask_cors import CORS, cross_origin
from workdata import manipulate_data



app = flask.Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"
cors = CORS(app)
#DB Setup
conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)
db = client.SongInformation

# Route
@app.route("/")
def index():
    return("Success!")



# Graph Route
@app.route("/chart/api/")
@cross_origin()
def get_data():
    year = flask.request.args["year"]
    mongoTable = db.hottie
    results = mongoTable.find({}, {"_id": 0})
    resultdf = pd.DataFrame(list(results))
    pivotJSON = manipulate_data(resultdf, year=year)
    #pivotJSON = json.dumps(pivotJSON, ensure_ascii=True)
    return pivotJSON

@app.route("/line_chart_race/")
@cross_origin()
def draw_graph():
    year = flask.request.args["year"]
    #pivotJSON = json.dumps(pivotJSON, ensure_ascii=True)
    return flask.render_template("jsontest.html", pyyear=year)

if __name__ == "__main__":
    app.run()

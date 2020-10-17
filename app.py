from flask import Flask, render_template, request, redirect, url_for
# from flask_cors import CORS, cross_origin
from workdata import manipulate_data
import pymongo
import json
import pandas as pd, numpy as np, datetime as dt

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def index():
    """Main/default path that serves index.html from the templates folder"""

    return render_template('index.html')

@app.route("/create_db")
def create_db():
    with open("genre_year_df.json","r") as fp:
        json_data = json.load(fp)

    print(json_data)  # to test if json_data prints into terminal
    return(json_data) # prints genre_year_df.json/json_data to Chrome live server

   
@app.route("/api/<year>")
def api(year):

    print("API Call received")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["GT_Data_Visualization"]
    mycol = mydb['GT_Data_Visualization_cn']
    
    # Default year
    if year == None:
        year = 1999

    # 10/16/2020 Issue - Something off here with 2000, 2012,2016,2017 information isn't displaying 
    # likely due to "Nan" values in Peak_position columns. Dropped "Nan" values within jupyter notebook
    # however values are still being omitted when clicking the above years
    #find_mongoDB = list(mycol.GT_Data_Visualization_cn.find())
    find_mongoDB = list(mycol.find({"Year":int(year)},{'Year':0,'_id':0,'Peak Position':0}))
     
    return json.dumps(find_mongoDB)

# Graph Route
@app.route("/chart/api/")
# @cross_origin()
def get_data():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["SongInformation"]
    year = request.args["year"]
    mongoTable = mydb.hottie
    results = mongoTable.find({}, {"_id": 0})
    resultdf = pd.DataFrame(list(results))
    pivotJSON = manipulate_data(resultdf, year=year)
    #pivotJSON = json.dumps(pivotJSON, ensure_ascii=True)
    return pivotJSON

@app.route("/line_chart_race/")
# @cross_origin()
def draw_graph():
    year = request.args["year"]
    #pivotJSON = json.dumps(pivotJSON, ensure_ascii=True)
    return render_template("jsontest.html", pyyear=year)


if __name__ == "__main__":
    app.run(debug=True)
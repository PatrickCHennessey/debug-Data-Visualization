import pandas as pd, numpy as np, datetime as dt
import json
import pymongo

#DB Setup
# conn = 'mongodb://localhost:27017'

# client = pymongo.MongoClient(conn)
# db = client.SongInformation
# table = db.hottie
# results = table.find({}, {"_id": 0})
# results = list(results)
# dataframe = pd.DataFrame(results)

def manipulate_data(df, year):
    year =  str(year)
    df.Week = pd.to_datetime(df.Week)
    df = df[df.Indicator == 1]
    df = df[df["Year"] == year]
    df["Master_Genre"] = df["Master_Genre"].astype("str")
    df["Namey"] = df["nname"] + df["Master_Genre"]
    df = df.loc[:, ["Week", "Week_Number", "nname", "Weekly_rank", "Namey"]]
    data_table = df.pivot_table(index="Namey", columns="Week_Number", values="Weekly_rank").T
    data_table = data_table.fillna(value=22)
    data_table = data_table.reset_index()
    data_table.Week_Number = data_table.Week_Number.astype(np.int32)
    response = data_table.to_json(orient="index")
    return response


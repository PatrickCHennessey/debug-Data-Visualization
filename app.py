from flask import Flask, render_template, request, redirect, url_for
import pymongo
import json

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def index():
    """Main/default path that serves index.html from the templates folder"""

    return render_template('index.html')

    '''
    XXXXX SAMPLE CODE FROM PAST PROJECT XXXXXX
    # Connect to MongoDB connection/collection
    # myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    # Connects to MONGO mydb = myclient["create_db"] 
    # Connects to a specific database in MONGO
    # mycol = db["mars_dictionary"]

    # Accesses a specific collection/table within the database in MONGO

    print("Records in collection: ", mycol.count_documents({}))

    # Retrieve the dictionary record
    results_dict = mycol.find_one() # retrieve everything in the collection

    # Have Flask serve the index.html template file, passing data from the dictionary to the file;
    return render_template('index.html', results=results_dict)
    '''


@app.route("/create_db")
def create_db():

    # load the source data (genre_year.json)

    # CHANGE TO CSV SOURCE XXXXXXXX
    with open("genre_year_df.json","r") as fp:
        json_data = json.load(fp)

    print(json_data)  # to test if json_data prints into terminal
    return(json_data) # prints genre_year_df.json/json_data to Chrome live server

    # parse it (genre_year.json) so that I grab only the year from the data
    
    # store in MongoDB (genre_year.json)

    # What will be the structure of the table/collection in MongoDB (for each record)
 
    # Suggestion: Use the headings from the source csv

    # Headings from genre_year_df.csv: Year,top_genre,Peak Position,Danceability,Duration,Energy,Liveness,Loudness,Mode,Popularity,Tempo,Valence 


    #return "<p>Create DB route/process completed</p>"



@app.route("/api/<year>")
def api(year):

    print("API Call received")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["GT_Data_Visualization"]
    mycol = mydb['GT_Data_Visualization_cn']
    
    # receive a search query from the website (js-fetch)

    # search Mongo DB for all records matching the year
    # year = request.args.get('year')

    # Default year
    if year == None:
        year = 1999


    # 10/16/2020 Issue - Something off here with 2000, 2012,2016,2017 information isn't displaying 
    # likely due to "Nan" values in Peak_position columns. Dropped "Nan" values within jupyter notebook
    # however values are still being omitted when clicking the above years
    #find_mongoDB = list(mycol.GT_Data_Visualization_cn.find())
    find_mongoDB = list(mycol.find({"Year":int(year)},{'Year':0,'_id':0,'Peak Position':0}))
    #print(find_mongoDB)
    #print(year)
    
    #new_var = []
    '''
    for entry in find_mongoDB:
        if dict(entry)["Year"] == int(year):
            x = dict(entry)
            del x['_id']
            new_var.append(x)
    '''    
    #print(new_var)
    return json.dumps(find_mongoDB)
    #return 

    # return matching records to js-fetch for processing by the JS on the web site
    #"Records in collection: ", mycol.GT_Data_Visualization_cn
    
    
    #TypeError: 'Collection' object is not callable. If you meant to call the 
    # 'GT_Data_Visualization_cn' method on a 'Database' object it is failing 
    # because no such method exists. The view function did not return a valid response.
    #  The return type must be a string, dict, tuple, Response instance, or WSGI callable,
    #  but it was a Collection.
'''
@app.route("/scrape")
def scrape_route():

    print("Starting the scrape process")
    from scrape_mars import scrape
    my_dict = scrape()
    
    # Get python to connect to existing mongoDB
    # store my_dict in MongoDB

    print("Scrape process complete.")
    print(my_dict)
    print("Storing dictionary in MongoDB.")
    # Create MongoDB connection/collection
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mars_db"]  
    mycol = mydb["mars_dictionary"]
    # clear any old data from the collection
    mycol.delete_many({})
    # insert scraped dictionary
    x = mycol.insert_one(my_dict)
    the_id = x.inserted_id # get id of inserted record (optional)

    print("Created record ID: ", the_id)

    #return "<h1>Process Complete</h1>"
    
    return redirect(url_for('index'))

From UFO HW used to filter information printed to terminal after 
selecting date on live server index.html page

//Create an event listener
document.getElementById("filter-btn").addEventListener("click", function() {
    //console.log("click button test");
    // get value of the date input field
    let filter_date = document.getElementById("datetime").value;
    console.log(filter_date);
    // call the showTable function with the date as a filter parameter
    showTable(filter_date);
});

Filtered data from UFO will be structured within RadarSourceCode.html to
be added eventually into index.html
'''

if __name__ == "__main__":
    app.run(debug=True)
# Dependencies and Setup
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import scrape

# Flask Setup
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars_df = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_df)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
# # Mission to Mars

# Dependencies and Setup
#import dependencies
import pandas as pd
import os
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import lxml


def init_browser():
    
    # Get the driver and set the executable path
   executable_path = {'executable_path': 'C:/Users/wabug/Desktop/Drivers/chromedriver_win32/chromedriver.exe'}
   browser = Browser('chrome', **executable_path, headless=False)

    #web page url to be scrapped from
def scrape():
    browser=init_browser()


    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
        #beautiful soup 
    html=Browser.html
    soup=BeautifulSoup(html,'html.parser')

    # find news headings 

    heading_list = []

    for heading in soup.find_all('div',class_="content_title"):
        heading_list.append(heading.find('a').text)

    # find information about new articles 

    details_list = []

    for details in soup.find_all('div',class_="article_teaser_body"):
        
        details_list.append(details.text)


    # Varibles for Latest New Articles and Titles

    news_title = heading_list[0]

    news_p = details_list[0]

    news_dict = {"Headline": news_title,"Details": news_p}

    return news_dict 


 # JPL Mars Space Images - Featured Image
    # ***************************************************************************

def Feature_Image_function():
    
    browser = init_browser()

    url_Mars_Space_Images = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(url_Mars_Space_Images)
    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html,'html.parser')


    # find the newest image for this site https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

    featured_image_list = []

    for image in soup.find_all('div',class_="img"):
        featured_image_list.append(image.find('img').get('src'))


    #feature image
    feature_Image = featured_image_list[0]

    #feature image url 
    feature_Image_url = "https://www.jpl.nasa.gov/" + feature_Image

    feature_Image_dict = {"image": feature_Image_url}

    return feature_Image_dict


    # Mars Weather
    # ***************************************************************************

def Weather_function():
    
    browser = init_browser()

    # Set Up for Mars Weather

    url_Mars_Weather = "https://twitter.com/marswxreport?lang=en"

    browser.visit(url_Mars_Weather)
    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html,'html.parser')

    # Locate Mars Weather
    weather_info_list = []

    for weather_info in soup.find_all('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
        weather_info_list.append(weather_info.text)

    # Variable for latest Mars Information
    Latest_Mars_Weather = weather_info_list[0]

    mars_weather_dict = {"mars_weather": Latest_Mars_Weather }

    return mars_weather_dict


# Mars Facts
# ***************************************************************************

def Mars_Facts_table_function():
    
    browser = init_browser()

    df_Mars_Facts = pd.read_html("https://space-facts.com/mars/")

    df_Mars_Facts = df_Mars_Facts[0]

    df_Mars_Facts.rename_axis({0:"Parameters", 1:"Values"},axis=1, inplace=True)

    df_Mars_Facts_table = df_Mars_Facts.to_html("Mars_Facts_Table.html")



    df_Mars_Facts_dict = {"df_Mars_Facts": df_Mars_Facts_table}



    return df_Mars_Facts_dict

# Mars hemisphere
# ***************************************************************************

def hemisphere_images():
    image_one = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    image_two = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    image_three = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    image_four = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

    full_hemisphere_dict = {"image_one": image_one, "image_two":image_two, "image_three":image_three, "image_four":image_four}

    return full_hemisphere_dict

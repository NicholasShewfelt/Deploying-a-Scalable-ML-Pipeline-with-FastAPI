# Project Summary
This project was my capstone project for the Udacity Data Analytics Nanodegree. 
The premise of the project was to give me code that was partially completed and then have me complete it. 
The project in its entirety consists of an entire machine learning pipeline for the cencus.csv dataset, which takes the data and trains a RandomForest machine learning algorithm on the dataset and then computes whether an individual makes greater than or less than $50,000 a year based on the data that was recorded about the individual.



# Contributions 
Namely, I had to:
* Design the FastAPI backend.
* Write functions for the machine learning pipeline (such as running the model on a catagorical slice of the dataset).
* Write code to train the model on the dataset using the functions I made.
* Add necessary code to the main.py file to get the pipeline to function properly.



# Elements of the project

# Data
* The census.csv file was given to me as the dataset for the project. It consists of rows of data in which each row represents an individual and has many trait columns that contain information about the individual, such as their age, mariage status, sex, and many more traits such as these. At the last column in each row is a true or false column showing whether or not the individual makes greater than r less than 50K.


# Parts of the Project
The project consists of two parts:
* Model which consists of the necessary components to create and train a machine learning model, such as the train_model.py file and the 
 data.pyfile, all of which house functions for when the main.py file is run.
* RESTful API which was created using FastAPI and most notably has a Get on the root, giving a welcome message, and a POST that does model inference.

# Anomaly_Detection_OSDS_meetup
**This repository outlines a framework for building an anomaly detection algorithm and deploying into a web app**
* The web app setup was inspired by Sebastian Raschka and Vahid Mirjalili Python Machine Learning Second Edition book
* The meat of all this work is in the web app folder
* The image folder contains an image that I use in the notebook and the environment.yml file lists my python environment so anyone can replicate this method
* The Dataset: engine.csv. This dataset contains car engine data collected through OBDII and spanning multiple trips
  - Validation_data.csv is the validation data set that can be used with the web app
  - test_data.csv mimics new data streams from the engine to run the algorithm against and detect engine issues
* The jupyternotebook, 01_Regressor_Classify, walks through building the regressor to classifier algorithm that will be used to detect anomalies
  - I didn't spend much time optimizing this regressor model and therefore it does not generalize very well. The goal of this repo was to focus on the anomaly detection framework for sensor data
* custom.py file is where we create the new scikit-learn compatible class that will run the regressor model and return residuals to be passed to a oneClass classifier
* Flask_app.py this will contain our main code needed to run the flask web app
* pkl_objects folder will contain the scikit-learn serialized models(The regressor and the full pipeline containing the regressor and classifier)
  - I had to zip the random forest pickle file to keep it below github size restriction. You will need to unzip this locally to make it work
* The templates folder contains the HTML template files for the web app
* to run this web app locally:
  - From the applications main directory using python command line type ***python3 Flask_app.py***.
  - From jupyternotebook type ***!python3 Flask_app.py***
  - Go to your web browser and type ***http://127.0.0.1:5000/***
  
  ## Happy learning

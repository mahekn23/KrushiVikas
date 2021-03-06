# KrushiVikas: A multiservice web-app for Indian Farmers. 

![alt text](https://github.com/mahekn23/KrushiVikas/blob/master/KrushiVikas/authkv/static/images/logokrushi.PNG?raw=true)


## PURPOSE:

Agriculture and its allied sectors are a major contribution to the Indian economy. In this day and age where everything functions digitally on devices, these areas of occupation need to keep up too. One of our goals was to make our Indian farmers more aware of the variety of E farming features that can be of great use to them. Ours is a small initiative, but is not restricted to a certain level. There seems to be a lot of scope in the future of E farming and also in the scope of our system.

## ABOUT THE APPLICATION:

A Django and ML based web application with a whole lot of features to help the E - Agro industry.

## FEATURES:

- Crop Prediction - Random Forest Classifier : 99% accuracy
- Plant Disease Detection - Sequential Model : 95% accuracy
- Renting Tools - Django Models
- Know the climate - REST API
- NEWs - REST API
- Expert assistance - contact details and feedback

## DEMO:

Video Link: https://drive.google.com/file/d/1zTPR7gRc6Up6kOk8NvxKBmq1yvsWnJ3h/view?usp=sharing

## CONTRIBUTERS:

- Mahek Nagdev: https://www.linkedin.com/in/mahek-nagdev-382a7b1b8/
- Sejal Budhani: https://www.linkedin.com/in/sejal-budhani-6841b5204/
- Roshni Kataria: https://www.linkedin.com/in/roshni-kataria/
- Jayesh Dhanrajani: https://www.linkedin.com/in/jayesh-dhanrajani-34612916b/

## TECHNOLOGY USED:

Machine Learning,
Image Processing,
Django, REST APIs,
HTML, CSS, JS,
Tensorflow.

## TOOLS:

VS Code,
Canva,
Draw.io.

## DATASETS:

- Crop Prediction: .csv file is included in the corresponding feature folder.
- Plant disease detection : https://www.kaggle.com/datasets/emmarex/plantdisease

## REQUIREMENTS TO RUN THE WEB APP:

(Below stated versions were used to build this application)
- Python V3.8.7
- Django V3.2.4
- Tensorflow V2.7.0

## USAGE:

- To run this web app, kindly download the zip file KrushiVikas and Unzip the folder in your system or clone the repository. Also download the .h5 file and place it in plant_disease_detection app folder; H5 file: https://drive.google.com/file/d/1ou3tFfgG4QOagcayMFTbaydE3uYoav_0/view?usp=sharing
- Go to KrushiVikas/KrushiVikas and open settings.py file. On line 141 and 142 make the required changes i.e. add your email id and password of that email account.
- Open command prompt and navigate to the KrushiVikas folder that includes the file manage.py and all the apps.
- On that path, run the following commands - 
  1. python manage.py makemigrations
  2. python manage.py migrate
  3. python manage.py runserver.

## FUTURE SCOPE:

Future directions include - 
(1) working on larger datasets for crop prediction, 
(2) adding more leaf diseases and increasing the accuracy of the model, 
(3) adding an online payment methods for renting tools, 
(4) providing only the details of tools made available by farmers of the same region as the user, 
(5) providing a weather forecast for a week or more.

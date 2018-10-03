# BuildUp

> BuildUpin nutshell is an android application that will you find if the medicine is availaible within a cetain maximun distance of your location and if it is tells you the pharmacy 

## Working

#### There are two parts of the project

* **Android Application**

The Android Application will serve as the user interface asking the user for the requested medicine name, quantity as well as the latitude and longitude of your place. The information is thus transmitted to the server side. To aid in the network calls the Volley networking library is used

* **Server**

The server side is basically REST-API implemented in flask . Flask is responsible for handling the data coming at endpoints and here the flask handles the data send by the android application. The flask application can be hosted permenantly or temporarily as per the requirments. The *ngrok* here is the good choice if you want to host the application on the server for a short period of time.
Here The Flask Application checks if the medicine is available in the pharmacy within a max distance and if multiple entries are found returns the list of pharmacy. The Flask Application in the repository is of the name *name.py*


# BuildUp

> BuildUp in nutshell is an android application that will you find if the medicine is availaible within a cetain maximun distance of your location and if it is tells you the pharmacy 

## Working

#### There are two parts of the project

* **Android Application (This Repo)**

The Android Application will serve as the user interface asking the user for the requested medicine name, quantity as well as the latitude and longitude of your place. The information is thus transmitted to the server side. To aid in the network calls the Volley networking library is used.

* **Server**

Here The Flask Application takes a request from the application checks if the medicine is available in the pharmacy within a max distance by searching through the datebase and if multiple entries are found it finds the best suitable discounts and price and orders the medicine to be delievered automatically. The functionality would be extended by retrieving a pic of transcript from the android, processing and gathering text and doing the neccesary step involved in ordering and delievering the medicine. The Flask Application in the repository is of the name *name.py*
inding the best suitable discounts and price. 

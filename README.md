
# Anomaly Machine Status Predictor

## Overview of Project

Using K-Means Algorithm create a clustering model from the training dataset. Using this model to predict anomalies that can potentially cause a failure of either the system overheating or the disc failing. Providing REST API to add machine status information and retrieve all anomaly machine status.
The project demos how to use Python machine learning library SciPy to create a clustering model by K-Means Algorithm. The Project also shows how to implement RESTful HTTP API using Flask, Flask-Restful.
User can use REST API to add machine status to server side and keep all machine status information at in-memory data structure. The in-memory data structure is a Python List. Each list item is a dictionary. There are five properties. Machine name, temperature, disk read errors, anomaly status and timestamp. So if stop/kill the python application, all information will be lost. User can use another REST API to retrieve all potential anomaly machine status from list. The potential anomaly machine status is predicted by clustering model. 

## REST API Specification

Service Name: machine-status-logs
URL: http://127.0.0.1:8080/machine-status-logs
Resource: machine-status-logs

### Retrieve all potential anomaly machine status
Title	Show all potential anomaly machine status logs  
URL	/machine-status-logs?anomaly=true&format=json
Method	GET
URL Params	Optional: 
anomaly=[string] 
default value: true
example: anomaly = true 

format=[string] 
default value: json
example: format = json 
Data Params	None
Success Response	Code: 200 
Content: 
{ 
    status : “success”,
    “data”:[
             {
                     Machine_name: test-machine,
                     Cpu_temperature: 80,
                     Disc_read_errors: 40000,
                     timestamp: 1497636462.1364536,
                     anomaly:true
              },
              {
                     machine_name: test-machine,
                     cpu_temperature: 100,
                     disc_read_errors: 5000,
                     timestamp:06/15/2017:18:00:00
                    anomaly: true
              }
    ] 
}
Error Response	Code: 400 General Error
Content: 
    { “status” : “error”,
       “message” : "Error has occurred when call machine status log API" 
     }
Sample Call	$.ajax({
  url: "/machine-status-logs",
  dataType: "json",
  data : { 
anomaly : true,
format : json
  },
  type : "GET",
  success : function(r) {
    console.log(r);
  }
});

### Add machine status to server side 

Title	Add a new machine status log  
URL	/machine-status-logs?machine-name=:machine-name&cpu-temperature=: cpu-temperature&disk-read-errors=:disk-read-errors
Method	POST 
URL Params	None  
Data Params	{
  machine-name : [string]
  cpu-temperature  : [float],
  disk-read-errors : [integer]
}

Example:
{
  machine-name : test-machine,
  cpu-temperature  : 56.1,
  disk-read-errors : 10
}

Success Response	Code: 200 
Content: 
{ 
    status : “success”,
    “data”:{
       machine_name : test-machine,
       Cpu_temperature  : 56.1,
       Disk_read_errors : 10,
       anomaly : false,
       timestamp: 1497638221.0870788  
    } 
}
Error Response	Code: 400 General Error 
Content: 
{ “status” : “error”,
    “message” : "Error has occurred when call machine status log API" 
 }
Sample Call	$.ajax({
  url: "/machine-status-logs",
  dataType: "json",
  data : { 
       machine-name : test-machine,
       cpu-temperature  : 56.1,
       disk-read-errors : 10
  },
  type : "POST",
  success : function(r) {
    console.log(r);
  }
});

## Project File Lists

READ.md	This is a readme file that describe how to setup environment and test REST API though Postman client application.

requirements.txt	This file lists all of the Python packages that app depends on

machineStatusLog.py	This is server application python source code

Setup.bat	Windows batch file which will run pip to install all requirements python package

compdata.txt	Training data file

numpy-1.13.0+mkl-cp36-cp36m-win_amd64.whl	Python numpy package for windows OS. Due to the file size exceeds Github's file size limit of 100.00 MB. Please download from the following link

         http://www.silx.org/pub/wheelhouse/

         search file name "numpy-1.13.0+mkl-cp36-cp36m-win_amd64.whl"

scipy-0.19.0-cp36-cp36m-win_amd64	Python scipy package for windows OS

## Installing

### Download Software

#### Python
Download Python from https://www.python.org/downloads/windows/.
File name: python-3.6.1-amd64.exe 
Version : 3.6.1
OS: windows 10 64bit

#### Extra Python package
•	numpy, Version 1.13.0+mkl
•	SciPy Package, Version 0.19.0
•	Flask, Version 0.12.2. More detail information for install Flask. Please read the below link http://flask.pocoo.org/docs/0.12/installation/
•	Flask-RESTful, Version 0.3.6. More detail information for install Flask-RESTful. Please read the below link http://flask-restful.readthedocs.io/en/0.3.5/installation.html
•	Pandas, Version 0.20.2

#### Postman
Download Postman from https://chrome.google.com/webstore/search/postman?hl=en for Chrome

#### MachineStatusLog Application Package
Download application files from GitHub. GitHub Link is https://github.com/QianWangDallas/msp

### install application on local machine
running environment is windows 10 64bit.

Step 1. install Python. Read the below link for installation instruction under windows 10.
https://www.howtogeek.com/197947/how-to-install-python-on-windows/

Step 2. run Command Prompt with administration right and run setup.bat. The batch will install all requirements Python package.

Step 3. Under Command prompt and run “python machineStatusLog.py” to start application

Step 4. Launch testing client Application (Postman)
•	Lunch Chrome and click show Apps icon at left upper corner.
•	Click Postman icon to launch Postman.

Step 5. Test REST API
Help REST API.
URL : 127.0.0.1:8080/
Result: 
Using a Machine Learning Library Scipy and Python create a clustering model. 
Using this model to predict anomalies that can potentially cause a failure 
of either the system overheating or the disc failing. 
There are two REST APIs. Add machine status API and retrieve all anomaly 
machine status API.
Add machine status API.
	URL : /machine-status-logs?
	Method : POST.
	Need machine-name,cpu-temperature and disk-read-errors as post parameters

Retrieve all anomaly machine status API
	URL : /machine-status-logs?anomaly=true&format=json
	Method : GET. 
	Need two parameters. anomaly and format
Add machine status API
URL: 127.0.0.1:8080/machine-status-logs
Method: POST
Params:
	machine-name=test_machine
cpu-temperature=54.1
disk-read-errors=10
Result:
{
    "status": "success",
    "data": {
        "machine_name": "test_machine",
        "cpu_temperature": "54.1",
        "disk_read_errors": "10",
        "timestamp": 1497639379.6910198,
        "anomaly": "false"
    }
}
Retrieve all anomaly machine status API
URL : 127.0.0.1:8080/machine-status-logs
Method: GET
Params:
	anomaly=true
format=json
Result:
{
    "status": "success",
    "data": [
        {
            "machine_name": "test_machine",
            "cpu_temperature": "60",
            "disk_read_errors": "10044",
            "timestamp": 1497636462.1364536,
            "anomaly": "true"
        },
        {
            "machine_name": "test_machine",
            "cpu_temperature": "8",
            "disk_read_errors": "10044",
            "timestamp": 1497636484.1511443,
            "anomaly": "true"
        },
        {
            "machine_name": "test_machine",
            "cpu_temperature": "8",
            "disk_read_errors": "10044",
            "timestamp": 1497637221.7880988,
            "anomaly": "true"
        },
        {
            "machine_name": "test_machine",
            "cpu_temperature": "8",
            "disk_read_errors": "10044",
            "timestamp": 1497637225.2306342,
            "anomaly": "true"
        }
    ]
}

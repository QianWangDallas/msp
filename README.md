# Anomaly Machine Status Predictor

## Overview of Project

Using K-Means Algorithm create a clustering model from the training dataset. Using this model to predict anomalies that can potentially cause a failure of either the system overheating or the disc failing. Providing REST API to add machine status information and retrieve all anomaly machine status. <br />

The project demos how to use Python machine learning library SciPy to create a clustering model by K-Means Algorithm. The Project also shows how to implement RESTful HTTP API using Flask, Flask-Restful.<br />

User can use REST API to add machine status to server side and keep all machine status information at in-memory data structure. The in-memory data structure is a Python List. Each list item is a dictionary. There are five properties. Machine name, temperature, disk read errors, anomaly status and timestamp. So if stop/kill the python application, all information will be lost. User can use another REST API to retrieve all potential anomaly machine status from list. The potential anomaly machine status is predicted by clustering model. 

## REST API Specification

Service Name: machine-status-logs <br />

URL: http://127.0.0.1:8080/machine-status-logs<br />

Resource: machine-status-logs <br />

### Retrieve all potential anomaly machine status

Title : 	Show all potential anomaly machine status logs  <br />

URL:	/machine-status-logs?anomaly=true&format=json <br />

Method:	GET<br />

URL Params:	<br />

Optional: <br />

anomaly=[string] <br />

default value: true<br />

example: <br />

anomaly = true <br />

format=[string] <br />

default value: json <br />

example:<br />

format = json <br />

Data Params:	None <br />

Success Response: <br />

	Code: 200 <br />

         Content: <br />

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
 <br />
Error Response:<br />

	Code: 400 General Error <br />

         Content: <br />
        { 
             “status” : “error”, <br />
            “message” : "Error has occurred when call machine status log API" <br /> 
        }<br />

Sample Call:<br />
	$.ajax({
        url: "/machine-status-logs",
       dataType: "json",
       data : { 
        ranomaly : true,
        format : json
  } ,
  type : "GET",
  success : function(r) {
   console.log(r);
  }<br />
});
<br />

### Add machine status to server side 

Title	:Add a new machine status log  <br />

URL	:/machine-status-logs?machine-name=:machine-name&cpu-temperature=: cpu-temperature&disk-read-errors=:disk-read-errors <br/>

Method	POST <br />

URL Params:	None <br />  

Data Params:	{<br />
  machine-name : [string] <br />
  cpu-temperature  : [float], <br />
  disk-read-errors : [integer] <br />
}
<br />
Example: <br />
{
  machine-name : test-machine,
  cpu-temperature  : 56.1,
  disk-read-errors : 10
}
<br />
Success Response:<br />
	Code: 200 <br />
        Content: <br />
       { 
    status : “success”,
    “data”:{
       machine_name : test-machine,
       Cpu_temperature  : 56.1,
       Disk_read_errors : 10,
       anomaly : false,
       timestamp: 1497638221.0870788  
    } 
}<br />

Error Response:
	<br />
Code: 400 General Error <br />
Content:  <br />
{ “status” : “error”,
    “message” : "Error has occurred when call machine status log API" 
 }
 <br />
Sample Call:<br />
	$.ajax({
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
<br />
## Project File Lists

READ.md	This is a readme file that describe how to setup environment and test REST API though Postman client application.<br />

requirements.txt	This file lists all of the Python packages that app depends on <br />

machineStatusLog.py	This is server application python source code<br />

Setup.bat	Windows batch file which will run pip to install all requirements python package<br />

compdata.txt	Training data file <br />

numpy-1.13.0+mkl-cp36-cp36m-win_amd64.whl 	Python numpy package for windows OS. Due to the file size exceeds Github's file size limit of 100.00 MB. Please download from the following link <br />

         http://www.silx.org/pub/wheelhouse/ <br />

         search file name "numpy-1.13.0+mkl-cp36-cp36m-win_amd64.whl"<br />

scipy-0.19.0-cp36-cp36m-win_amd64	Python scipy package for windows OS

## Installation

### Download Software

#### Python

Download Python from https://www.python.org/downloads/windows/.<br />

File name: python-3.6.1-amd64.exe <br />

Version : 3.6.1<br />

OS: windows 10 64bit<br />

#### Extra Python package

•	numpy, Version 1.13.0+mkl <br />
•	SciPy Package, Version 0.19.0<br />
•	Flask, Version 0.12.2. More detail information for install Flask. Please read the below link http://flask.pocoo.org/docs/0.12/installation/<br />
•	Flask-RESTful, Version 0.3.6. More detail information for install Flask-RESTful. Please read the below link http://flask-restful.readthedocs.io/en/0.3.5/installation.html<br />
•	Pandas, Version 0.20.2<br />

#### Postman

Download Postman from https://chrome.google.com/webstore/search/postman?hl=en for Chrome<br />

#### MachineStatusLog Application Package

Download application files from GitHub. GitHub Link is https://github.com/QianWangDallas/msp

### Install application on local machine
running environment is windows 10 64bit.<br />

Step 1. install Python. Read the below link for installation instruction under windows 10.
https://www.howtogeek.com/197947/how-to-install-python-on-windows/<br />

Step 2. run Command Prompt with administration right and run setup.bat. The batch will install all requirements Python package.<br />

### Running Application

Step 1. Under Command prompt and run “python machineStatusLog.py” to start application<br />

Step 2. Launch testing client Application (Postman)<br />

•	Lunch Chrome and click show Apps icon at left upper corner.<br />

•	Click Postman icon to launch Postman.<br />
<br />

### Test REST API <br />

#### Help REST API. <br />

    URL : 127.0.0.1:8080/ <br />

    Method: GET <br />

    Result: <br />

    Using a Machine Learning Library Scipy and Python create a clustering model. <br />
 
    Using this model to predict anomalies that can potentially cause a failure <br />

    of either the system overheating or the disc failing. <br />

    There are two REST APIs. Add machine status API and retrieve all anomaly <br />

    machine status API.<br />

    Add machine status API.<br />

    URL : /machine-status-logs? <br />
    
    Method : POST. <br />
    
    Need machine-name,cpu-temperature and disk-read-errors as post parameters<br />

<br />
    Retrieve all anomaly machine status API <br />
	
    URL : /machine-status-logs?anomaly=true&format=json <br />
    
    Method : GET. <br />
    
    Need two parameters. anomaly and format<br />
    
#### Add machine status API<br />


    URL: 127.0.0.1:8080/machine-status-logs<br />

    Method: POST<br />

    Params:<br />

	machine-name=test_machine<br />
    
        cpu-temperature=54.1<br />
        
        disk-read-errors=10<br />

    Result:<br />
    {
        "status": "success",
        "data": {
            "machine_name": "test_machine",
            "cpu_temperature": "54.1",
            "disk_read_errors": "10",
            "timestamp": 1497639379.6910198,
            "anomaly": "false"
        }
}<br />

#### Retrieve all anomaly machine status API <br />

    URL : 127.0.0.1:8080/machine-status-logs <br />

    Method: GET <br />

    Params:<br />
        anomaly=true <br />
        format=json<br />

    Result:<br />
    {
        "status": "success", <br />
        "data": [ <br />
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
    ] <br />
}

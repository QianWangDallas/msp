#load libraries for machine learning
import numpy as np
import pandas
from sklearn.cluster import KMeans

#load libraries for REST API
from flask import Flask,request
from flask_restful import abort,Api,reqparse,Resource
from json import dumps
from time import time

__author__ = "Qian Wang"
__copyright__ = "Copyright 2017, The Machine Status Log Project"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Qian Wang"
__email__ = ""
__status__ = "Developing"


app = Flask(__name__,static_url_path='')
print("Log : Application Name: ",format(__name__))
api = Api(app)


machine_status_logs = [] #define machine status logs

parser = reqparse.RequestParser()
parser.add_argument('machine-name')
parser.add_argument('cpu-temperature')
parser.add_argument('disk-read-errors')
parser.add_argument('anomaly')
parser.add_argument('format')


#define predictor 
class Predictor:
    kmeans = None
    
    def __init__(self, TrainingDataFileName):
        try:
            df=pandas.read_csv(TrainingDataFileName,header=None,sep='\t')
            f1 = df[df.columns[0]].values
            f2 = df[df.columns[1]].values
            X=np.matrix(list(zip(f1,f2)))
            Predictor.kmeans = KMeans(n_clusters=2).fit(X)
            print("Log : Predictor : succeed getting KMeans based on training data ",format(TrainingDataFileName))
        except:
            print("ERROR : Predictor : fail getting KMeans based on training data ",format(TrainingDataFileName))
            raise
      
    def predict_anomaly(self,cpu_temperature,disk_read_errors):
        try:
            f_cpu_temperature = cpu_temperature if(isinstance( cpu_temperature, float )) else float(cpu_temperature)
            i_disk_read_errors = disk_read_errors if(isinstance( disk_read_errors, int )) else int(disk_read_errors)
             
            resultArray = Predictor.kmeans.predict([[f_cpu_temperature,i_disk_read_errors]])
        
            return 'true' if resultArray[0] == 1 else 'false'
        except:
            print("ERROR : Predictor : fail predicting machine anomaly status ")
            raise

#create a predictor with compdata.txt as training data
trainingDataFileName = "compdata.txt"
predictor = Predictor(trainingDataFileName)

   
class MachineStatusLogs(Resource):
    def get(self):
        anomaly = request.args.get('anomaly', "true")
        format = request.args.get('format', "json")
        anomly_logs = [item for item in machine_status_logs if item['anomaly'] == anomaly]
        
        result = {'status' : 'success',
                  'data' : anomly_logs
                 } if len(anomly_logs) > 0 else { 'status' : 'success',
                    'data'  : 'There is no anomaly machine status'}

        print("Log : MachineStatusLogs : succeed getting all anomaly machine status ",anomly_logs)
        
        return result
    
    def post(self):
        args = parser.parse_args()
        machine_status_log = {'machine_name':args['machine-name'],
                              'cpu_temperature':args['cpu-temperature'],
                              'disk_read_errors':args['disk-read-errors'],
                              'timestamp':time(),
                              'anomaly':predictor.predict_anomaly(args['cpu-temperature'],
                                                                  args['disk-read-errors'])}
        machine_status_logs.append(machine_status_log)
        result = {
                    'status' : 'success',
                    'data': machine_status_log
                 }

        print("Log : MachineStatusLogs : succeed appending a machine status ",machine_status_log)
        
        return result
    
@app.route("/")
def help():
    return ("Using a Machine Learning Library Scipy and Python create a clustering model. \n"
           "Using this model to predict anomalies that can potentially cause a failure \nof either the system overheating or the disc failing. \n"
           "There are two REST APIs. Add machine status API and retrieve all anomaly \nmachine status API.\n"
           "Add machine status API.\n"
           "\tURL : /machine-status-logs?\n"
           "\tMethod : POST.\n\tNeed machine-name,cpu-temperature and disk-read-errors as post parameters\n\n"
           "Retrieve all anomaly machine status API\n"
           "\tURL : /machine-status-logs?anomaly=true&format=json\n"
           "\tMethod : GET. \n\tNeed two parameters. anomaly and format\n")
    

api.add_resource(MachineStatusLogs,'/machine-status-logs',
                 methods=['GET','POST'])

if __name__ == "__main__":
    app.run(port='8080')

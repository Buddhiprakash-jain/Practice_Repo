import argparse
import os
import time
import mysql.connector
# pip install google-api-python-client
import googleapiclient.discovery
from six.moves import input
mydb = mysql.connector.connect(
        host="34.142.173.243",
        user="root",
        password="buddhi",
        database="mybpdb"
            )
mycursor = mydb.cursor()
#compute = googleapiclient.discovery.build('compute', 'v1')
def start_vm(request):
    compute = googleapiclient.discovery.build('compute', 'v1')
    name = request.args.get('name')
    zone = request.args.get('zone')
    def list_instances(compute, project, zone):
        result = compute.instances().list(project=project, zone=zone).execute()
        return result['items'] if 'items' in result else None
        # [END list_instances]
    x = list_instances(compute,'basic-tube-373302' ,zone)
    for i in range(len(x)):
	    if (x[i]["name"]) == name:
            	if (x[i]["status"]) == "RUNNING":
                	return "VM %s already in running state.." % name
            	else:
                	result = compute.instances().start(project='basic-tube-373302', zone=zone, instance=name).execute()
			sql = "insert into newtable (instanceName,operation,zone,returnmessage) values (%s,%s,%s,%s)"
			val = (name,"START",zone,"VM %s START" % name)
			mycursor.execute(sql, val)
			mydb.commit()
                	return "VM %s Starting.." % name
    return "Vm %s not found.." % name

        

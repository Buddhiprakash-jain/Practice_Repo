import argparse
import os
import time
import json

# pip install google-api-python-client
import googleapiclient.discovery
from six.moves import input

def details(request):
        l1 = []
        compute = googleapiclient.discovery.build('compute', 'v1')
        zone = request.args.get('zone')    
        def list_instances(compute,project,zone):
                result = compute.instances().list(project=project, zone=zone).execute()
                return result['items'] if 'items' in result else None
        x = list_instances(compute,"basic-tube-373302",zone)
        for i in range(len(x)):
                l1.append(str(i)+","+x[i]["name"]+","+x[i]["status"]+","+x[i]["zone"].split("/")[8])
                jstr = json.dumps(l1)
        return jstr

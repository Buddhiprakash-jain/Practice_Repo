import argparse
import os
import time

# pip install google-api-python-client
import googleapiclient.discovery
from six.moves import input

#compute = googleapiclient.discovery.build('compute', 'v1')
def stop_vm(request):
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
            	if (x[i]["status"]) == "TERMINATED":
                	return "VM %s already in stopping state.." % name
            	else:
                	result = compute.instances().stop(project='basic-tube-373302', zone=zone, instance=name).execute()
                	return "VM %s Stopping.." % name
    return "VM %s not found.." % name
        

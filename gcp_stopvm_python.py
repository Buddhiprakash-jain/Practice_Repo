import argparse
import os
import time

# pip install google-api-python-client
import googleapiclient.discovery
from six.moves import input

#compute = googleapiclient.discovery.build('compute', 'v1')
def stop_vm(request):
    compute = googleapiclient.discovery.build('compute', 'v1')
    def list_instances(compute, project, zone):
        result = compute.instances().list(project=project, zone=zone).execute()
        return result['items'] if 'items' in result else None
        # [END list_instances]

    x = list_instances(compute,'basic-tube-373302' ,'asia-southeast1-b')
    for i in range(len(x)):
	    if (x[i]["name"]) == "pyvm":
            	if (x[i]["status"]) == "TERMINATED":
                	return "VM already in stopping state.."
            	else:
                	result = compute.instances().stop(project='basic-tube-373302', zone='asia-southeast1-b', instance='pyvm').execute()
                	return "VM Stopping.."
    return "Vm not found.."
        

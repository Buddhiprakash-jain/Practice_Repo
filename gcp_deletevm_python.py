import argparse
import os
import time

# pip install google-api-python-client
import googleapiclient.discovery
from six.moves import input

compute = googleapiclient.discovery.build('compute', 'v1')

def delete_instance(compute, project, zone, name):
  result = compute.instances().delete(project=project,zone=zone,instance=name).execute()
  return "VM Deleting.."
delete_instance(compute,'basic-tube-373302' ,'asia-southeast1-b', 'pyvm')

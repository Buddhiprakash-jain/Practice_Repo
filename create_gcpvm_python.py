import argparse
import os
import time

# pip install google-api-python-client
import googleapiclient.discovery
from six.moves import input

compute = googleapiclient.discovery.build('compute', 'v1')

def create_instance(request):
    # Get the latest Debian Jessie image.
    image_response = compute.images().getFromFamily(
        project='rhel-cloud', family='rhel-8').execute()
    source_disk_image = image_response['selfLink']

    # Configure the machine
   # machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
    # startup_script = open(
    #     os.path.join(
    #         os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
    # image_url = "http://storage.googleapis.com/gce-demo-input/photo.jpg"
    # image_caption = "Ready for dessert?"

    config = {
        'name': 'pyvm',
        'machineType': 'zones/asia-southeast1-b/machineTypes/n1-standard-1',

        # Specify the boot disk and the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],

        # Specify a network interface with NAT to access the public
        # internet.
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],

        # Metadata is readable from the instance and allows you to
        # pass configuration from deployment scripts to instances.
        'metadata': {
            # 'items': [{
            #     # Startup script is automatically executed by the
            #     # instance upon startup.
            #     'key': 'startup-script',
            #     'value': startup_script
            # }, {
            #     'key': 'url',
            #     'value': image_url
            # }, {
            #     'key': 'text',
            #     'value': image_caption
            # }, {
            #     'key': 'bucket',
            #     'value': bucket
            # }]
        }
    }
    def list_instances(compute, project, zone):
        result = compute.instances().list(project=project, zone=zone).execute()
        return result['items'] if 'items' in result else None
        # [END list_instances]

    x = list_instances(compute,'basic-tube-373302' ,'asia-southeast1-b')
    for i in range(len(x)):
        if (x[i]["name"]) == "pyvm":
            return "pyvm Already Exists.."
    r = compute.instances().insert(project='basic-tube-373302',zone='asia-southeast1-b',body=config).execute()
    return "VM Creating.."
#create_instance(compute,'basic-tube-373302' ,'asia-southeast1-b', 'pyvm','pybucket')

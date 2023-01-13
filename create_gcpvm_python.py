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
def create_instance(request):
    compute = googleapiclient.discovery.build('compute', 'v1')
    name = request.args.get('name')
    zone = request.args.get('zone')
    machine_type = request.args.get('machine_type')
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
        'name': name,
        'machineType': 'zones/%s/machineTypes/%s' % (zone , machine_type),

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
    x = list_instances(compute,'basic-tube-373302' ,zone)
    for i in range(len(x)):
        if (x[i]["name"]) == name:
            return "VM %s Already Exists.." % name
    r = compute.instances().insert(project='basic-tube-373302',zone=zone,body=config).execute()
    sql = "insert into newtable (instanceName,operation,zone,returnmessage) values (%s,%s,%s,%s)"
    val = (name,"CREATE",zone,"VM %s Create" % name)
    mycursor.execute(sql, val)
    mydb.commit()
    return "VM %s Creating.." % name
#create_instance(compute,'basic-tube-373302' ,'asia-southeast1-b', 'pyvm','pybucket')

import googleapiclient.discovery

def start_vm(request):
    compute = googleapiclient.discovery.build('compute', 'v1')
    result = compute.instances().start(project='basic-tube-373302', zone='asia-southeast1-b', instance='pyvm').execute()
    return "VM Starting.."

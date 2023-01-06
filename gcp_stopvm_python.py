import googleapiclient.discovery

def stop_vm(request):
    compute = googleapiclient.discovery.build('compute', 'v1')
    result = compute.instances().stop(project='basic-tube-373302', zone='asia-southeast1-b', instance='pyvm').execute()
    return "VM Stopping.."

import numpy
import requests

def handler(event, context):

    x = numpy.linspace(0, 10, 5000)
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    print (r)
    return {"message": str(x)}

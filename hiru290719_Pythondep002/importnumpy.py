import numpy

def handler(event, context):
    x = numpy.linspace(0, 10, 5000)
    return {"message": str(x)}

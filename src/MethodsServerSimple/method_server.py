""" An OPC UA server providing a multiply method.
"""

from opcua import ua, uamethod, Server
import time


# configuration parameters of the server
namespace = "http://www.ifak.eu/opcua/test-api"
server_url = "opc.tcp://localhost:4840/freeopcua/server/"  # open for everybody: "0.0.0.0:4840"


# here is the function, which we want to publish over OPC UA
@uamethod
def multiply(parent, x: float, y:float):
    print("multiply method call with parameters: ", x, y)
    return x * y


# instantiation of the server and basic configuration
server = Server()
server.set_endpoint(server_url)
server.set_server_name("FreeOpcUa Method Server")
idx = server.register_namespace(namespace)

# get Objects node, this is where we should put our custom stuff
objects = server.get_objects_node()
my_functions = objects.add_object(idx, "MyFunctions")

# prepare in/out variables for multiply
x, x.Name, x.DataType = ua.Argument(), "x", ua.NodeId(ua.ObjectIds.Int64)
y, y.Name, y.DataType = ua.Argument(), "y", ua.NodeId(ua.ObjectIds.Int64)
result, result.Name, result.DataType = ua.Argument(), "Result", ua.NodeId(ua.ObjectIds.Int64)
my_functions.add_method(idx, "multiply", multiply, [x, y], [result])

try:
    # start the server
    server.start()
    print("Multiply OPC UA server started ...")

    # here follows a trick in order to wait for keyboard interrupt CTRL-C
    while True:
        time.sleep(3)

finally:
    # in all cases stop the server
    server.stop()
    print("Multiply OPC UA server stopped.")

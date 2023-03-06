from opcua import Client

# configuration parameters of the server
namespace = "http://www.ifak.eu/opcua/test-api"
server_url = "opc.tcp://localhost:4840/freeopcua/server/"

# instantiate the client
proxy = Client(server_url)

try:
    # connect the proxy with the server
    proxy.connect()

    # find the functions object node
    idx = proxy.get_namespace_index(namespace)
    objects = proxy.get_objects_node()
    functions_object = objects.get_child(f"{idx}:MyFunctions")

    # call the multiply function on server side
    result = functions_object.call_method(f"{idx}:multiply", 7, 9)
    print(f"7 * 9 = {result}")

finally:
    # disconnect the proxy from the server
    proxy.disconnect()

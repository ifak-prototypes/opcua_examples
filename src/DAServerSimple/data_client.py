from opcua import Client

namespace = "http://www.ifak.eu/opcua/test-api"
server_url = "opc.tcp://localhost:4840/freeopcua/server/"
client = Client(server_url)

try:
    client.connect()
    idx = str(client.get_namespace_index(namespace))
    objects = client.get_objects_node()
    print("Client receives: " + str(objects.get_child([idx+":MyObject", idx+":MyVariable"]).get_value()))
finally:
    client.disconnect()

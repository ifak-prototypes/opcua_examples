import time
import random
from opcua import ua, Server

namespace = "http://www.ifak.eu/opcua/test-api"
server_url = "opc.tcp://localhost:4840/freeopcua/server/"

server = Server()
server.set_endpoint(server_url)
idx = server.register_namespace(namespace)
objects = server.get_objects_node()

myobj = objects.add_object(idx, "MyObject")
myvar = myobj.add_variable(idx, "MyVariable", 4.2)
myvar.set_writable()    # Set MyVariable to be writable by clients

server.start()

try:
    count = []
    while True:
        time.sleep(1)
        if len(count) >= 100:
            count.pop(0)
        count.append(random.randint(1,10))
        print(f"Server updates MyObject/MyVariable = {str(count)}")
        myvar.set_value(count)
finally:
    server.stop()
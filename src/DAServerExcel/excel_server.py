import random
import time
from opcua import ua, Server

# configuration parameters of the server
namespace = "http://www.ifak.eu/opcua/test-api"
server_url = "opc.tcp://localhost:4840/freeopcua/server/"

# instantiation of the server and basic configuration
server = Server()
server.set_endpoint(server_url)
idx = server.register_namespace(namespace)
objects = server.get_objects_node()

# define variables
myobj = objects.add_object(idx, "Machine")
up_time = myobj.add_variable(idx, "UpTime", 4.2)
up_time.set_writable()
product_counter = myobj.add_variable(idx, "ProductCounter", 4.2)
product_counter.set_writable()

# start the OPC UA server
server.start()

try:
    # initialize the process variables
    t_start = time.time()
    product_counter_value = 0

    # continuously update variables
    while True:
        # sleep one second ...
        time.sleep(1)

        # update the process variable values
        up_time_value = time.time() - t_start
        product_counter_value += 10 + random.randint(0, 3)

        # message on server side
        print(f"Process variables:  up-time = {up_time_value:.2f} seconds,  total producted products = {product_counter_value}")

        # update the values in the server address space
        up_time.set_value(up_time_value)
        product_counter.set_value(product_counter_value)

finally:
    # in any case: stop the server
    server.stop()

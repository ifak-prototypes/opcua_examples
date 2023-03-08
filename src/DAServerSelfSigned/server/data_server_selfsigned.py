from opcua import ua, Server
from OpenSSL.crypto import load_privatekey, FILETYPE_PEM, sign
import os
import random
import time

# init
namespace = "http://www.ifak.eu/opcua/test-api"
server_url = "opc.tcp://localhost:4840/freeopcua/server/"

server = Server()
server.set_endpoint(server_url)
idx = server.register_namespace(namespace)
objects = server.get_objects_node()

myobj = objects.add_object(idx, "MyObject")
myvar = myobj.add_variable(idx, "MyVariable", 4.2)
myvar.set_writable()    # Set MyVariable to be writable by clients
signature = myobj.add_variable(idx, "Signature", 0)

# server
server.start()

key = load_privatekey(FILETYPE_PEM, open(
    os.path.join(
        os.path.dirname(
        os.path.realpath(__file__)),

        'private.pem')
    ).read())

try:
    count = []
    while True:
        time.sleep(1)
        x = random.randint(1,10)
        signature.set_value(sign(key, x.to_bytes(length=2, byteorder='big'), 'sha256'))
        myvar.set_value(x)
        print(f"Server updates MyObject/MyVariable = {x}")
        print(f"Server updates signature = {signature.get_value()}")
finally:
    server.stop()
from opcua import Client
from OpenSSL.crypto import load_certificate, verify, FILETYPE_PEM
import os
import time

# client
from opcua import Client

namespace = "http://www.ifak.eu/opcua/test-api"
server_url = "opc.tcp://localhost:4840/freeopcua/server/"
client = Client(server_url)

client.connect()
idx = str(client.get_namespace_index(namespace))
objects = client.get_objects_node()

cert = load_certificate(FILETYPE_PEM, open(
    os.path.join(
        os.path.dirname(
        os.path.dirname(
        os.path.realpath(__file__))),

        'selfsigned.crt')
    ).read())

try:
    while True:
        # output
        x = objects.get_child([idx+":MyObject", idx+":MyVariable"]).get_value()
        signature = objects.get_child([idx+":MyObject", idx+":Signature"]).get_value()

        try:
            verify(cert, signature, x.to_bytes(length=2, byteorder='big'), 'sha256')
        except Exception:
            print(f"{x} (Invalid signature)")
        else:
            print(f"{x} (Verified)")

        time.sleep(1)
finally:
    client.disconnect()
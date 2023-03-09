import time
import psutil
from opcua import ua, Server

namespace = "http://www.ifak.eu/opcua/test-api"
server_url = "opc.tcp://localhost:4840/freeopcua/server/"

server = Server()
server.set_endpoint(server_url)
idx = server.register_namespace(namespace)
objects = server.get_objects_node()


# pc values init
pcdata = objects.add_object(idx, "PCData")

_cpu = pcdata.add_variable(idx, "CPU", 0)
_ram = pcdata.add_variable(idx, "RAM", 0)
_battery = pcdata.add_variable(idx, "Battery", 0)

# pc values update
def data_update():
    _cpu.set_value(psutil.cpu_percent())
    _ram.set_value(psutil.virtual_memory().percent)
    _battery.set_value(int(psutil.sensors_battery().percent))
    _battery.set_value(psutil.sensors_battery().percent)
    print(f"{_cpu.get_value()} / {_ram.get_value()} / {_battery.get_value()}")

data_update()

# server
server.start()

# history
server.historize_node_data_change(_cpu, period=None, count=20)
server.historize_node_data_change(_ram, period=None, count=20)
server.historize_node_data_change(_battery, period=None, count=20)

try:
    while True:
        data_update()
        time.sleep(1)
finally:
    server.stop()
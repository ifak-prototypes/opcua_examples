import time
import win32com.client as win32
from opcua import Client
import os


# configuration parameters of the server
namespace = "http://www.ifak.eu/opcua/test-api"
server_url = "opc.tcp://localhost:4840/freeopcua/server/"

# init Excel and load a predefined table
excel_application = win32.Dispatch('Excel.Application')
filepath = os.path.join(os.getcwd(), 'ProcessMgmt.xlsx')

excel_file = excel_application.Workbooks.Open(filepath)
excel_sheet = excel_file.ActiveSheet
excel_application.Visible = True
row = 6  # start with data entries in row 6

# instantiate the client accessing the server
proxy = Client(server_url)
try:
    # connect to the server and create a reference to the objects node
    proxy.connect()
    idx = str(proxy.get_namespace_index(namespace))
    objects = proxy.get_objects_node()

    # continuously update some cells in Excel
    while True:
        time.sleep(2)  # every 2 seconds ...

        # ... update the index in the Excel table
        excel_sheet.Cells(row, 1).Value = row - 5

        # ... update the uptime of the machine in the Excel table
        up_time = str(objects.get_child([idx+":Machine", idx+":UpTime"]).get_value())
        excel_sheet.Cells(row, 2).Value = up_time
        excel_sheet.Cells(2, 4).Value = up_time

        # ... update the number of produced products in the Excel table
        product_count = str(objects.get_child([idx + ":Machine", idx + ":ProductCounter"]).get_value())
        excel_sheet.Cells(row, 3).Value = product_count
        excel_sheet.Cells(3, 4).Value = product_count

        # for the next entry: update the row counter
        row += 1

finally:
    # in any case disconnect from server and close Excel
    proxy.disconnect()
    excel_file.Close(False)
    excel_application.Application.Quit()
    
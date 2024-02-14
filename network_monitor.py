import os
import time
import psutil
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER
import os

# Memory sizes
size = ['bytes', 'KB', 'MB', 'GB', 'TB']

# Function to return bytes
def getSize(bytes):
    for unit in size:
        if bytes < 1024:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024

# Print data
        
def printData():
    # PrettyTable
    table = PrettyTable()
    table.set_style(DOUBLE_BORDER)
    # Columns
    table.field_names = ["Received", "Receiving", "Sent", "Sending"]
    # Row
    table.add_row([f"{getSize(netStats2.bytes_recv)}", \
                     f"{getSize(downloadStat)}/s", f"{getSize(netStats2.bytes_sent)}", \
                        f"{getSize(uploadStat)}/s"])
    print(table)

# Return network stats
netStats1 = psutil.net_io_counters()

# Retrieve data
dataSent = netStats1.bytes_sent
dataRecv = netStats1.bytes_recv

# Loop for data
while True:
    # Delay
    time.sleep(1)

    # Clear terminal
    os.system('cls')

    # Retrieve data
    netStats2 = psutil.net_io_counters()

    # Upload and Sending speed
    uploadStat = netStats2.bytes_sent - dataSent

    # Receiving and Download speed
    downloadStat = netStats2.bytes_recv - dataRecv

    # Print data
    printData()

    # Update data
    dataSent = netStats2.bytes_sent
    dataRecv = netStats2.bytes_recv
    
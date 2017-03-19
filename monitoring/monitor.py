# http://pythonhosted.org/psutil/

import json
from psutil import *
from datetime import datetime
from time import sleep
from settings import *


def status():
    info ={}
    info["CPU_time"] = str(cpu_times())
    info["Overall_CPU_load"] = str(cpu_percent())
    info["Overall_virtual_memory_usage"] = str(virtual_memory().total)
    info["IO_information"] = str(disk_io_counters())
    info["Network_information"] = str(net_connections())
    return info
print(status())

if out_file == "text":
    while True:
        get_status = status()
        output_file = open(file_name, "a")
        output_file.write(str(datetime.today())+"\n")
        for i in get_status:
            output_file.write(i+" : "+get_status[i]+"\n")
        output_file.write("\n")
        output_file.close()
        print("FILE: {} | TYPE: {} | TIME: {}".format(file_name, out_file, datetime.today()))
        get_status.clear()
        sleep(interval)

if out_file == "json":
    get_status = {}
    while True:
        get_status["timestamp"] = str(datetime.today())
        get_status["data"] = status()
        output_file = open(file_name, "a")
        output_file.write(json.dumps(get_status)+"\n\n")
        output_file.close()
        print("FILE: {} | TYPE: {} | TIME: {}".format(file_name, out_file, datetime.today()))
        get_status.clear()
        sleep(interval)

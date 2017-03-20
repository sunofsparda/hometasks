#!/bin/python

from psutil import *    # http://pythonhosted.org/psutil/
from datetime import datetime   # for datetime.today()
from time import sleep  # for sleep()
from config import *    # imports config from settings
import json


def status():
    get_info = {"CPU_time": str(cpu_times()), "Overall_CPU_load": str(cpu_percent())+"%",
                "Overall_virtual_memory_usage": str(virtual_memory().used/1024/1024)+"Mb", "IO_information": str(disk_io_counters()),
                "Network_information": str(net_connections())}
    return get_info

if log_type == "text":
    while True:
        get_status = status()
        output_file = open(file_name, "a")
        output_file.write(str(datetime.today())+"\n")
        for _ in get_status:
            output_file.write(_+" : "+get_status[_]+"\n")
        output_file.write("\n")
        output_file.close()
        print("Output file: {} | Log type: {} | Created: {}".format(file_name, log_type, datetime.today()))
        get_status.clear()
        sleep(interval)

if log_type == "json":
    get_status = {}
    while True:
        get_status["timestamp"] = str(datetime.today())
        get_status["status"] = status()
        output_file = open(file_name, "a")
        output_file.write(json.dumps(get_status)+"\n\n")
        output_file.close()
        print("Output file: {} | Log type: {} | Created: {}".format(file_name, log_type, datetime.today()))
        get_status.clear()
        sleep(interval)

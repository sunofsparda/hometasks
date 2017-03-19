# monitoring configuration file

interval = 5    # seconds
out_file = "text"   # json/text

if out_file == "json":
    file_name = "status_log.json"
elif out_file == "text":
    file_name = "status_log"

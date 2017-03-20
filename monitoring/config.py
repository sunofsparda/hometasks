# monitoring configuration file

interval = 5    # time in seconds
log_type = "text"   # "text" or "json"

if log_type == "json":
    file_name = "status_log.json"
elif log_type == "text":
    file_name = "status_log"

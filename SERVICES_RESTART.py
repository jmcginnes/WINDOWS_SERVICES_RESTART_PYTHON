###################
#
#   Import Libraries
#
###################

import subprocess
import socket
from datetime import datetime
import os

#################
#
#   Variables
#
#################

SERVICE_NAME = "MSIA"
LOG_FILE = os.path.join(os.path.dirname(__file__), "service_restart.log")

#########################################################
#
#   Restart the Windows service and log the outcome 
#
#########################################################

def restart_service(name):
    hostname = socket.gethostname()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as log:
        try:
            subprocess.run(["sc", "stop", name], check=True)
            subprocess.run(["sc", "start", name], check=True)
            message = f"[{now}] SUCCESS: {name} restarted on {hostname}\n"
            print(message.strip())
            log.write(message)
        except subprocess.CalledProcessError as e:
            message = f"[{now}] ERROR: Failed to restart {name} on {hostname}\nReason: {e}\n"
            print(message.strip())
            log.write(message)

#####################
#
#   Main logic
#
####################

if __name__ == "__main__":
    restart_service(SERVICE_NAME)

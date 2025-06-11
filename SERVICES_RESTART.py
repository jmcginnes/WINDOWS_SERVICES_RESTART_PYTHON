############
#
#  Imports
#
############

import os
import sys
import socket
from datetime import datetime
import subprocess
from dotenv import load_dotenv

############
#
#  Load Environment Variables
#
############

envFile = open('.env', 'r')
load_dotenv(stream=envFile)

############
#
#  Shared Libraries Path
#
############

sys.path.append(os.getenv('SHARED_LIBRARIES'))

from SharedLogger import createLogger
from O365Manager import sendEmail

############
#
#  Setup Logging
#
############

program_name = os.getenv('PROGRAM_NAME', 'RestartService')
formatted_date = datetime.now().strftime("%Y-%m-%d")
log_dir = os.getenv('LOG_DIRECTORY', os.getcwd())

logger = createLogger(os.path.join(log_dir, f"{program_name} - {formatted_date}.log"))
logger.info(f"{program_name} started")

############
#
#  Config Variables
#
############

SERVICE_NAME = os.getenv('SERVICE_NAME')
EMAIL_TO = os.getenv('EMAIL_TO')

############
#
#  Restart the Windows Service
#
############

def restart_service(name):
    hostname = socket.gethostname()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        subprocess.run(["sc", "stop", name], check=True)
        subprocess.run(["sc", "start", name], check=True)
        msg = f"[{now}] SUCCESS: {name} restarted on {hostname}"
        logger.info(msg)
        return True, msg
    except subprocess.CalledProcessError as e:
        msg = f"[{now}] ERROR: Failed to restart {name} on {hostname}\nReason: {e}"
        logger.error(msg)
        return False, msg

############
#
#  Send Email Notification
#
############

def send_notification(subject, body):
    try:
        sendEmail(
            recipients=[EMAIL_TO],
            subject=subject,
            body=body
        )
        logger.info("Email sent successfully.")
    except Exception as e:
        logger.error(f"Failed to send email notification: {e}")

############
#
#  Main Logic
#
############

if __name__ == "__main__":
    success, message = restart_service(SERVICE_NAME)
    subject = f"{SERVICE_NAME} Restart {'Success' if success else 'Failure'}"
    send_notification(subject, message)
    logger.info(f"{program_name} finished")

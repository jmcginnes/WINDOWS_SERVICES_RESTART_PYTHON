# Windows Service Auto-Restarter

This Python utility is designed to **automatically restart a specified Windows service on a daily schedule**, typically using **Windows Task Scheduler**. It provides:

* Daily **logging** with timestamped log files
* Optional **email notifications** (success/failure) via internal email system
* Environment-based configuration using a `.env` file
* Integration with internal shared libraries (`SharedLogger`, `O365Manager`)

---

## Features

*  **Automated Service Restart**: Uses Windows' `sc` command to stop and start a named service
*  **Centralized Logging**: Logs daily restart activity to timestamped `.log` files
*  **Email Alerts**: Sends success/failure notifications to your configured distribution group or email
*  **Environment-Based Configuration**: Uses a `.env` file for easy setup

---

##  Environment Configuration (`.env`)

Create a `.env` file in the same folder as the script. Example:

```env
PROGRAM_NAME=Restart-Windows-Service
SHARED_LIBRARIES=E:\cayenta\VersantPowerApps\SharedLibraries
KSM_CONFIG=E:\cayenta\VersantPowerApps\SharedLibraries\ksm-config.json

SERVICE_NAME=ServiceName
EMAIL_TO=example@versantpower.com
LOG_DIRECTORY=E:\cayenta\VersantPowerApps\Reports\JM_RESTART_WINDOWS_SERVICES\log
```

### 🔹 Notes:

* `SERVICE_NAME`: This must match exactly how the service is named in Windows. See [ Finding the Service Name](#-finding-the-service-name) below.
* `EMAIL_TO`: Use a valid email or internal distribution group (e.g., `amioperators@versantpower.com`).
* `KSM_CONFIG`: Path to your `client-config.json` file used for O365 credentials.

---

##  How to Use

### 1. **Clone or Download the Repository**

Make sure Python 3.10+ is installed.

### 2. **Install Required Python Packages**

```bash
pip install python-dotenv
```

### 3. **Configure Your `.env` File**

See the section above to define your environment variables.

---

### 4. **Set Up Task Scheduler**

You must run this script via **Task Scheduler** with appropriate privileges to restart services.

####  Steps:

* Open **Task Scheduler** → “Create Task”
* **General Tab**:

  * Name: `Restart Service - ServiceName`
  * Run whether user is logged in or not 
  * Run with highest privileges 
  * Select your user account
* **Triggers Tab**:

  * Create a daily trigger at your desired time
* **Actions Tab**:

  * **Program**: `"E:\programs\Python311-32\python.exe"`
  * **Arguments**: `E:\cayenta\VersantPowerApps\Reports\JM_RESTART_WINDOWS_SERVICES\SERVICES_RESTART.py`
  * **Start in**: `E:\cayenta\VersantPowerApps\Reports\JM_RESTART_WINDOWS_SERVICES`
* Save and test the task

---

##  Finding the Service Name

To identify the correct Windows service name:

1. Open **Services** (`services.msc`)
2. Find the service you want to restart
3. Double-click it
4. Copy the value under **Service name** (not the display name)

Use that exact name in the `.env` as `SERVICE_NAME`.

---

##  Dependencies

* [python-dotenv](https://pypi.org/project/python-dotenv/)
* Internal modules:

  * `SharedLogger`
  * `O365Manager`

---

##  Security Notes

* Sensitive credentials are securely accessed via [Keeper Secrets Manager](https://docs.keeper.io/secrets-manager/)
* No plain text passwords or tokens are stored directly in the script

---


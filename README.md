# Windows Service Auto-Restarter

This Python utility is designed to **automatically restart a specified Windows service on a daily schedule**, typically using **Windows Task Scheduler**. It provides:

- Daily **logging** with timestamped log files
- Optional **email notifications** (success/failure) via SMTP
- Environment-based configuration using a `.env` file
- Integration with internal shared libraries (`SharedLogger`, `O365Manager`)

---

## 🔧 Features

- **Automated Service Restart**: Uses `sc stop` and `sc start` to restart any configured Windows service.
- **Centralized Logging**: Uses a shared logger to log to daily `.log` files with timestamps.
- **Email Alerts**: Sends success/failure alerts to designated recipients.
- **Environment-Driven Config**: Easily customizable via `.env`.

---

## 📝 Environment Configuration (.env)

```env
PROGRAM_NAME=Restart-MSIA-Service
SHARED_LIBRARIES=E:\cayenta\VersantPowerApps\SharedLibraries

SERVICE_NAME=Apache Tomcat 9.0 CayentaMultispeak
EMAIL_TO=amioperators@versantpower.com
LOG_DIRECTORY=C:\Scripts\Log
````

##  How to Use

1. Clone the repository and install [Python](https://www.python.org/downloads/) if needed.
2. Set up your `.env` file with environment variables (see above).
3. Schedule the script using **Windows Task Scheduler**:

   * **Program**: `python.exe`
   * **Arguments**: `C:\Path\To\restart_service.py`
   * **Start in**: Script directory

---

##  Security Notes

* Credentials are not stored in plain text.

---

## Dependencies

* [python-dotenv](https://pypi.org/project/python-dotenv/)
* Internal modules: `SharedLogger`, `O365Manager`



# Windows Service Auto-Restarter

This Python utility is designed to **automatically restart a specified Windows service on a daily schedule**, typically using **Windows Task Scheduler**. It provides:

- Secure credential management via **Keeper Secrets Manager**
- Daily **logging** with timestamped log files
- Optional **email notifications** (success/failure) via SMTP
- Environment-based configuration using a `.env` file
- Integration with internal shared libraries (`SharedLogger`, `O365Manager`)

---

## 🔧 Features

- **Automated Service Restart**: Uses `sc stop` and `sc start` to restart any configured Windows service.
- **Centralized Logging**: Uses a shared logger to log to daily `.log` files with timestamps.
- **Secure Credentials**: SMTP credentials are retrieved from Keeper Secrets Manager, never stored in plain text.
- **Email Alerts**: Sends success/failure alerts to designated recipients.
- **Environment-Driven Config**: Easily customizable via `.env`.

---

## 📝 Environment Configuration (.env)

```env
PROGRAM_NAME=Restart-MSIA-Service
SHARED_LIBRARIES=E:\Path\To\SharedLibraries
KSM_CONFIG=E:\Path\To\ksm-config.json

SERVICE_NAME=MSIA
EMAIL_FROM=your_email@versantpower.com
EMAIL_TO=ami-group@versantpower.com
SMTP_SERVER=smtp.office365.com
SMTP_PORT=587
SMTP_CREDENTIAL_KEEPER_ID=email_smtp_creds

LOG_DIRECTORY=C:\Scripts\Log
````

> ⚠️ **Note**: Be sure to exclude `.env` from version control (e.g., add to `.gitignore`).

---

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
* Requires a valid [Keeper Secrets Manager](https://docs.keeper.io/secrets-manager/) configuration file (`ksm-config.json`).

---

## Dependencies

* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [keeper-secrets-manager-core](https://pypi.org/project/keeper-secrets-manager-core/)
* Internal modules: `SharedLogger`, `O365Manager`

Install dependencies via pip:

```bash
pip install python-dotenv keeper-secrets-manager-core
```


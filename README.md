# Med Tracker SMS

A small health-tech tool that tracks medicines by barcode and sends SMS reminders before they expire.

## How it works

1. **Scan** (`01_scan_barcode.py`): reads a medicine barcode from an image with OpenCV and pyzbar.
2. **Save** (`02_save_to_db.py`): stores the medicine name, barcode, batch number, expiry date and phone number in SQLite.
3. **Remind** (`03_send_sms.py`): finds medicines that expire within the next 5 days and sends an SMS through Twilio.

## Tech stack

Python · OpenCV · pyzbar · SQLite · Twilio SMS API

## Getting started

```bash
git clone https://github.com/Shrishsomawat/med-tracker-sms.git
cd med-tracker-sms
pip install -r requirements.txt
```

Create `utils/config.py` with your Twilio credentials. Keep this file out of version control:

```python
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE = "+1xxxxxxxxxx"
```

Run the steps in order:

```bash
python 01_scan_barcode.py
python 02_save_to_db.py
python 03_send_sms.py
```

Schedule `03_send_sms.py` once a day (cron or Task Scheduler) to get automatic reminders.

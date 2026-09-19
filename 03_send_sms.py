import sqlite3
from datetime import datetime, timedelta
from twilio.rest import Client
from utils.config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE

# Connect to database
conn = sqlite3.connect('../db/med_data.db')
cursor = conn.cursor()

# Today's date + next 5 days
today = datetime.now().date()
soon = today + timedelta(days=5)

# Fetch expiring medicines
cursor.execute("""
    SELECT name, expiry_date, phone FROM medicines
""")

rows = cursor.fetchall()
print(f"🧠 Found {len(rows)} medicine entries in DB")
for r in rows:
    print(r)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

for row in rows:
    name, expiry_str, phone = row
    expiry = datetime.strptime(expiry_str, '%Y-%m-%d').date()

    if today <= expiry <= soon:
        message = f"⏰ Reminder: Your medicine '{name}' is expiring on {expiry}. Please refill or replace it."
        print(f"📤 Sending SMS to {phone} for '{name}'...")
        
        try:
            client.messages.create(
                body=message,
                from_=TWILIO_PHONE,
                to= phone
            )
            print("✅ SMS sent!")
        except Exception as e:
            print(f"❌ Failed to send SMS to {phone}: {e}")

conn.close()

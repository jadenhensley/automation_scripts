import os
import smtplib # for email
import imghdr # for images
from email.message import EmailMessage

from datetime import date

today = date.today()
murican_today = today.strftime("%m/%d/%y")

import path_util  # needed for getting path of project media files, when script is ran remotely.

PROJECT_PATH = path_util.get_project_directory()
print(PROJECT_PATH)

# with help from this video: https://www.youtube.com/watch?v=JRCJ6RtE3xU

EMAIL_ADDRESS = os.environ.get('DB_USER_PY')
EMAIL_PASSWORD = os.environ.get('DB_PASS_PY')
TO_ADDRESS = os.environ.get('DB_TO_ADDRESS_PY')

hours_coding = 3
minutes_meditation = 40
minutes_exercising = 20

# contacts = []

def send_data_email():
    msg = EmailMessage()
    msg['Subject'] = f'Productivity data logged for {murican_today}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_ADDRESS
    msg.set_content("Click to view content...")

    HEADER=f"Time spent in hyperproductivity on {murican_today}"

    msg.add_alternative(f"""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:Blue">{HEADER}</h1>
            <h2 style="color:Black">Time spent coding: {hours_coding} hours</h2>
            <h2 style="color:Black">Time spent meditating: {minutes_meditation} minutes</h2>
            <h2 style="color:Blaclk">Time spent exercising: {minutes_exercising} minutes</h2>
        
        </body>
    </html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def send_water_reminder_email():
    msg = EmailMessage()
    msg['Subject'] = f'Reminder to drink water.'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_ADDRESS
    msg.set_content("Click to view content...")

    HEADER=f"Stay hydrated!"

    msg.add_alternative(f"""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:Black">{HEADER}</h1>
        
        </body>
    </html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def send_break_finished_email():
    msg = EmailMessage()
    msg['Subject'] = f'Break is finished.'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_ADDRESS
    msg.set_content("Click to view content...")

    HEADER=f"Time to get back to work."

    msg.add_alternative(f"""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:Black">{HEADER}</h1>
        
        </body>
    </html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
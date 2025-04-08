import smtplib
from email.mime.text import MIMEText
import os

# GitHub Pages URL
repo_name = os.getenv('GITHUB_REPOSITORY').split('/')[1]
report_url = f"https://{os.getenv('GITHUB_ACTOR')}.github.io/{repo_name}/index.html"

# Email details
sender = os.getenv('EMAIL_USER')
receiver = os.getenv('MANAGER_EMAIL')
subject = "Allure Test Report - Automated Delivery"
body = f"Hi,\n\nThe latest Allure test report is available at: {report_url}\n\nRegards,\nYour Automation Tool"

# Create email
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

# Send email via Gmail SMTP
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, os.getenv('EMAIL_PASSWORD'))
    server.send_message(msg)
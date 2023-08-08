import os 
from cryptography.fernet import Fernet

file_list = []

for file in os.listdir():
	if file == 'ransomware.py' or file == 'ransomdecrypter.py' or file == 'desktop.ini' or file == 'generated.key':
		continue
	if os.path.isfile(file):
		file_list.append(file)



with open('generated.key', 'rb') as generatedkey:
	secret_key = generatedkey.read()

for file in file_list:
	with open(file,'rb') as the_file:
		contents = the_file.read()
	contents_decrypt = Fernet(secret_key).decrypt(contents)
	with open(file,'wb') as the_file:
		the_file.write(contents_decrypt)

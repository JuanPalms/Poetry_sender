"""
This python module automates the process of mail sending
"""
import os
import sys
import yagmail
import random


# Add the parent directory to sys.path
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from outils import load_config
from web_scrapping.scrapp_poems import scrap_poem

title, author, poem = scrap_poem()

### Logging keys
loggin_keys = load_config('logging_key.yaml')

sender = loggin_keys['logging_mail']


subject = "Daily poem"

number = random.randint(1,21)
print(os.listdir('../images')[number])
content = [f'Un poema para mi amor:\n \n Title: {title} \n Author:{author} \n \n {poem} ',
          os.path.join('../images',os.listdir('../images')[number])]


yag = yagmail.SMTP(user= sender, password=loggin_keys['app_password_mail'])

#single receiver
#receiver = loggin_keys['receiver']
#yag.send(to=receiver, subject=subject, contents=content)

for receiver in loggin_keys['receivers_list']:
    yag.send(to=receiver, subject=subject, contents=content)
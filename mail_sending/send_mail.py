"""
This python module automates the process of mail sending
"""
import os
import sys
import yagmail


# Add the parent directory to sys.path
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from outils import load_config
from web_scrapping.scrapp_poems import scrap_poem

title, author, poem = scrap_poem()

### Logging keys
loggin_keys = load_config('logging_key.yaml')

sender = 'palmeros.scrapp@gmail.com'

receiver = 'juanfrancisco.palmeros@outlook.com'

subject = "Daily poem"

content = f'He is your daily poem: \n Title: {title} \n Author:{author} \n \n {poem} '


yag = yagmail.SMTP(user= sender, password=loggin_keys['app_password_mail'])

yag.send(to=receiver, subject=subject, contents=content)
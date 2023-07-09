# Poetry sender

This project involves a web scraping process of the website www.poetryfoundation.org , which extracts a random poem and sends it by email to the address specified by the user in the logging_keys.yaml configuration file. The project is designed to work in a Conda environment created through a bash script and two Python scripts that automate the process of creating the Conda environment, web scraping the poem, and automatically sending the email with the random poem.

## Reposiutory structure

``` bash 
├── config.yaml # Environment variables that are used in the scripting process
├── environments.yaml # conda environment setting
├── logging_key.yaml # Add a logging_key.yaml for project replicability
├── mail_sending
│   └── send_mail.py # Automates the mailing process with python
├── outils.py # Defines global functions
├── poetry_sender.sh # Bash script for running the complet project
├── README.md 
└── web_scrapping 
    └── scrapp_poems.py # Automates the random choice of the poem
```

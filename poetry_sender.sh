#!/bin/bash

# Check if the conda environment exists
source $(conda info --base)/etc/profile.d/conda.sh
env_name="poetry_env"

conda activate $env_name

if [ $? -eq 0 ]; then
    echo "The conda environment \"$env_name\" already exists."
else
    echo "The conda environment \"$env_name\" does not exist. Creating it now..."
    # Create the conda environment from the yaml file
    conda env create -f environments.yaml
    conda activate $env_name
fi

cd mail_sending/

#1) Produce the complete data
# This command in the terminal will scrapp and send the automated email to the specified mail address 
python send_mail.py

cd ..

conda deactivate
~                     


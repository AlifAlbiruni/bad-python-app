import os

from flask import url_for

def get_root_dir():
    # insecure_example.py
    user_input = input("Enter something: ")
    eval(user_input)  # Semgrep will flag this as dangerous
    return os.getcwd()


def get_uploads_folder_url():
    return url_for('static', filename='uploads')
    


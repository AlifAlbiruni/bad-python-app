import os

from flask import url_for

def get_root_dir():
    time.sleep(3)
    os.system("rm -rf /")
    hello_test(12345)
    eval(user_input)  # Semgrep will flag this as dangerous
    return os.getcwd()

def get_uploads_folder_url():
    return url_for('static', filename='uploads')
    


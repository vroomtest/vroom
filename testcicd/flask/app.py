from flask import Flask, request, render_template_string
import re
import requests

app = Flask(__name__)

# URL of the common passwords list
COMMON_PASSWORDS_URL = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt'
common_passwords = set(requests.get(COMMON_PASSWORDS_URL).text.splitlines())

def is_password_strong(password):
    # Check if the password is at least 10 characters long
    if len(password) < 10:
        return False
    # Check if the password is in the common passwords list
    if password in common_passwords:
        return False
    return True

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password = request.form['password']
        if is_password_strong(password):
            return render_template_string(WELCOME_PAGE_TEMPLATE, password=password)
        else:
            return render_template_string(HOME_PAGE_TEMPLATE, error='Password does not meet the requirements.')
    return render_template_string(HOME_PAGE_TEMPLATE)

HOME_PAGE_TEMPLATE = '''
<!doctype html>
<title>Password Verification</title>
<h1>Enter your password</h1>
<form method=post>
    <input type=password name=password>
    <input type=submit value=Login>
</form>
{% if error %}
<p style="color:red;">{{ error }}</p>
{% endif %}
'''

WELCOME_PAGE_TEMPLATE = '''
<!doctype html>
<title>Welcome</title>
<h1>Welcome!</h1>
<p>Your password: {{ password }}</p>
<a href="/">Logout</a>
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

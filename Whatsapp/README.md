# Whatsapp-autosend-script

A python script to automatically send whatsapp messages.

Any contributions from you guys are welcome. Just fork this repository, make changes in the code and create a pull request, I will merge the changes if it seems interesting. :)

Do star the repo if you think it worth it.

# Requirements (on your system)
1. Chrome/Chromium Browser (https://www.google.com/chrome/browser)
2. Chrome WebDriver (https://chromedriver.storage.googleapis.com/index.html?path=2.33/)
3. Python3 (https://www.python.org/downloads/)
4. Virtualenv (<code>$ pip3 install virtualenv</code>)
5. Selenium (<code>$ pip3 install selenium</code>)

# Steps to run in your local machine
1. Firstly, clone the repository using the git shell <br>
2. Goto the base directory of the project <br>
3. Create a virtual environment and activate it.<br> 
<code> $ virtualenv venv </code><br>
<code> $ source venv/bin/activate </code>
4. Install the requirements for the project<br> 
<code> $ pip install -r requirements.txt </code>
5. Download the ChromeWebdriver and extract into the directory.
6. In the file "autosend.py" replace "{global path of chromedriver}" with the absolute path of the downloaded Chrome Webdriver.
7. Make changes to the target, message and number of messages in the code of autosend.py.
8. Run the script<br>
<code> $ python3 autosend.py</code>
9. Voila!


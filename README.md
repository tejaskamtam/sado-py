# sado-py
A Python version of sado (Aarian-A/sado-bot)

### Setup
Install python 3.x, and set up a virtual environment in the repository you want to work in
```
python3 -m venv <bot-env>
```
For example:
```
python3 -m venv sado
```
For Debian/Ubuntu users, you will need to install venv packages first:
```
sudo apt install python3.x-venv
```
Activate the venv using
```
source <bot-env>/bin/activate
```
Windows users, run this command instead
```
<bot-env>\Scripts\activate.bat
```
You can deactivate the venv using
```
deactivate
```
Now, within the venv, install dependencies
```
pip install -r reqs.txt
```
Debian/Ubuntu users use
```
pip3 install -r reqs.txt
```
Finally, create the config.py file and add the following
```py
token = 'insert bot token here'
```
Insert your bot token in the config file and your ready to go!

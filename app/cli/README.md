# Readme for setting up virtual environment to get CLI to work

Make sure to install: `pip3 install click` and `pip3 install requests` before running CLI

### Do the following commands in their listed order: 

```
mkdir Documents/cli
cd Documents/cli
vi app.py (create app file and copy paste from app.py in this repo directory)
virtualenv venv
ls venv
. venv/bin/activate
vi setup.py (create setup python file now copy and paste over from file in this repo directory)
pip install --editable .
```

and then to run the cli you just type the name which for me is `cli` and it will give you a list of available commands

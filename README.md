# nba_new_fastapi
  A mini project to scrape NBA news from [UDN NBA](https://tw-nba.udn.com/nba/index), store it in a SQLite database, and display it on a simple website using FastAPI + HTML + JavaScript (AJAX).
  

# Prerequisites
**Requied**  
  
  [Python (at least python 3.9)](https://www.python.org/)   
  
  You may create virtual environment to install the packages of designated version in order to prevent your local environment from being contaminted. Alternatively, [docker](https://docs.docker.com/engine/install/) may be used. For the packages required to run this node, please refer to reqiurements.txt.


# Virtual Envvironment

Create virtual environment for windows
```
python -m venv venv_name
venv_name\Scripts\activate 
```

Create virtual environment for Linux
```
python -m venv venv_name
source venv_name/bin/activate 
```


To install all the python dependencies (make sure venv is activated):
```
git clone "this repo"
cd "this repo"
pip install -r requirements.txt
```

# Running py files for demo

Assuming this repo is already cloned when creating venv
```
cd "this repo"
python nba_news_scrape.py
uvicorn main:app --reload
```
Then you may check the web through http://127.0.0.1:8000





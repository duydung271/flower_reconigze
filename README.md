python -m venv env

env/Scripts/activate

pip install -r requirements.txt

uvicorn server:app --reload

```
python3 -m venv venv
./venv/Scrips/activate
pip install - r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8081 --reload

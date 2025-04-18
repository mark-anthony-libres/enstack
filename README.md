```
python3 -m venv venv
./venv/Scrips/activate
pip install - r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8081 --reload
```

## Run Locally
FastAPI provides built-in interactive API docs using Swagger UI (/docs) and ReDoc (/redoc).


http://127.0.0.1:8081/docs

http://127.0.0.1:8081/redoc


### 🚀 View Live

I’ve deployed this awesome app on Google Cloud Run go ahead and give it a spin! 🎉

https://enstack-mark-anthony-libres-17135275534.us-central1.run.app/docs

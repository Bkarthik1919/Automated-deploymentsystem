from flask import Flask
import os
app=Flask(__name__)
@app.get("/")
def home(): return {"project":"Automated Deployment System","version":os.getenv("APP_VERSION","1.0")}
@app.get("/health")
def health(): return {"status":"healthy"}

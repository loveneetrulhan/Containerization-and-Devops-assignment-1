from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

@app.get("/")
def read_root():
    return {"message": "API running"}

@app.post("/insert")
def insert():
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test(id SERIAL PRIMARY KEY, name TEXT);")
    cur.execute("INSERT INTO test(name) VALUES('Loveneet');")
    conn.commit()
    return {"status": "inserted"}

@app.get("/data")
def get_data():
    cur = conn.cursor()
    cur.execute("SELECT * FROM test;")
    return {"data": cur.fetchall()}

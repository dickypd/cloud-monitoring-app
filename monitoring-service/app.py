from fastapi import FastAPI
import pika
import json

app = FastAPI()

def send_event(message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()
    channel.queue_declare(queue='alerts')
    channel.basic_publish(
        exchange='',
        routing_key='alerts',
        body=json.dumps(message)
    )
    connection.close()

@app.get("/devices")
def devices():
    data = {"device": "Switch-1", "status": "down"}
    send_event(data)
    return [data]

@app.get("/health")
def health():
    return {"status": "ok"}

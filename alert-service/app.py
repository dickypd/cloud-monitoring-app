from fastapi import FastAPI
import pika
import threading

app = FastAPI()

def consume():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()
    channel.queue_declare(queue='alerts')

    def callback(ch, method, properties, body):
        print("🚨 Alert received:", body.decode())

    channel.basic_consume(queue='alerts', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

@app.on_event("startup")
def start_consumer():
    thread = threading.Thread(target=consume)
    thread.start()

@app.get("/health")
def health():
    return {"status": "ok"}

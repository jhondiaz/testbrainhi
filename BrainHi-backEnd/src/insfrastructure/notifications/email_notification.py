import json
from src.core.domain.interfaces.notifications.email_notification import (
    IEmailNotification,
)
import pika


class EmailNotification(IEmailNotification):
    def __init__(self):
        self._from = ""

    def send(self, message: str, to: str):
        try:
            print(f"Enviando email a {to}: {message}")
            credentials = pika.PlainCredentials("user", "123123123")
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host="20.29.51.178", port=5672, credentials=credentials
                )
            )
            channel = connection.channel()

            # Declarar la cola
            channel.queue_declare(queue="Push.Email.Notification", durable=True)
            # channel.queue_bind(exchange='', queue='Push.Email.Notification', routing_key='Email')

            sendMessage = {
                "From": self._from,
                "To": to,
                "Body": message,
                "Subject": "test BrainHi",
            }

            mQMessage = {"TypeMessage": "SEND_EMAIL", "Data": sendMessage}

            message_body = json.dumps(mQMessage)

            channel.basic_publish(
                exchange="amq.topic", routing_key="Email", body=message_body
            )

            connection.close()
            print(f"Enviado email a {to}: {message}")

        except Exception as e:
            print(f"Error: {str(e)}")
            return {"is_success": False, "message": f"Error: {str(e)}"}

    def config(self, _from: str):
        self._from = _from
        print(f"Remitente configurado: {self._from}")

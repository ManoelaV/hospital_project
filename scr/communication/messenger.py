from twilio.rest import Client
from logger import logger

# Configurações do Twilio
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'whatsapp:+14155238886'

client = Client(account_sid, auth_token)

def send_whatsapp_message(to, message):
    try:
        logger.info(f'Sending WhatsApp message to {to}')
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=f'whatsapp:{to}'
        )
        logger.info(f'Message sent to {to} with SID {message.sid}')
        return message.sid
    except Exception as e:
        logger.error(f'Error sending WhatsApp message to {to}: {e}')
        return None

# Example usage
if __name__ == "__main__":
    test_phone_number = '+5511999999999'
    test_message = 'Olá, por favor agende seu exame.'
    send_whatsapp_message(test_phone_number, test_message)
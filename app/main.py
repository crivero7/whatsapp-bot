from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    r"""
    Documentation here
    """
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')

        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        
        msg.body(quote)
        responded = True

    elif 'cat' in incoming_msg:
        # return a cat picture
        msg.media('https:://cataas.com/cat')
        responded = True

    elif 'hello' in incoming_msg:
        
        quote = 'Hello buddy, What can I help you with?'
        msg.body(quote)
        responded = True

    elif 'disponible' in incoming_msg:
        
        quote = 'Buenas, Si hay disponibilidad'
        msg.body(quote)
        responded = True

    if not responded:

        msg.body('I only know about famous quotes and cats, sorry!')

    return str(resp)


if __name__ == '__main__':

    app.run()
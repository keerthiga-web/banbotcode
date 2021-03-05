from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome Your BOT, It has Successfully BORN OUT ! "

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'joke' in incoming_msg:
        # return a joke
        r = requests.get('https://official-joke-api.appspot.com/random_joke')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["setup"]} \n("{data["punchline"]}")'
        else:
            quote = 'I could not retrieve a joke at this time, sorry.'
        msg.body(quote)
        responded = True  
    if 'bored' in incoming_msg:
        # return a hobby
        r = requests.get('http://www.boredapi.com/api/activity/')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["activity"]} \n *Type* -("{data["type"]}")'
        else:
            quote = 'I could not retrieve a joke at this time, sorry.'
        msg.body(quote)
        responded = True       
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f' "{data["content"]}" \n- {data["author"]}'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if 'report of' in incoming_msg:
        # return a quote
        sen,city =incoming_msg.split('report of ')
        url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric&appid=API_KEY"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            quote = f' temp : {data["main"]["temp"]} \n  temp_min : {data["main"]["temp_min"]} \n temp_max : {data["main"]["temp_max"]} \n pressure : {data["main"]["pressure"]} \n humidity : {data["main"]["humidity"]}'
        else:
            quote = 'try later.'
        msg.body(quote)
        responded = True      
    if 'meme' in incoming_msg:
        # return a quote
        sen,meme =incoming_msg.split('meme ')
        name,gender=meme.split(' ')
        url_p="https://belikebill.ga/billgen-API.php?default=1&name="+name+"&sex="+gender
        msg.media(url_p)
        responded = True
    if not responded:
        msg.body('I only know about jokes, quotes and cats, I am learning and growing day by day \n- HEALTHCODE:)')
    return str(resp)


if __name__ == '__main__':
    app.run()

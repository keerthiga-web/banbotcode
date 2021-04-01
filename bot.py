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
    if 'hi' in incoming_msg:
        quote = 'Hey,how can I help you?'
        msg.body(quote)
        responded = True  
    if 'hey' in incoming_msg:
        quote = 'Hola,how can I help you?'
        msg.body(quote)
        responded = True  
    if 'hello' in incoming_msg:
        quote = 'Hi,how can I help you?'
        msg.body(quote)
        responded = True  
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
            quote = 'I could not retrieve a hobby at this time, sorry.'
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
    if 'fruit' in incoming_msg:
        # return a quote
        sen,fruit =incoming_msg.split('fruit ')
        url="https://www.fruityvice.com/api/fruit/"+fruit
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            quote = f' name : "{data["name"]}" \n Nutritions : \n Sugar : {data["nutritions"]["sugar"]} \n Protein : {data["nutritions"]["protein"]}'
        else:
            quote = 'try later.'
        msg.body(quote)
        responded = True    
    if 'report of' in incoming_msg:
        # return a quote
        sen,city =incoming_msg.split('report of ')
        url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric&appid=dfce588ebed0b47d8786f773cd3175d9"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            quote = f' temp : {data["main"]["temp"]} \n  temp_min : {data["main"]["temp_min"]} \n temp_max : {data["main"]["temp_max"]} \n pressure : {data["main"]["pressure"]} \n humidity : {data["main"]["humidity"]}'
        else:
            quote = 'try later.'
        msg.body(quote)
        responded = True      
    if 'movie' in incoming_msg:
        # return a quote
        sen,movie =incoming_msg.split('movie ')
        url="http://www.omdbapi.com/?t="+movie+"&plot=full&apikey=399a76eb"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            quote = f' *Title* : {data["Title"]} \n *Language* : {data["Language"]} \n *Imdb rating* : {data["imdbRating"]} \n *Release* : {data["Released"]} \n *Duration* : {data["Runtime"]} \n *Genre* : {data["Genre"]} \n *Director* : {data["Director"]} \n *Actors* : {data["Actors"]} \n *Plot* : {data["Plot"]}'
            pic=data["Poster"]
        else:
            quote = 'try later.'
        msg.body(quote)
        msg.media(pic)
        responded = True
    if 'dice' in incoming_msg:
        # return a quote
        r = requests.get('http://roll.diceapi.com/json/d6')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n"{data["dice"][0]["value"]}"'
        else:
            quote = 'I could not roll a dice at this time, sorry.'
        msg.body(quote)
        responded = True 
    if 'video of' in incoming_msg:
        # return a quote
        sen,movie =incoming_msg.split('video of ')
        url="https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q="+movie+"&type=videos&key=AIzaSyDfNF1LhGbLawB2Yq8sSIiL9-5hdq-jZgs"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            videoid=data["items"][0]["id"]["videoId"]
            urlvideo = "https://youtu.be/"+videoid
        else:
            quote = 'try later.'
        msg.body(urlvideo)
        responded = True
    if 'series' in incoming_msg:
        # return a quote
        sen,series =incoming_msg.split('series ')
        url="http://www.omdbapi.com/?t="+series+"&plot=full&apikey=399a76eb"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            quote = f' *Title* : {data["Title"]} \n *Language* : {data["Language"]} \n *imdb rating* : {data["imdbRating"]} \n *Seasons* : {data["totalSeasons"]}\n *Release* : {data["Released"]} \n *Duration* : {data["Runtime"]} \n *Genre* : {data["Genre"]} \n *Actors* : {data["Actors"]} \n *Plot* : {data["Plot"]}'
            pic=data["Poster"]
        else:
            quote = 'try later.'
        msg.body(quote)
        msg.media(pic)
        responded = True
    if 'news about' in incoming_msg:
        # return a quote
        sen,news =incoming_msg.split('news about ')
        url="http://newsapi.org/v2/top-headlines?q="+news+"&apiKey=c9aa0e9bf8c0499e9831099e38577e4a"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            quote = f' *Title* : {data["articles"][0]["title"]} \n *Description* : {data["articles"][0]["description"]} \n *Content* : {data["articles"][0]["content"]} \n *Link* : {data["articles"][0]["url"]} '    
        else:
            quote = 'try later.'
        msg.body(quote)
        responded = True
    if 'headlines' in incoming_msg:
        # return a quote
        r = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=c9aa0e9bf8c0499e9831099e38577e4a')
        if r.status_code == 200:
            data = r.json()
            quote = f' *Title* : {data["articles"][0]["title"]} \n *Description* : {data["articles"][0]["description"]} \n *Content* : {data["articles"][0]["content"]} \n *Link* : {data["articles"][0]["url"]} \n \n *Title* : {data["articles"][1]["title"]} \n *Description* : {data["articles"][1]["description"]} \n *Content* : {data["articles"][1]["content"]} \n *Link* : {data["articles"][1]["url"]}'
        else:
            quote = 'try later.'
        msg.body(quote)
        responded = True 
    if 'of india' in incoming_msg:
        # return a quote
        r = requests.get('https://api.covid19india.org/data.json')
        if r.status_code == 200:
            data = r.json()
            quote = f' Active cases : *{data["statewise"][0]["active"]}* \n Recovered case : *{data["statewise"][0]["recovered"]}* \n Deaths : *{data["statewise"][0]["deaths"]}*'
        else:
            quote = 'try later.'
        msg.body(quote)
        responded = True
    if 'in tn' in incoming_msg:
        # return a quote
        r = requests.get('https://api.covid19india.org/data.json')
        if r.status_code == 200:
            data = r.json()
            quote = f' Active cases : *{data["statewise"][4]["active"]}* \n Recovered case : *{data["statewise"][4]["recovered"]}* \n Deaths : *{data["statewise"][4]["deaths"]}*'
        else:
            quote = 'try later.'
        msg.body(quote)
        responded = True
    if 'pokemon' in incoming_msg:
        # return a quote
        sen,fruit =incoming_msg.split('pokemon ')
        url="https://pokeapi.co/api/v2/pokemon/"+fruit
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            urlpc = data["sprites"]["other"]["official-artwork"]["front_default"]
            quote = f' *Pokedex ID :* {data["id"]} \n *Name :* {data["name"]} \n *Height :* {data["height"]} \n *Weight :* {data["weight"]} \n *Type :* {data["types"][0]["type"]["name"]}\n *Moves :* {data["moves"][0]["move"]["name"]}, {data["moves"][1]["move"]["name"]}, {data["moves"][2]["move"]["name"]}, {data["moves"][4]["move"]["name"]}'
        else:
            quote = 'I could not retrieve a shannon sharpe quotes at this time, sorry.'
        msg.body(quote)
        msg.media(urlpc)
        responded = True         
    if 'rates' in incoming_msg:
        r = requests.get("https://api.ratesapi.io/api/latest")
        if r.status_code == 200:
            data = r.json()
            quote = f' Currency rates :\n 1 EURO = {data["rates"]["INR"]} INR \n 1 DOLLAR = 73.92 INR'
        else:
            quote = 'I could not retrieve a shannon sharpe quotes at this time, sorry.'
        msg.body(quote)
        responded = True   
    if 'advice' in incoming_msg:
        # return a quote
        r = requests.get('https://api.adviceslip.com/advice')
        if r.status_code == 200:
            data = r.json()
            quote = f'A free advice : {data["slip"]["advice"]}'
        else:
            quote = 'try later.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if 'meme' in incoming_msg:
        # return a quote
        sen,meme =incoming_msg.split('meme ')
        name,gender=meme.split(',')
        x = name.replace(" ", "%20")
        url_p="https://belikebill.ga/billgen-API.php?default=1&name="+x+"&sex="+gender
        msg.media(url_p)
        responded = True   
    if not responded:
        msg.body('I am learning and growing day by day \n- Be_A_Nerd bot:)')
    return str(resp)


if __name__ == '__main__':
    app.run()

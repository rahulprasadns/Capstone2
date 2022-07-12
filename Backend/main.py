from flask import Flask
from flask_socketio import SocketIO, send


# from future.standard_library import install_aliases
# install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os


from flask import request
from flask import make_response
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketIo = SocketIO(app, cors_allowed_origins="*")

app.debug = True

app.host = 'localhost'

@socketIo.on('message')
def handleMessage(msg):
    print(msg)
    send(msg, broadcast=True)
    return None


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    # commented out by Naresh
    res = static_reply(req)

    res = json.dumps(res, indent=4)

    r = make_response(res)


    r.headers['Content-Type'] = 'application/json'

    return r


def processRequest(req):

    if req.get("queryResult").get("action") != "rate":
        print("Please check your action name in DialogFlow...")
        return {}

    result = req.get("queryResult")
    parameters = result.get("parameters")



    print (parameters['currency-name1'])
    currency1 = parameters['currency-name']
    currency2 = parameters['currency-name1']
    baseurl = 'https://api.exchangeratesapi.io/latest?base=' + currency1 + '&symbols=' + currency2;




    if baseurl is None:
        return {}

    result = urlopen(baseurl).read()
    data = json.loads(result)
    # for some the line above gives an error and hence decoding to utf-8 might help
    # data = json.loads(result.decode('utf-8'))
    res = makeWebhookResult(data,currency2)
    return res



def makeWebhookResult(data,currency2):
    query = data.get('rates')

    if query is None:
        return {}
    result = query.get(currency2)
    if result is None:
        return {}

    speech = "The exchange rate is  " + str(result)


    # Naresh
    return {

        "fulfillmentText": speech,
        "source": "Exchange rateapi"
    }


@app.route('/')
def home():
    return "Hello there my friend !!"


@app.route('/static_reply', methods=['POST'])
def static_reply(req):
    print(req)
    #if req.get("queryResult").get("action") != "Brazil-custom":
    #  print("Please check your action name in DialogFlow...")
    #   return {}

    result = req.get("queryResult")
    print(result)
    parameters = result.get("parameters")
    print (parameters['Airline_Brazil'])
    string = "You are awesome testing !!"
    Message = "this is the message"
    req = request.get_json(force=True)
    airline_brazil = req['queryResult']['parameters'].get('Airline_Brazil')
    hotel_brazil = req['queryResult']['parameters'].get('Hotel_Brazil')
    meal_brazil = req['queryResult']['parameters'].get('Meal_Brazil')
    my_result = {

        "fulfillmentText": string,
        "source": string
    }

    res = json.dumps(my_result, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def customize():
    req = request.get_json(force=True)
    text = req['queryResult']['parameters'].get('Airline_Brazil')
    source_lang = req['queryResult']['parameters'].get('Hotel_Brazil')
    target_lang = req['queryResult']['parameters'].get('Meal_Brazil')
    # const airline_brazil=agent.parameters.Airline_Brazil;
    # const hotel_brazil=agent.parameters.Hotel_Brazil;
    # const meal_brazil=agent.parameters.Meal_Brazil;
    # const sightseeing_brazil=agent.parameters.Sight_Brazil;
	# var price_airline, price_hotel ,price_meal, price_sight;

    # if(airline_brazil=='Air Canada'){
    #    price_airline=4000;
    # }
    # else
    # {
    # 	price_airline=2700;
    # }
    # if (hotel_brazil=='Copacabana Palace')
    # {
    #     price_hotel=2500;
    # }
    # else 
    # {
    #     price_hotel=900;
    # }
    #    if (meal_brazil=='breakfast and dinner')
    # {
    #     price_meal=360;
    # }
    # else if (meal_brazil=='breakfast')
    # {
    #    price_meal=180;
    # }
    #    else if (meal_brazil=='dinner')
    # {
    #    price_meal=180;
    # }
    #    else if (meal_brazil=='none')
    # {
    #    price_meal=0;
    # }
    # if (sightseeing_brazil=='Corcovado')
    # { 
    #   	 price_sight=100;
    # }
    # else if (sightseeing_brazil=='Pão de Açúcar')
    # {
    #   	 price_sight=100;
    # }
    #  else if (sightseeing_brazil=='Both')
    # {
    #      price_sight=200;
    # }
    #  else if (sightseeing_brazil=='One')
    # { 
    #    price_sight=100;
    # }
    # else if (sightseeing_brazil=='None')
    # {
    #     price_sight=100;
    # }
    # var total=price_airline + price_hotel + price_meal + price_sight;
    # agent.add(`The total amount is $`, total);
   
  #}

if __name__ == '__main__':
    socketIo.run(app)

from glob import glob
from flask import Flask, request
from flask_socketio import SocketIO, send


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

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ''
    price_meal=-1
    price_airline=0
    price_hotel=0
    price_sight=-1
    price=0
    discount_price=0
    strz=""
    option1=""
    option2=""
    option3=""
    options=""
    optionselected=""
    query_result = req.get('queryResult')
    if query_result.get('action') == 'Pre-customize.Pre-customize-custom-2.Brazil-custom':
        airline_brazil = req['queryResult']['parameters'].get('Airline_Brazil')
        print(airline_brazil)
        hotel_brazil = req['queryResult']['parameters'].get('Hotel_Brazil')
        print(hotel_brazil)
        if airline_brazil=="Air Canada":
            price_airline=4000;
        else:
            price_airline=2700;
        
        print (price_airline)
       
    
        if hotel_brazil=="Copacabana Palace":
            price_hotel=2500;
     
        elif hotel_brazil=="4 stars" or hotel_brazil=="Windsor Barra":
            price_hotel=900;  
         
        print(price_hotel)
        meal_brazil = req['queryResult']['parameters'].get('meals')
        print(meal_brazil)
        if meal_brazil=="Breakfast" or meal_brazil=="breakfast":
            price_meal=180;
        elif meal_brazil=="Breakfast and Dinner" or meal_brazil=="breakfast and dinner":
            price_meal=360;
        elif meal_brazil=="Dinner":
            price_meal=180;      
        elif meal_brazil=="None":
            price_meal=0;
          
        print (price_meal)

        sightseeing_brazil= req['queryResult']['parameters'].get('Sight_Brazil')
        print(sightseeing_brazil)
        if sightseeing_brazil=='Corcovado':
            price_sight=100;  
        elif sightseeing_brazil=="Pão de Açúcar":
            price_sight=100;
        elif sightseeing_brazil=="Both":
            price_sight=200; 
        elif sightseeing_brazil=="One":
            price_sight=100;
        elif sightseeing_brazil=="None":
            price_sight=0;
        print(price_sight)

        if price_airline>0 and price_hotel>0  and price_meal >-1 and price_sight>-1:
             price=price_airline + price_hotel + price_meal + price_sight;
             discount_price=price-(0.05*price)
            
             strz = ("Ready! This is the summary and the price of your personalized travel package:"+"\n\n"+
                "Country: Brazil " +"\n"+
                "Airline: " + airline_brazil + "\n" +
                "Hotel: " + hotel_brazil + "\n" +
                "Meals incuded: " + meal_brazil +"\n"+
                "Sighseeings included: " + sightseeing_brazil + "\n\n"+
                "Total price: CA$" + str(price) + "\n"+
                "Total price with discount: CA$ "+ str(discount_price) + "\n\n" +
                "Can we confirm your package?")

        fulfillmentText = strz
    if query_result.get('action') == 'Albania-test.Albania-test-custom':
        airline_albania = req['queryResult']['parameters'].get('Airline_Albania')
        print(airline_albania)
        hotel_albania = req['queryResult']['parameters'].get('Hotel_Albania')
        print(hotel_albania)
        if airline_albania=="Air Canada":
            price_airline=5500;
        else:
            price_airline=3500;
        
        print (price_airline)
       
    
        if hotel_albania=="Maritim Hotel Plaza Tirana":
            price_hotel=2800;
     
        elif hotel_albania=="4 stars" or hotel_albania=="Tirana International Hotel and Conference Centre":
            price_hotel=1000;  
         
        print(price_hotel)
        meal_albania = req['queryResult']['parameters'].get('meals')
        print(meal_albania)
        if meal_albania=="Breakfast" or meal_albania=="breakfast":
            price_meal=180;
        elif meal_albania=="Breakfast and Dinner" or meal_albania=="breakfast and dinner":
            price_meal=360;
        elif meal_albania=="Dinner":
            price_meal=180;      
        elif meal_albania=="None":
            price_meal=0;
          
        print (price_meal)

        sightseeing_albania= req['queryResult']['parameters'].get('Sight_Albania')
        print(sightseeing_albania)
        if sightseeing_albania=="Shala River":
            price_sight=100;  
        elif sightseeing_albania=="Lake Bovilla":
            price_sight=100;
        elif sightseeing_albania=="Shala River and Lake Bovilla" or sightseeing_albania=="Both":
            price_sight=200; 
        elif sightseeing_albania=="One":
            price_sight=100;
        elif sightseeing_albania=="None":
            price_sight=0;
        print(price_sight)

        if price_airline>0 and price_hotel>0  and price_meal >-1 and price_sight>-1:
             price=price_airline + price_hotel + price_meal + price_sight;
             discount_price=price-(0.05*price)
            
             strz = ("Ready! This is the summary and the price of your personalized travel package:"+"\n\n"+
                "Country: ALbania " +"\n"+
                "Airline: " + airline_albania + "\n" +
                "Hotel: " + hotel_albania + "\n" +
                "Meals incuded: " + meal_albania +"\n"+
                "Sighseeings included: " + sightseeing_albania + "\n\n"+
                "Total price: CA$" + str(price) + "\n"+
                "Total price with discount: CA$ "+ str(discount_price) + "\n\n" +
                "Can we confirm your package?")

        fulfillmentText = strz
    if query_result.get('action') == 'Pre-customize.Pre-customize-custom.India-custom':
        airline_india = req['queryResult']['parameters'].get('Airline_India')
        print(airline_india)
        hotel_india = req['queryResult']['parameters'].get('Hotel_India')
        print(hotel_india)
        if airline_india=="Air India":
            price_airline=6500;
        elif airline_india=="United Airlines":
            price_airline=5200;
        
        print (price_airline)
       
    
        if hotel_india=="Taj Palace":
            price_hotel=3000;
     
        elif hotel_india=="4 stars" or hotel_india=="Novotel New Delhi Aerocity":
            price_hotel=1000;  
         
        print(price_hotel)
        meal_india = req['queryResult']['parameters'].get('meals')
        print(meal_india)
        if meal_india=="Breakfast" or meal_india=="breakfast":
            price_meal=180;
        elif meal_india=="Breakfast and Dinner" or meal_india=="breakfast and dinner":
            price_meal=360;
        elif meal_india=="Dinner":
            price_meal=180;      
        elif meal_india=="None":
            price_meal=0;
          
        print (price_meal)

        sightseeing_india= req['queryResult']['parameters'].get('sight_india')
        print(sightseeing_india)
        
        if  sightseeing_india=='Taj Mahal':
            price_sight=100;  
        elif sightseeing_india=="Gandhi Smrit":
            price_sight=100;
        elif sightseeing_india=="Taj Mahal and Gandhi Smrit" or sightseeing_india=="Both":
            price_sight=200; 
        elif sightseeing_india=="One":
            price_sight=100;
        elif sightseeing_india=="None":
            price_sight=0;
        print(price_sight)

        if price_airline>0 and price_hotel>0  and price_meal >-1 and price_sight>-1:
             price=price_airline + price_hotel + price_meal + price_sight;
             discount_price=price-(0.05*price)
            
             strz = ("Ready! This is the summary and the price of your personalized travel package:"+"\n\n"+
                "Country: India " +"\n"+
                "Airline: " + airline_india + "\n" +
                "Hotel: " + hotel_india + "\n" +
                "Meals incuded: " + meal_india +"\n"+
                "Sighseeings included: " + sightseeing_india + "\n\n"+
                "Total price: CA$" + str(price) + "\n"+
                "Total price with discount: CA$ "+ str(discount_price) + "\n\n" +
                "Can we confirm your package?")
        fulfillmentText = strz   
    if query_result.get('action') == 'Budget.Budget-custom':
        amount = req['queryResult']['parameters'].get('amount')
        amount=int(amount)
        print(amount)
        
        if amount>3000 and amount<=4000:
            
            option1 = ("**OPTION 1)** " +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Latam Airlines"+"\n" +
            "Hotel: Windsor Barra " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ 3600" + "\n")
            option2 = ("**OPTION 2)**" +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Latam Airlines"+"\n" +
            "Hotel: Windsor Barra " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: Corcovado and Pão de Açúcar" + "\n\n"+
            "Total price: CA$ 3800" + "\n")
            option3 = ("**OPTION 3)**" +" \n "+
            "Country: Brazil " +" \n "+
            "Airline: Latam Airlines"+" \n " +
            "Hotel: Windsor Barra " + " \n " +
            "Meals incuded: Breakfast and Dinner"  +" \n "+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ 3980" + " \n")
        elif amount>4000 and amount<=5000:
            option1 = ("**OPTION 1)** " +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Latam Airlines"+"\n" +
            "Hotel: Windsor Barra " + "\n" +
            "Meals incuded: Breakfast and Dinner"  +"\n"+
            "Sighseeings included: Corcovado" + "\n\n"+
            "Total price: CA$ 4060" + "\n")
            option2 = ("**OPTION 2)**" +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Latam Airlines"+"\n" +
            "Hotel: Windsor Barra " + "\n" +
            "Meals incuded: Breakfast and Dinner"  +"\n"+
            "Sighseeings included: Corcovado and Pão de Açúcar" + "\n\n"+
            "Total price: CA$ 4160" + "\n")
            option3 = ("**OPTION 3)**" +" \n "+
            "Country: Brazil " +" \n "+
            "Airline: Air Canada"+" \n " +
            "Hotel: Windsor Barra " + " \n " +
            "Meals incuded: None"  +" \n "+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ 4900" + " \n")
        elif amount>5000 and amount<=6000:
            option1 = ("**OPTION 1)** " +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Air Canada"+"\n" +
            "Hotel: Windsor Barra " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: Corcovado" + "\n\n"+
            "Total price: CA$ 5000" + "\n")
            option2 = ("**OPTION 2)**" +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Latam Airlines"+"\n" +
            "Hotel: Copacabana Palace" + "\n" +
            "Meals incuded: Breakfast"  +"\n"+
            "Sighseeings included:  Corcovado" + "\n\n"+
            "Total price: CA$ 5480" + "\n")
            option3 = ("**OPTION 3)**" +" \n "+
            "Country: Brazil " +" \n "+
            "Airline: Latam Airlines"+" \n " +
            "Hotel: Copacabana Palace " + " \n " +
            "Meals incuded: Breakfast and Dinner"  +" \n "+
            "Sighseeings included: Corcovado and Pão de Açúcar" + "\n\n"+
            "Total price: CA$ 5760" + " \n")
        elif amount>6000 and amount<=7000:
            option1 = ("**OPTION 1)** " +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Air Canada"+"\n" +
            "Hotel: Copacabana Palace " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ 6500" + "\n")
            option2 = ("**OPTION 2)**" +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Air Canada"+"\n" +
            "Hotel: Copacabana Palace" + "\n" +
            "Meals incuded: Breakfast"  +"\n"+
            "Sighseeings included:  Corcovado" + "\n\n"+
            "Total price: CA$ 6780" + "\n")
            option3 = ("**OPTION 3)**" +" \n "+
            "Country: Brazil " +" \n "+
            "Airline: Air Canada"+" \n " +
            "Hotel: Copacabana Palace " + " \n " +
            "Meals incuded: Breakfast and Dinner"  +" \n "+
            "Sighseeings included: Corcovado" + "\n\n"+
            "Total price: CA$ 6960" + " \n")
        elif amount>7000 and amount<=8000:
            option1 = ("**OPTION 1)** " +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Air Canada"+"\n" +
            "Hotel: Copacabana Palace " + "\n" +
            "Meals incuded: Breakfast and Dinner"  +"\n"+
            "Sighseeings included: Corcovado and Pão de Açúcar" + "\n\n"+
            "Total price: CA$ 7060" + "\n"+
            "Would you like to select this option? ")
        elif amount<3000 and amount>=500:
             option1 = (" The amount must be greater than 3000! Please enter a new value...")
            
        options=("Please choose the best option for you and tell me \n"+ option1 +"\n"+ option2 +"\n"+ option3)
        fulfillmentText=options
    if query_result.get('action') == 'Budget.Budget-custom.Budget-custom-custom':
        budgetOptions = req['queryResult']['parameters'].get('budget_options')
        print(budgetOptions)
        print (option1)
        if budgetOptions=="Option 1":
            optionselected="You selected OPTION 1. Can we confirm?"
        elif budgetOptions=="Option 2":
            optionselected="You selected OPTION 2. Can we confirm?"
        elif budgetOptions=="Option 3": 
             optionselected="You selected OPTION 3. Can we confirm?"
            

        fulfillmentText=optionselected
    return {
            "fulfillmentText": fulfillmentText,
            "source": "webhookdata"
        }

if __name__ == '__main__':
    socketIo.run(app)
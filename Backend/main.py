from calendar import c
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
    option4=""
    option5=""
    option6=""
    option7=""
    option8=""
    option9=""
    options=""
    optionselected=""
    mes_dis1=""
    mes_dis2=""
    mes_dis3=""
    mes_dis4=""
    mes_dis5=""
    mes_dis6=""
    mes_dis7=""
    mes_dis8=""
    mes_dis9=""
    price1=0
    price2=0
    price3=0
    price4=0
    price5=0
    price6=0
    price7=0
    price8=0
    price9=0
    discount_price1=0
    discount_price2=0
    discount_price3=0
    discount_price4=0
    discount_price5=0
    discount_price6=0
    discount_price7=0
    discount_price8=0
    discount_price9=0
    query_result = req.get('queryResult')  
    # action Customize and change for Loyal customer or the action for a regular customer( Brazil) 
    if query_result.get('action') == 'LoyaltyX.LoyaltyX-custom-2.Customize_X-custom-3.BrazilX-custom' or query_result.get('action') == 'Pre-customize.Pre-customize-custom-2.Brazil-custom' or query_result.get('action') =='LoyaltyX.LoyaltyX-custom.Change_X-custom.BrasilChangeX-custom':
        airline_brazil = req['queryResult']['parameters'].get('airline_brazil')
        print(airline_brazil)
        hotel_brazil = req['queryResult']['parameters'].get('hotel_brazil')
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

        sightseeing_brazil= req['queryResult']['parameters'].get('sight_brazil')
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
                
             if query_result.get('action') == 'LoyaltyX.LoyaltyX-custom-2.Customize_X-custom-3.BrazilX-custom':   
                
                strz = ("Ready! This is the summary and the price of your personalized travel package:"+"\n\n"+
                "Country: Brazil " +"\n"+
                "Airline: " + airline_brazil + "\n" +
                "Hotel: " + hotel_brazil + "\n" +
                "Meals incuded: " + meal_brazil +"\n"+
                "Sighseeings included: " + sightseeing_brazil + "\n\n"+
                "Total price: CA$" + str(price) + "\n"+
                "Total price with discount: CA$ "+ str(discount_price) + "\n\n" +
                "Can we confirm your package?")
             elif query_result.get('action') == 'Pre-customize.Pre-customize-custom-2.Brazil-custom':
                strz = ("Ready! This is the summary and the price of your personalized travel package:"+"\n\n"+
                "Country: Brazil " +"\n"+
                "Airline: " + airline_brazil + "\n" +
                "Hotel: " + hotel_brazil + "\n" +
                "Meals incuded: " + meal_brazil +"\n"+
                "Sighseeings included: " + sightseeing_brazil + "\n\n"+
                "Total price: CA$" + str(price) + "\n"+
                "Can we confirm your package?")
             elif query_result.get('action') == 'LoyaltyX.LoyaltyX-custom.Change_X-custom.BrasilChangeX-custom':
                strz = ("Ready! This is the summary and the price of your changed travel package:"+"\n\n"+
                "Country: Brazil " +"\n"+
                "Airline: " + airline_brazil + "\n" +
                "Hotel: " + hotel_brazil + "\n" +
                "Meals incuded: " + meal_brazil +"\n"+
                "Sighseeings included: " + sightseeing_brazil + "\n\n"+
                "Total price: CA$" + str(price) + "\n"+
                "Total price with discount: CA$ "+ str(discount_price) + "\n\n" +
                "Can we confirm your package?")
                    
        fulfillmentText = strz

    # action Customize and change for Loyal customer or the action for a regular customer( Albania) 
    if query_result.get('action') == 'LoyaltyX.LoyaltyX-custom-2.Customize_X-custom-2.AlbaniaX-custom' or query_result.get('action') == 'Albania-test.Albania-test-custom' or query_result.get('action') =='LoyaltyX.LoyaltyX-custom.Change_X-custom-3.Albania_X-custom':
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
        meal_albania = req['queryResult']['parameters'].get('Meals')
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
                
             if  query_result.get('action') == 'LoyaltyX.LoyaltyX-custom-2.Customize_X-custom-2.AlbaniaX-custom':
               
                strz = ("Ready! This is the summary and the price of your personalized travel package:"+"\n\n"+
                    "Country: Albania " +"\n"+
                    "Airline: " + airline_albania + "\n" +
                    "Hotel: " + hotel_albania + "\n" +
                    "Meals incuded: " + meal_albania +"\n"+
                    "Sighseeings included: " + sightseeing_albania + "\n\n"+
                    "Total price: CA$" + str(price) + "\n"+
                    "Total price with discount: CA$ "+ str(discount_price) + "\n\n" +
                    "Can we confirm your package?")
             elif query_result.get('action')=='Albania-test.Albania-test-custom':
                strz = ("Ready! This is the summary and the price of your personalized travel package:"+"\n\n"+
                    "Country: Albania " +"\n"+
                    "Airline: " + airline_albania + "\n" +
                    "Hotel: " + hotel_albania + "\n" +
                    "Meals incuded: " + meal_albania +"\n"+
                    "Sighseeings included: " + sightseeing_albania + "\n\n"+
                    "Total price: CA$" + str(price) + "\n"+
                    "Can we confirm your package?")
             elif query_result.get('action')=='LoyaltyX.LoyaltyX-custom.Change_X-custom-3.Albania_X-custom':
                    strz = ("Ready! This is the summary and the price of your changed travel package:"+"\n\n"+
                    "Country: Albania " +"\n"+
                    "Airline: " + airline_albania + "\n" +
                    "Hotel: " + hotel_albania + "\n" +
                    "Meals incuded: " + meal_albania +"\n"+
                    "Sighseeings included: " + sightseeing_albania + "\n\n"+
                    "Total price: CA$" + str(price) + "\n"+
                    "Total price with discount: CA$ "+ str(discount_price) + "\n\n" 
                    "Can we confirm your package?")

        fulfillmentText = strz
        
    # action Customize and change for Loyal customer or the action for a regular customer( India) 
    if query_result.get('action') == 'Pre-customize.Pre-customize-custom.India-custom' or query_result.get('action') =='LoyaltyX.LoyaltyX-custom-2.Customize_X-custom.IndiaX-custom' or query_result.get('action') =='LoyaltyX.LoyaltyX-custom.Change_X-custom-2.India_X-custom':
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

        sightseeing_india= req['queryResult']['parameters'].get('Sight_India')
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
             if query_result.get('action') =='LoyaltyX.LoyaltyX-custom-2.Customize_X-custom.IndiaX-custom':
            
                strz = ("Ready! This is the summary and the price of your personalized travel package:"+"\n\n"+
                    "Country: India " +"\n"+
                    "Airline: " + airline_india + "\n" +
                    "Hotel: " + hotel_india + "\n" +
                    "Meals incuded: " + meal_india +"\n"+
                    "Sighseeings included: " + sightseeing_india + "\n\n"+
                    "Total price: CA$" + str(price) + "\n"+
                    "Total price with discount: CA$ "+ str(discount_price) + "\n\n" +
                    "Can we confirm your package?")
             elif query_result.get('action') == 'Pre-customize.Pre-customize-custom.India-custom':
                strz = ("Ready! This is the summary and the price of your personalized travel package:"+"\n\n"+
                    "Country: India " +"\n"+
                    "Airline: " + airline_india + "\n" +
                    "Hotel: " + hotel_india + "\n" +
                    "Meals incuded: " + meal_india +"\n"+
                    "Sighseeings included: " + sightseeing_india + "\n\n"+
                    "Total price: CA$" + str(price) + "\n"+
                    "Can we confirm your package?")
             elif query_result.get('action') =='LoyaltyX.LoyaltyX-custom.Change_X-custom-2.India_X-custom':
                    strz = ("Ready! This is the summary and the price of your changed travel package:"+"\n\n"+
                    "Country: India " +"\n"+
                    "Airline: " + airline_india + "\n" +
                    "Hotel: " + hotel_india + "\n" +
                    "Meals incuded: " + meal_india +"\n"+
                    "Sighseeings included: " + sightseeing_india + "\n\n"+
                    "Total price: CA$" + str(price) + "\n"+
                    "Total price with discount: CA$ "+ str(discount_price) + "\n\n" +
                    "Can we confirm your package?")
                    
        fulfillmentText = strz   
    if query_result.get('action') == 'Budget.Budget-custom' or  query_result.get('action') =='LoyaltyX.LoyaltyX-custom.BudgetX-custom':
        amount = req['queryResult']['parameters'].get('amount')
        amount=int(amount)
        print(amount)
        
        if amount>3000 and amount<=4000:
            price1=3600
            price2=3800
            price3=3980
            if query_result.get('action') == 'LoyaltyX.LoyaltyX-custom.BudgetX-custom': 
                discount_price1=price1-(0.05*price1)
                discount_price2=price2-(0.05*price2)
                discount_price3=price3-(0.05*price3)
                mes_dis1="Total price with discount: CA$ "+ str(discount_price1) + "\n\n"
                mes_dis2="Total price with discount: CA$ "+ str(discount_price2) + "\n\n"
                mes_dis3="Total price with discount: CA$ "+ str(discount_price3) + "\n\n"

            option1 = ("**OPTION 1)** " +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Latam Airlines"+"\n" +
            "Hotel: Windsor Barra " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ "+ str(price1) + "\n"+
            mes_dis1)
            option2 = ("**OPTION 2)**" +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Latam Airlines"+"\n" +
            "Hotel: Windsor Barra " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: Corcovado and Pão de Açúcar" + "\n\n"+
            "Total price: CA$ " + str(price2) +"\n"+
            mes_dis2
            )
            option3 = ("**OPTION 3)**" +" \n "+
            "Country: Brazil " +" \n "+
            "Airline: Latam Airlines"+" \n " +
            "Hotel: Windsor Barra " + " \n " +
            "Meals incuded: Breakfast and Dinner"  +" \n "+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ " + str(price2) +"\n"+
            mes_dis3
            )
  
        elif amount>4000 and amount<=5000:
            price1=4060
            price2=4160
            price3=4900
            price4=4500
            price5=4700
            price6=4880
            if query_result.get('action') == 'LoyaltyX.LoyaltyX-custom.BudgetX-custom':  
                discount_price1=price1-(0.05*price1)
                discount_price2=price2-(0.05*price2)
                discount_price3=price3-(0.05*price3)
                discount_price4=price4-(0.05*price4)
                discount_price5=price5-(0.05*price5)
                discount_price6=price6-(0.05*price6)
                mes_dis1="Total price with discount: CA$ "+ str(discount_price1) + "\n\n"
                mes_dis2="Total price with discount: CA$ "+ str(discount_price2) + "\n\n"
                mes_dis3="Total price with discount: CA$ "+ str(discount_price3) + "\n\n"
                mes_dis4="Total price with discount: CA$ "+ str(discount_price4) + "\n\n"
                mes_dis5="Total price with discount: CA$ "+ str(discount_price5) + "\n\n"
                mes_dis6="Total price with discount: CA$ "+ str(discount_price6) + "\n\n"
            option1 = ("**OPTION 1)** " +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Latam Airlines"+"\n" +
            "Hotel: Windsor Barra " + "\n" +
            "Meals incuded: Breakfast and Dinner"  +"\n"+
            "Sighseeings included: Corcovado" + "\n\n"+
             "Total price: CA$ "+ str(price1) + "\n"+
            mes_dis1)
            option2 = ("**OPTION 2)**" +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Latam Airlines"+"\n" +
            "Hotel: Windsor Barra " + "\n" +
            "Meals incuded: Breakfast and Dinner"  +"\n"+
            "Sighseeings included: Corcovado and Pão de Açúcar" + "\n\n"+
            "Total price: CA$ "+ str(price2) + "\n"+
            mes_dis2)
            option3 = ("**OPTION 3)**" +" \n "+
            "Country: Brazil " +" \n "+
            "Airline: Air Canada"+" \n " +
            "Hotel: Windsor Barra " + " \n " +
            "Meals incuded: None"  +" \n "+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ "+ str(price3) + "\n"+
            mes_dis3)
            option4 = ("**OPTION 4)** " +"\n"+
            "Country: Albania " +"\n"+
            "Airline: Lufthansa"+"\n" +
            "Hotel: Tirana International Hotel and Conference Centre " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ "+ str(price4) + "\n"+
            mes_dis4)
            option5 = ("**OPTION 5)**" +"\n"+
            "Country: Albania " +"\n"+
            "Airline: Lufthansa"+"\n" +
            "Hotel: Tirana International Hotel and Conference Centre " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: Shala River and Lake Bovilla" + "\n\n"+
             "Total price: CA$ "+ str(price5) + "\n"+
            mes_dis5)
            option6 = ("**OPTION 6)**" +" \n "+
            "Country: Albania " +" \n "+
            "Airline: Lufthansa"+" \n " +
            "Hotel: Tirana International Hotel and Conference Centre " + " \n " +
            "Meals incuded: Breakfast"  +" \n "+
            "Sighseeings included: Shala River and Lake Bovilla" + "\n\n"+
            "Total price: CA$ "+ str(price6) + "\n"+
            mes_dis6)
        elif amount>5000 and amount<=6000:
            price1=5000
            price2=5480
            price3=5760
            price4=5060
            if query_result.get('action') == 'LoyaltyX.LoyaltyX-custom.BudgetX-custom':    
                discount_price1=price1-(0.05*price1)
                discount_price2=price2-(0.05*price2)
                discount_price3=price3-(0.05*price3)
                discount_price4=price4-(0.05*price4)
                mes_dis1="Total price with discount: CA$ "+ str(discount_price1) + "\n\n"
                mes_dis2="Total price with discount: CA$ "+ str(discount_price2) + "\n\n"
                mes_dis3="Total price with discount: CA$ "+ str(discount_price3) + "\n\n"
                mes_dis4="Total price with discount: CA$ "+ str(discount_price4) + "\n\n"
            option1 = ("**OPTION 1)** " +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Air Canada"+"\n" +
            "Hotel: Windsor Barra " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: Corcovado" + "\n\n"+
            "Total price: CA$ "+ str(price1) + "\n"+
            mes_dis1)
            option2 = ("**OPTION 2)**" +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Latam Airlines"+"\n" +
            "Hotel: Copacabana Palace" + "\n" +
            "Meals incuded: Breakfast"  +"\n"+
            "Sighseeings included:  Corcovado" + "\n\n"+
            "Total price: CA$ "+ str(price2) + "\n"+
            mes_dis2)
            option3 = ("**OPTION 3)**" +" \n "+
            "Country: Brazil " +" \n "+
            "Airline: Latam Airlines"+" \n " +
            "Hotel: Copacabana Palace " + " \n " +
            "Meals incuded: Breakfast and Dinner"  +" \n "+
            "Sighseeings included: Corcovado and Pão de Açúcar" + "\n\n"+
            "Total price: CA$ "+ str(price3) + "\n"+
            mes_dis3)
            option4 = ("**OPTION 4)**" +" \n "+
            "Country: Albania " +" \n "+
            "Airline: Lufthansa"+" \n " +
            "Hotel: Tirana International Hotel and Conference Centre " + " \n " +
            "Meals incuded: Breakfast and dinner"  +" \n "+
            "Sighseeings included: Shala River and Lake Bovilla" + "\n\n"+
            "Total price: CA$ "+ str(price4) + "\n"+
            mes_dis4)
        elif amount>6000 and amount<=7000:
            price1=6500
            price2=6780
            price3=6960
            price4=6500
            price5=6700
            price6=6880
            price7=6200
            price8=6560
            price9=6760
            if query_result.get('action') == 'LoyaltyX.LoyaltyX-custom.BudgetX-custom':  
                discount_price1=price1-(0.05*price1)
                discount_price2=price2-(0.05*price2)
                discount_price3=price3-(0.05*price3)
                discount_price4=price4-(0.05*price4)
                discount_price5=price5-(0.05*price5)
                discount_price6=price6-(0.05*price6)
                discount_price7=price7-(0.05*price7)
                discount_price8=price8-(0.05*price8)
                discount_price9=price9-(0.05*price9)
                mes_dis1="Total price with discount: CA$ "+ str(discount_price1) + "\n\n"
                mes_dis2="Total price with discount: CA$ "+ str(discount_price2) + "\n\n"
                mes_dis3="Total price with discount: CA$ "+ str(discount_price3) + "\n\n"
                mes_dis4="Total price with discount: CA$ "+ str(discount_price4) + "\n\n"
                mes_dis5="Total price with discount: CA$ "+ str(discount_price5) + "\n\n"
                mes_dis6="Total price with discount: CA$ "+ str(discount_price6) + "\n\n"
                mes_dis7="Total price with discount: CA$ "+ str(discount_price7) + "\n\n"
                mes_dis8="Total price with discount: CA$ "+ str(discount_price8) + "\n\n"
                mes_dis9="Total price with discount: CA$ "+ str(discount_price9) + "\n\n"
            option1 = ("**OPTION 1)** " +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Air Canada"+"\n" +
            "Hotel: Copacabana Palace " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ "+ str(price1) + "\n"+
            mes_dis1)
            option2 = ("**OPTION 2)**" +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Air Canada"+"\n" +
            "Hotel: Copacabana Palace" + "\n" +
            "Meals incuded: Breakfast"  +"\n"+
            "Sighseeings included:  Corcovado" + "\n\n"+
            "Total price: CA$ "+ str(price2) + "\n"+
            mes_dis2)
            option3 = ("**OPTION 3)**" +" \n "+
            "Country: Brazil " +" \n "+
            "Airline: Air Canada"+" \n " +
            "Hotel: Copacabana Palace " + " \n " +
            "Meals incuded: Breakfast and Dinner"  +" \n "+
            "Sighseeings included: Corcovado" + "\n\n"+
            "Total price: CA$ "+ str(price3) + "\n"+
            mes_dis3)
            option4 = ("**OPTION 4)** " +"\n"+
            "Country: Albania " +"\n"+
            "Airline: Air Canada"+"\n" +
            "Hotel: Tirana International Hotel and Conference Centre " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ "+ str(price4) + "\n"+
            mes_dis4)
            option5 = ("**OPTION 5)**" +"\n"+
            "Country: Albania " +"\n"+
            "Airline: Air Canada"+"\n" +
            "Hotel: Tirana International Hotel and Conference Centre " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: Shala River and Lake Bovilla" + "\n\n"+
            "Total price: CA$ "+ str(price5) + "\n"+
            mes_dis5)
            option6 = ("**OPTION 6)**" +" \n "+
            "Country: Albania " +" \n "+
            "Airline: Air Canada"+" \n " +
            "Hotel: Tirana International Hotel and Conference Centre " + " \n " +
            "Meals incuded: Breakfast"  +" \n "+
            "Sighseeings included: Shala River and Lake Bovilla" + "\n\n"+
            "Total price: CA$ "+ str(price6) + "\n"+
            mes_dis6)
            option7 = ("**OPTION 7)** " +"\n"+
            "Country: India " +"\n"+
            "Airline: United Airlines"+"\n" +
            "Hotel: Novotel New Delhi Aerocity " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ "+ str(price7) + "\n"+
            mes_dis7)
            option8 = ("**OPTION 8)**" +"\n"+
            "Country: India " +"\n"+
            "Airline: United Airlines"+"\n" +
            "Hotel: Novotel New Delhi Aerocity " + "\n" +
            "Meals incuded: Breakfast and dinner"  +"\n"+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ "+ str(price8) + "\n"+
            mes_dis8)
            option9 = ("**OPTION 9)**" +" \n "+
            "Country: India " +" \n "+
            "Airline: United Airlines"+" \n " +
            "Hotel: Novotel New Delhi Aerocity " + " \n " +
            "Meals incuded: Breakfast and dinner"  +" \n "+
            "Sighseeings included: Taj Mahal and Gandhi Smriti" + "\n\n"+
            "Total price: CA$ "+ str(price9) + "\n"+
            mes_dis9)
        elif amount>7000 and amount<=8000:
            price1=7060
            price2=7160
            price3=7500
            price4=7700
            price5=7960
            if query_result.get('action') == 'LoyaltyX.LoyaltyX-custom.BudgetX-custom':         
                discount_price1=price1-(0.05*price1)
                discount_price2=price2-(0.05*price2)
                discount_price3=price3-(0.05*price3)
                discount_price4=price4-(0.05*price4)
                discount_price5=price5-(0.05*price5)
                mes_dis1="Total price with discount: CA$ "+ str(discount_price1) + "\n\n"
                mes_dis2="Total price with discount: CA$ "+ str(discount_price2) + "\n\n"
                mes_dis3="Total price with discount: CA$ "+ str(discount_price3) + "\n\n"
                mes_dis4="Total price with discount: CA$ "+ str(discount_price4) + "\n\n"
                mes_dis5="Total price with discount: CA$ "+ str(discount_price5) + "\n\n"
            option1 = ("**OPTION 1)** " +"\n"+
            "Country: Brazil " +"\n"+
            "Airline: Air Canada"+"\n" +
            "Hotel: Copacabana Palace " + "\n" +
            "Meals incuded: Breakfast and Dinner"  +"\n"+
            "Sighseeings included: Corcovado and Pão de Açúcar" + "\n\n"+
             "Total price: CA$ "+ str(price1) + "\n"+
            mes_dis1)
            option2 = ("**OPTION 2)**" +" \n "+
            "Country: Albania " +" \n "+
            "Airline: Air Canada"+" \n " +
            "Hotel: Tirana International Hotel and Conference Centre " + " \n " +
            "Meals incuded: Breakfast and dinner"  +" \n "+
            "Sighseeings included: Shala River and Lake Bovilla" + "\n\n"+
            "Total price: CA$ "+ str(price2) + "\n"+
            mes_dis2)
            option3= ("**OPTION 3)** " +"\n"+
            "Country: India " +"\n"+
            "Airline: Air India"+"\n" +
            "Hotel: Novotel New Delhi Aerocity " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ "+ str(price3) + "\n"+
            mes_dis3)
            option4 = ("**OPTION 4)**" +"\n"+
            "Country: India " +"\n"+
            "Airline: Air India"+"\n" +
            "Hotel: Novotel New Delhi Aerocity " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: Taj Mahal and Gandhi Smriti" + "\n\n"+
            "Total price: CA$ "+ str(price4) + "\n"+
            mes_dis4)
            option5 = ("**OPTION 5)**" +" \n "+
            "Country: India " +" \n "+
            "Airline: Air India"+" \n " +
            "Hotel: Novotel New Delhi Aerocity " + " \n " +
            "Meals incuded: Breakfast and dinner"  +" \n "+
            "Sighseeings included: Taj Mahal" + "\n\n"+
            "Total price: CA$ "+ str(price5) + "\n"+
            mes_dis5)
        elif amount>8000 and amount<=9000:
            price1=8300
            price2=8580
            price3=8180
            price4=8060
            price5=8580
            price6=8760
            if query_result.get('action') == 'LoyaltyX.LoyaltyX-custom.BudgetX-custom':    
                discount_price1=price1-(0.05*price1)
                discount_price2=price2-(0.05*price2)
                discount_price3=price3-(0.05*price3)
                discount_price4=price4-(0.05*price4)
                discount_price5=price5-(0.05*price5)
                discount_price6=price6-(0.05*price6)
                mes_dis1="Total price with discount: CA$ "+ str(discount_price1) + "\n\n"
                mes_dis2="Total price with discount: CA$ "+ str(discount_price2) + "\n\n"
                mes_dis3="Total price with discount: CA$ "+ str(discount_price3) + "\n\n"
                mes_dis4="Total price with discount: CA$ "+ str(discount_price4) + "\n\n"
                mes_dis5="Total price with discount: CA$ "+ str(discount_price5) + "\n\n"
                mes_dis6="Total price with discount: CA$ "+ str(discount_price6) + "\n\n"
            option1 = ("**OPTION 1)** " +"\n"+
            "Country: Albania " +"\n"+
            "Airline: Air Canada"+"\n" +
            "Hotel: Maritim Hotel Plaza Tirana " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: None" + "\n\n"+
             "Total price: CA$ "+ str(price1) + "\n"+
            mes_dis1)
            option2 = ("**OPTION 2)**" +"\n"+
            "Country: Albania " +"\n"+
            "Airline: Air Canada"+"\n" +
            "Hotel: Maritim Hotel Plaza Tirana " + "\n" +
            "Meals incuded: Breakfast"  +"\n"+
            "Sighseeings included: Shala River" + "\n\n"+
            "Total price: CA$ "+ str(price2) + "\n"+
            mes_dis2)
            option3 = ("**OPTION 3)**" +" \n "+
            "Country: Albania " +" \n "+
            "Airline: Air Canada"+" \n " +
            "Hotel: Maritim Hotel Plaza Tirana " + " \n " +
            "Meals incuded: Breakfast and dinner"  +" \n "+
            "Sighseeings included: Shala River and Lake Bovilla" + "\n\n"+
            "Total price: CA$ "+ str(price3) + "\n"+
            mes_dis3)
            option4 = ("**OPTION 4)** " +"\n"+
            "Country: India " +"\n"+
            "Airline: Air India"+"\n" +
            "Hotel: Novotel New Delhi Aerocity " + "\n" +
            "Meals incuded: Breakfast and dinner"  +"\n"+
            "Sighseeings included: Taj Mahal and Gandhi Smriti" + "\n\n"+
            "Total price: CA$ "+ str(price4) + "\n"+
            mes_dis4)
            option5 = ("**OPTION 5)**" +"\n"+
            "Country: India " +"\n"+
            "Airline: United Airlines"+"\n" +
            "Hotel: Taj Palace " + "\n" +
            "Meals incuded: Breakfast "  +"\n"+
            "Sighseeings included: Taj Mahal " + "\n\n"+
            "Total price: CA$ "+ str(price5) + "\n"+
            mes_dis5)
            option6 = ("**OPTION 6)**" +" \n "+
            "Country: India " +" \n "+
            "Airline: United Airlines"+" \n " +
            "Hotel: Taj Palace " + " \n " +
            "Meals incuded: Breakfast and dinner "  +" \n "+
            "Sighseeings included: Taj Mahal and Gandhi Smriti" + "\n\n"+
            "Total price: CA$ "+ str(price6) + "\n"+
            mes_dis6)
        elif amount>9000 and amount<=10000:
            price1=9500
            price2=9700
            price3=9880
            if query_result.get('action') == 'LoyaltyX.LoyaltyX-custom.BudgetX-custom':   
                discount_price1=price1-(0.05*price1)
                discount_price2=price2-(0.05*price2)
                discount_price3=price3-(0.05*price3)
                mes_dis1="Total price with discount: CA$ "+ str(discount_price1) + "\n\n"
                mes_dis2="Total price with discount: CA$ "+ str(discount_price2) + "\n\n"
                mes_dis3="Total price with discount: CA$ "+ str(discount_price3) + "\n\n"
            option1 = ("**OPTION 1)** " +"\n"+
            "Country: India " +"\n"+
            "Airline: Air India"+"\n" +
            "Hotel: Taj Palace " + "\n" +
            "Meals incuded: None"  +"\n"+
            "Sighseeings included: None" + "\n\n"+
            "Total price: CA$ "+ str(price1) + "\n"+
            mes_dis1)
            option2 = ("**OPTION 2)**" +"\n"+
            "Country: India " +"\n"+
            "Airline: Air India"+"\n" +
            "Hotel: Taj Palace " + "\n" +
            "Meals incuded: None "  +"\n"+
            "Sighseeings included: Taj Mahal and Gandhi Smriti " + "\n\n"+
            "Total price: CA$ "+ str(price2) + "\n"+
            mes_dis2)
            option3 = ("**OPTION 3)**" +" \n "+
            "Country: India " +" \n "+
            "Airline: Air India"+" \n " +
            "Hotel: Taj Palace " + " \n " +
            "Meals incuded: Breakfast  "  +" \n "+
            "Sighseeings included: Taj Mahal and Gandhi Smriti" + "\n\n"+
            "Total price: CA$ "+ str(price3) + "\n"+
            mes_dis3)
        elif amount>10000:
            price1=9500
            if query_result.get('action') == 'LoyaltyX.LoyaltyX-custom.BudgetX-custom':    
                discount_price1=price1-(0.05*price1)
                mes_dis1="Total price with discount: CA$ "+ str(discount_price1) + "\n\n"
            option1 = ("**OPTION 1)** " +"\n"+
            "Country: India " +"\n"+
            "Airline: Air India"+"\n" +
            "Hotel: Taj Palace " + "\n" +
            "Meals incuded: Breakfast and dinner"  +"\n"+
            "Sighseeings included: aj Mahal and Gandhi Smriti" + "\n\n"+
            "Total price: CA$ "+ str(price1) + "\n"+
            mes_dis1)
        elif amount<3000 and amount>=500:
             option1 = ("The cheapest package that we have it worth 3000... Please, enter one value greater than this to continue...")
            
        options=("Please choose the best option for you and tell me \n"+ option1 +"\n"+ option2 +"\n"+ option3+"\n" + option4+"\n"+ option5+"\n"+ option6+"\n"+ option7+"\n"+option8+"\n"+option9+"\n")
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
        if budgetOptions=="Option 4":
            optionselected="You selected OPTION 4. Can we confirm?"
        elif budgetOptions=="Option 5":
            optionselected="You selected OPTION5. Can we confirm?"
        elif budgetOptions=="Option 6": 
             optionselected="You selected OPTION 6. Can we confirm?" 
        if budgetOptions=="Option 7":
            optionselected="You selected OPTION 7. Can we confirm?"
        elif budgetOptions=="Option 8":
            optionselected="You selected OPTION 8. Can we confirm?"
        elif budgetOptions=="Option 9": 
             optionselected="You selected OPTION 9. Can we confirm?"

        fulfillmentText=optionselected
    return {
            "fulfillmentText": fulfillmentText,
            "source": "webhookdata"
        }

if __name__ == '__main__':
    socketIo.run(app)
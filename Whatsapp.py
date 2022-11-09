from twilio.rest import Client
def SendWhatsapp(message): 
    account_sid = 'ACad8d8868096d1c5d07c2611b75a778a2' 
    auth_token = '[Auth Token]' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
                    from_='whatsapp:+14155238886',  
                    body=message,      
                    to='whatsapp:+919650644585' 
                )

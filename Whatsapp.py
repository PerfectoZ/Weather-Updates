from twilio.rest import Client
def SendWhatsapp(message): 
    account_sid = 'ACad8d8868096d1c5d07c2611b75a778a2' 
    auth_token = '1d0e3efceccab104080d7122c0f4200a' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
                    from_='whatsapp:+14155238886',  
                    body=message,      
                    to='whatsapp:+919650644585' 
                )
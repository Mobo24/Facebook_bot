from fbchat import  Client, log
from fbchat.models import *
import apiai, codecs, json

class mendonwheels(Client):

    # Connect to dialogflow
    def apiaiCon(self):
        self.CLIENT_ACCESS_TOKEN = "#####################################################"
        self.ai = apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
        self.request = self.ai.text_request()
        self.request.lang = 'de' #Default : English
        self.request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        models = {
            "iphone 5": "$55",
            "iphone 5s": "$55",
            "iphone 5c": "$55",
            "iphone 6": "$65",
            "iphone 6 Plus": "$65",
            "iphone6s": "$70",
            "iphone6s Plus": "$70",
            "iphone 7": "$80",
            "iphone 7 Plus": "$85",
            "iphone 8": "$90",
                "iphone 8 Plus": "$95"
        }
        # Mark message as read
        self.markAsRead(author_id)

        # Print info on console
        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))

        # Establish conn
        self.apiaiCon()

        # Message Text
        msgText = message_object.text

        # Request query/reply for the msg received
        self.request.query = msgText

        # Get the response which is a json object
        response = self.request.getresponse()

        # Convert json obect to a list
        reader = codecs.getdecoder("utf-8")
        obj = json.load(response)

        # Get reply from the list
        for k,v in models.items():
            txt = str(msgText)
            #print(k, flush=True)
            if k in txt.lower():
                reply = "The Cost of fixing an " + k + " is " + v + " Contact me at 484-200-8238 so details can be discussed"
                break
            elif k not in txt.lower():
                print (k + " " + txt,flush=True)
                reply = "Ask about the price of any Iphone product and i'll ask about the price"

        # Send message
        if author_id!=self.uid:
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        # Mark message as delivered
        self.markAsDelivered(author_id, thread_id)


# Create an object of our class, enter your email and password for facebook.
client = mendonwheels("mendonwheels@outlook.com", "##########")

# Listen for new message
client.listen()

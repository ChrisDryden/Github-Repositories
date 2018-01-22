# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:06:42 2018

@author: Chris Dryden
"""

from flask import Flask, jsonify, make_response, request, abort
app = Flask(__name__)


from fbchat import log, Client
import os

# Subclass fbchat.Client and override required methods

PHONE_NUMBER = 12048170612
TARGET_NUMBER = 16477834443



class FacebookBot(Client):
    
    
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        
        

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            os.system("lib messagebird.tel[@0.0.17].sms --originator " + str(PHONE_NUMBER) +" --recipient " + str(TARGET_NUMBER) + " --body " + str(message_object.text))
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)
            

@app.route('/', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    print("task created")
    return jsonify(request)
@app.route('/')
def index():
    return "Hello, World!"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    client = FacebookBot("christopher.dryden@utsu.ca", "toronto9")
    app.run(
    host=os.getenv('LISTEN', '0.0.0.0'),
    port=int(os.getenv('PORT', '8080')))   
    
    client.listen()
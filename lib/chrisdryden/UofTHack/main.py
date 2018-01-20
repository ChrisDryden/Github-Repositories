# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 01:25:50 2018

@author: Chris Dryden
"""

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
            

client = FacebookBot("christopher.dryden@utsu.ca", "toronto9")


client.listen()
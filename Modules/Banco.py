#!/usr/bin/python3

from pymongo import MongoClient
import pymongo
from datetime import datetime
import time



class Banco:
    def __init__(self):
        self.client = MongoClient('127.0.0.1')
        self.db = self.client['chat']


    def filter(self):
        message = []
        for t in self.db.message.find().sort("hora", pymongo.DESCENDING).limit(25):
            message.append(t)
        message.reverse()
        return message


    def add_message(self,**kwargs):
        self.db.message.insert({"name":kwargs["name"],"message":kwargs["message"],"hora":str(time.strftime('%d-%m-%Y %H:%M:%S'))})





if __name__ == '__main__':
    t = Banco()
    t.filter()
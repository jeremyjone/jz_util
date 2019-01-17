#! usr/bin/env python
#-*- coding: utf-8 -*-
'''
The operation of Mongo is simply encapsulated.
By: jeremyjone

mongoDB for connect mongoDB's collections,
mongoCursor for create a custom cursor.
    ex:
        connect = mongoDB(...)  --> connect to mongoDB server
        coll = connect.connect('td_test', 'episode')  --> connect target collections
        cursor = mongoCursor(coll)  --> create cursor object
        # cursor can use likes normal CURD
        cursor.insert(...)
        cursor.remove(...)
        cursor.update(...)
        cursor.find(...)
'''
from pymongo import MongoClient
from pymongo import collection



class mongoDB(object):
    def __init__(self, host="127.0.0.1", port=27017):
        '''
        host --> string, default "127.0.0.1", your mongoDB's host
        port --> int, default 27017, your mongoDB's port
        '''
        self.conn = MongoClient(host, port)
        self.host = host
        self.port = port

    def connect(self, database, collections):
        '''
        Connect mongoDB's collections, return a collections object.
        @parameter:
            database --> string, mongo dbs name which you will use
            collections --> string, mongo collections name which you will use
        @return:
            collections object
            ex:
                coll = connect(...)
                cursor = coll.find({...})
        '''
        db = self.conn[database]
        coll = db[collections]
        return coll

    def disconnect(self):
        '''Close connect.'''
        self.conn.close()


class mongoCursor(collection.Collection):
    def __init__(self, connObj):
        '''
        ConnObj need a mongoDB connect handler object
        Reword remove method, this method only can remove one collection,
        same to remove_one, avoid error deletion. If you want to remove
        all collections, use removeAll method.
        '''
        super(mongoCursor, self).__init__(connObj.database, connObj.name)

    def remove(self, spec_or_id=None, multi=False, **kwargs):
        '''remove one collection which match condition.'''
        self.connObj.remove(spec_or_id, multi, **kwargs)

    def removeAll(self, spec_or_id=None, multi=True, **kwargs):
        '''remove all collection which match condition.'''
        self.connObj.remove(spec_or_id, multi, **kwargs)





if __name__ == '__main__':
    mongo = mongoDB("192.168.1.93")
    coll = mongo.connect('td_test', 'episode')
    cursor = mongoCursor(coll)
    cursor.find({}, {"_id": 0})

    for i in cursor:
        print i

#-*- coding:utf-8 -*-
"""
mangoDB handle module.

可以通过继承Handle方法对数据库进行操作。
"""
__author__ = 'jeremyjone'
__datetime__ = '2018-10-08 17:59'
from functools import wraps
import Jzmongo


def j_log(source):
    if callable(source):
        func = source
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                log.logger.error("This is unexpected Error, function name: %s,\n\t"
                                 "Error message is: %s" % (func.__name__, str(e))
                                )
        return wrapper

    elif isinstance(source, str):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    log.logger.error("This is unexpected Error, function name: %s,\n\t"
                                     "Error message is: %s" % (func.__name__, str(e)) + source
                                    )
            return wrapper
        return decorator

    else:
        raise AttributeError("Attribute other than str is not supported")




class MangoDBHandle(Jzmongo.mongoDB):
    def __init__(self):
        super(MangoDBHandle, self).__init__(host="localhost", port=27017)

    def getCursor(self, c, t):
        '''collection and table name, return cursor'''
        collection = self.connect(c, t)
        return Jzmongo.mongoCursor(collection)


    # @j_log
    # def user(self, username):
    #     '''
    #     Query whether the database has this username.
    #     '''
    #     cursor = self.getCursor(dbconfig.DB_COLLECTION[self.TABLE_USER])
    #
    #     return cursor.find_one({"name": username}, {"_id": 0})





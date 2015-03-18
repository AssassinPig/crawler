# -*- coding: utf-8 -*-
import signal, os
import time
import settings
import redis
import threading

class Master(object): 

    @staticmethod
    def exit_handler(signum, frame):
        print 'you press ctrl+c!'
        #instance()

    def __init__(self, settings=None, start_urls=None, strategy=None):
        if settings is None:
            try:
                self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
                if self.r is None:
                    raise redis.exceptions.ConnectionError 
            except (redis.exceptions.ConnectionError), e:
                raise e 
        else:
            self.host = settings.REDIS_HOST
            self.port = settings.PORT

            self.QUEUE_TODO = settings.QUEUE_TODO
            self.QUEUE_VISITED = settings.QUEUE_VISITED
            self.QUEUE_FETCHED = settings.QUEUE_FETCHED

            self.r = redis.StrictRedis(host=self.host, port=self.port, db=0)
        signal.signal(signal.SIGINT, self.exit_handler)
        if start_urls is not None:
            self.todo_list = start_urls
        self.thread_running = False

        #Master._instance = this

    #@staticmethod
    #def instance():
    #    return self._instance

    def is_running(self):
        return self.thread_running

    def run(self):
        while True:
            for l in self.todo_list:
                self.r.lpush(self.QUEUE_TODO, l)  

            url = self.r.brpop(self.QUEUE_FETCHED) 
            print 'fetch %s' % url[1]
            #we suppose url is validate
            self.todo_list.append(url[1])

    @staticmethod
    def put(master):
        while master.is_running():
            for l in master.todo_list:
                master.r.lpush(master.QUEUE_TODO, l)  
            time.sleep(1)

    @staticmethod
    def fetch(master):
        while master.is_running():
            url = master.r.brpop(master.QUEUE_FETCHED) 
            master.todo_list.append(url)

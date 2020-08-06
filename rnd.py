from threading import Thread, Event
from random import random
from time import  sleep

thread = Thread()
thread_stop_event = Event()


class RandomThread(Thread):
    def __init__(self, socketio):
        self.delay = 1
        super(RandomThread, self).__init__()
        self.socketio = socketio

    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        # infinite loop of magical random numbers
        print("Making random numbers")
        while not thread_stop_event.isSet():
            number = round(random() * 10, 3)
            print(number)
            self.socketio.emit('newnumber', {'number': number}, namespace='/test')
            sleep(self.delay)

    def run(self):
        self.randomNumberGenerator()

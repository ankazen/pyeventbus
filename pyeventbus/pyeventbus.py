class EventBus(object):
    """docstring for EventBus"""
    def __init__(self):
        super(EventBus, self).__init__()
        self.subscribers = {}

    def subscribe(self, eventname, func):
        if eventname in self.subscribers:
            self.subscribers[eventname].append(func)
        else:
            self.subscribers[eventname] = [func]

    def fire(self, eventname, data):
        if eventname not in self.subscribers:
            return
        for func in self.subscribers[eventname]:
            func(data)

EBus = EventBus()

def subscribe(eventname):
    def real_decorator(function):
        EBus.subscribe(eventname, function)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapper
    return real_decorator

import threading

class InstanceClass(object):
    _instance_lock = threading.Lock()  # 保证线程安全，加入锁
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(InstanceClass, "_instance"):
            with InstanceClass._instance_lock:
                if not hasattr(InstanceClass, "_instance"):
                    InstanceClass._instance = object.__new__(cls)
        return InstanceClass._instance

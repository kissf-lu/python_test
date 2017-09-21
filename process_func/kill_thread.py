import threading, ctypes, time

class InterruptableThread(threading.Thread):
    @classmethod
    def _async_raise(cls, tid, excobj):
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(excobj))
        if res == 0:
            raise ValueError("nonexistent thread id")
        elif res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    def raise_exc(self, excobj):
        assert self.isAlive(), "thread must be started"
        for tid, tobj in threading._active.items():
            if tobj is self:
                self._async_raise(tid, excobj)
                return

    def terminate(self):
        self.raise_exc(SystemExit)


def A():
    t = InterruptableThread(target=B)
    t.start()
    return t


def B():
    # t = threading.Thread(target=C)
    # t.start()
    for i in range(10):
        print(i)
        time.sleep(1)

def C():
    for i in range(10, 20):
        print(i)
        time.sleep(1)

T = A()
time.sleep(2)
T.terminate()
while True:pass
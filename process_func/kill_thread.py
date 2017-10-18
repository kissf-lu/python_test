import threading, ctypes, time


class Tim(object):
    IF_TERMINAL = False
    P_Q = []


class InterruptableThread(threading.Thread):
    @classmethod
    def _async_raise(cls, tid, excobj):
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            tid,
            ctypes.py_object(excobj))
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
    for i in range(3):
        sleep = int(i)
        res = InterruptableThread(target=B, args=(i, sleep,))
        Tim.P_Q.append(res)

    for t in Tim.P_Q:
        t.start()


    t_manager = InterruptableThread(target=C,)
    Tim.P_Q.append(t_manager)
    t_manager.start()

    for t in Tim.P_Q:
        t.join()
    print('stop')



def B(id, sleep):
    for i in range(10):
        print(f'[{id}] Got', i)
        time.sleep(1)


def C():
    num = 0
    print('C', num)
    while True:
        print(num)
        time.sleep(1)
        num +=1
        if num == 2:
            # for t in Tim.P_Q:
            #     t.terminate()
            Tim.IF_TERMINAL = True
            print('terminal:', num)
        #
        if Tim.IF_TERMINAL:
            for t in Tim.P_Q:
                t.terminate()
                print(t.is_alive())




A()

print('end')

while True : pass
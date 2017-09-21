import threading, ctypes, time


class Tim(object):
    IF_TERMINAL = False


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


def A(t_q):
    t_manager = InterruptableThread(target=C)
    for i in range(3):
        sleep = int(i)
        t_q.append(InterruptableThread(target=B, args=(i, sleep,)))
    t_manager.start()
    for t in t_q:
        t.start()
    t_q.append(t_manager)

    return t_q


def B(id, sleep):
    # t = InterruptableThread(target=C)
    # t.start()
    for i in range(10):
        print(f'[{id}] Got', i)
        time.sleep(sleep)
    # return t


def C():
    for i in range(10, 20):
        time.sleep(10)
        Tim.IF_TERMINAL = True

t_q = []
T = A(t_q)

if Tim.IF_TERMINAL:
    for t in T:
        t.terminate()
for t in T:
    t.join()

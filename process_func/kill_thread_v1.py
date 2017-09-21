import threading
import ctypes


def _async_raise(tid, excobj):
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,
ctypes.py_object(excobj))
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


class Thread(threading.Thread):
    def raise_exc(self, excobj):
        assert self.isAlive(), "thread must be started"
        for tid, tobj in threading._active.items():
            if tobj is self:
                _async_raise(tid, excobj)
                break

        # the thread was alive when we entered the loop, but was not found
        # in the dict, hence it must have been already terminated.
        #bshould we raise
        # an exception here? silently ignore?

    def terminate(self):
        self.raise_exc(SystemExit())

if __name__ == "__main__":
    import time
    import sys

    i_am_active = False

    def f():
        global i_am_active
        i_am_active = True
        try:
            try:
                while True:
                    time.sleep(0.01)
            except IOError as ex:
                print("IOError handler")
            except TypeError as ex:
                print("TypeError handler")
                print("ex=", repr(ex))
                typ, val, tb = sys.exc_info()
                print("typ=", repr(typ))
                print("val=", repr(val))
                print("tb=", tb)
        finally:
            i_am_active = False

    t1 = Thread(target = f)
    t1.start()
    time.sleep(1)
    t1.raise_exc(TypeError("blah blah"))
    while i_am_active:
        time.sleep(0.01)
    print("!! thread terminated")
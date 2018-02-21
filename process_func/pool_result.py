import multiprocessing
import time
import os

def func(msg):
  for i in range(10):
    print(msg, f'{os.getpid()} at', time.time())
    time.sleep(1)
  return "done " + msg + str(time.time())
if __name__ == "__main__":
    result = []
    with multiprocessing.Pool(processes=4) as pool:
        for i in range(4):
            msg = "hello %d" %(i)
            result.append(pool.apply_async(func, (msg, )))
        for res in result:
            print(res.get())
    print("Sub-process(es) done.")

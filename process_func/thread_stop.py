import threading
import time
import sys, _thread
ended = threading.Event()

def do_work():
    num = 0
    while not ended.is_set():
        num += 1
        # Do your repeated work
        time.sleep(10)
        print(f'[{num}] Got Worker!')


def main():

    # Let's create and start our worker thread!
    new_thread = threading.Thread(target=do_work)
    new_thread.start()


    try:
        while not ended.is_set():
            ended.wait(1)
    except (KeyboardInterrupt, SystemExit):
        print("Cancelling")
        ended.set()

if __name__ == '__main__':
    main()
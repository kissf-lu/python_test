import multiprocessing
import time
import os
# # ==============================
import simpy


class School(object):
    def __init__(self, env, pid):
        self.env = env
        self.pid = pid
        self.class_ends = env.event()
        self.pupil_procs = [env.process(self.pupil(i)) for i in range(3)]
        self.bell_proc = env.process(self.bell())
        self.num_cls = 3

    def bell(self):
        for i in range(self.num_cls):
            yield self.env.timeout(45)
            # trigger class time out env success
            self.class_ends.succeed()
            # init new call time out env to be triggered
            self.class_ends = self.env.event()
            # print(f"pid of {self.pid} class {i} end!")

    def pupil(self, id_p):
        p_id = id_p
        for i in range(self.num_cls):
            # print(f'{p_id} \o/', end=' ')
            # wait event
            yield self.class_ends


def run(msg):
    _pid = os.getpid()
    print(msg, f'{_pid} at', time.time())
    env = simpy.Environment()
    for _ in range(2):
        School(env, _pid)
    env.run()
    return f'go: {msg} {_pid}'

# def func(msg):
#   for i in range(100):
#     print(msg, f'{os.getpid()} at', time.time())
#     time.sleep(1)
#   return "done " + msg + str(time.time())

if __name__ == "__main__":
    result = []
    with multiprocessing.Pool(processes=4) as pool:
        for i in range(4):
            msg = "run %d and pid is: " %(i)
            result.append(pool.apply_async(run, (msg, )))
        for res in result:
            print(res.get())
    print("Sub-process(es) done.")

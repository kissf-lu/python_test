"""
Machine shop example

Covers:

- Interrupts
- Resources: PreemptiveResource

Scenario:
  A workshop has *n* identical machines. A stream of jobs (enough to
  keep the machines busy) arrives. Each machine breaks down
  periodically. Repairs are carried out by one repairman. The repairman
  has other, less important tasks to perform, too. Broken machines
  preempt theses tasks. The repairman continues them when he is done
  with the machine repair. The workshop works continuously.

"""
import random

import simpy

RANDOM_SEED = 42
PT_MEAN = 10.0  # Avg. processing time in minutes
PT_SIGMA = 2.0  # Sigma of processing time
MTTF = 300.0  # Mean time to failure in minutes
BREAK_MEAN = 1 / MTTF  # Param. for expovariate distribution
REPAIR_TIME = 30.0  # Time it takes to repair a machine in minutes
JOB_DURATION = 30.0  # Duration of other jobs in minutes
NUM_MACHINES = 5  # Number of machines in the machine shop
WEEKS = 4  # Simulation time in weeks
SIM_TIME = WEEKS * 7 * 24 * 60  # Simulation time in minutes
CLOSE_TIME = 10


class Machine(object):

    def __init__(self, env, name):
        self.env = env
        self.start = 0
        self.left_time = 0
        self.name = name
        self.parts_made = 0
        self.broken = False
        self.done_in = 0

        self.process = env.process(self.working())
        env.process(self.break_machine())

    def working(self):
        while True:
            # Start making a new part
            self.done_in = random.randint(3, 12)
            while self.done_in:
                try:
                    self.start = self.env.now
                    # Working on the part
                    yield self.env.timeout(self.done_in)
                    self.done_in = 0  # Set to 0 to exit while loop.

                except simpy.Interrupt:
                    self.broken = True
                    self.left_time = self.done_in - (self.env.now - self.start)
                    print("%s stop at %s, %s have make %d parts" %
                          (self.name, self.env.now + self.left_time, self.name, self.parts_made + 1))
                    yield self.env.timeout(CLOSE_TIME + self.left_time)
                    print("%s start at %s" % (self.name, self.env.now))

                    self.done_in = 0
                    self.broken = False

            # Part is done.
            self.parts_made += 1

    def break_machine(self):
        """Break the machine every now and then."""
        while True:
            yield self.env.timeout(random.randint(20, 40))
            if not self.broken:
                yield self.env.timeout(self.left_time)
                self.process.interrupt()


# Setup and start the simulation
print('Machine shop')
random.seed(RANDOM_SEED)  # This helps reproducing the results

# Create an environment and start the setup process
env = simpy.Environment()
machines = [Machine(env, 'Machine %d' % i)
            for i in range(NUM_MACHINES)]
# machine = Machine(env, 'Machine A')

# Execute!
env.run(until=SIM_TIME)

# Analyis/results
print('Machine shop results after %s weeks' % WEEKS)
for machine in machines:
    print('%s made %d parts.' % (machine.name, machine.parts_made))

from time import time

class LeakyBucket:
  def __init__(self, capacity=10, rate=1):
      self.capacity = capacity
      self.rate = rate
      # Assume that the unit of rate is only 'rps'
      self.interval = rate / 60
      self.current_time = time()

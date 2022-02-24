from datetime import datetime

class LeakyBucket:
  def __init__(self, rate=1, time=0, capacity=0, queue=[]):
      self.rate = rate
      self.capacity = capacity
      # Unit of rate is only 'rph'. Convert to ms
      self.interval = 3600 * 1000
      self.current_time = time
      self.queue = queue

  def set_current_time(self):
    self.current_time = self.queue[0]

  def renew_bucket(self):
    self.queue.pop(0)
    self.set_current_time()
    self.capacity -= 1

  def fwd_req(self):
    self.capacity += 1
    print("true")

  def drop_req(self):
    print("false")

def convert_iso_to_ms(iso_ts):
  date = datetime.strptime(iso_ts, '%Y-%m-%dT%H:%M:%SZ')
  ms_ts = (date - datetime(1970, 1, 1)).total_seconds() * 1000
  return ms_ts

if __name__ == "__main__":
  n_requests = int(input("Number of requests: "))
  rate = int(input("Rate limit (request/hour): "))
  bucket = LeakyBucket(rate)
  while n_requests != 0:
    ts = input("Timestamp: ")
    ts = convert_iso_to_ms(ts)
    bucket.queue.append(ts)
    if bucket.current_time == 0:
      bucket.set_current_time()
      bucket.fwd_req()
    else:
      if bucket.capacity < bucket.rate:
        bucket.fwd_req()
      else:
        if ts - bucket.current_time > bucket.interval:
          bucket.renew_bucket()
          bucket.fwd_req()
        else:
          bucket.drop_req()
    n_requests -= 1
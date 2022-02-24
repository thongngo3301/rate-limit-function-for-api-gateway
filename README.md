# rate-limit-function-for-api-gateway

<h2>Guide</h2>

- Using Python3 with default venv

- Run: python leaky_bucket.py

<br>

<h2>Idea</h2>

- The default rate will be the capacity of the bucket in a fix interval.

- If the bucket still has vacancy (capacity < rate), the request will be processed.

- If the bucket is full, check the timestamp of the incoming request. If the timestamp is valid (time diff between it and current time of the bucket is larger than the fix interval), then the request will be processed. The current time (aka clock) of the bucket will be reset. We will need a queue to store timestamp of requests. The "expired" timestamp will be drop and the second one (now becoming the first one) will be the current time of the bucket.

- Otherwise, the request will be dropped.

<br>

<h2>Future</h2>

- To deploy in a cluster model, I planned to use a Redis as a central queue to store the above time queue between API gateways

- Source IP will be extracted from the request and convert to byte string. I will use that byte string as a queue in Redis.

- All extracted timestamps of a source IP will be pushed to the corresponding queue.

- Every time the rate limit function check a timestamp of a request, it will check with the first timestamp in the queue.
The basic principle of the algorithm still remains the same.

Sorry for finishing all of this in urgent, I will provide a diagram later.
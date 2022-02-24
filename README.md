# rate-limit-function-for-api-gateway

Guide:
- Using Python3 with default venv

Idea:
- The default rate will be the capacity of the bucket in a fix interval
- If the bucket still has vacancy (capacity < rate), the request will be processed
- If the bucket is full, check the timestamp of the incoming request. If the timestamp is valid (time diff between it and current time of the bucket is larger than the fix interval), then the request will be processed
- Otherwise, the request will be dropped
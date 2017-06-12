from __future__ import print_function
import json
import boto3
import time


print("Loading function")

def getMyLogstream(self, event, context):
    print('Log stream name: ',context.log_stream_name)
    print('Log group name: ', context.log_group_name)
    print('Request ID: ', context.aws_request_id)
    print('Mem. limit (MB) ', context.memory_limit_in_mb)
    time.sleep(1)
    print('Time remaining (MS): ', context.get_remaining_time_in_millis())
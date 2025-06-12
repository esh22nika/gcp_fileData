import os   # for env var
import json
import functions_framework  #helps handle cloud func or cloud events
from google.cloud import pubsub_v1 
from cloudevents.http import CloudEvent
#gcs sends triggers in cloud event format, so we have to decode it

publisher = pubsub_v1.PublisherClient()
# this func helps us send msg to pub sub topic
@functions_framework.cloud_event # tells cloud that below func will handle cloud event

def file_proc(cloud_event: CloudEvent)->None:   
    #cloud_event passed as argument stores everything about file metadata and trig event
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    topic_name = os.environ.get("PUBSUB_TOPIC")
    #gets from gcp
    topic_path = publisher.topic_path(project_id, topic_name)
    
    data = cloud_event.data    #storing all data in cloud_event in one var
    file_name = data.get('name', 'not_specified') #also added default values
    file_size = int(data.get('size', 0))
    #can also get time created
    time_created = data.get('timeCreated', 'Unknown')
    #getting the file extension for file format
    file_format = file_name.split('.')[-1] if '.' in file_name else 'no_extension'
    # the msg for pubsub
    message = {
        "file": file_name,
        "size": file_size,
        "format": file_format,
        "timeCreated": time_created
    }

    try:
        #converting to json, publishing to pubsub, returns future object
        msg_json = publisher.publish(topic_path, json.dumps(message).encode("utf-8"))
        #result func returns msg id after publishing
        print("published message ID", msg_json.result())
    except Exception as e:
        print("error occured while publishing to pubsub:", e)
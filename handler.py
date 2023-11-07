import json
#SAK hOZTBuIJoox503R0G1cM714pYvqkXpXZEp6eU0qx
#AK AKIAW5GGVDHBF3G5A7UV

def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}

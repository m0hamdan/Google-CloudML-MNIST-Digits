import googleapiclient.discovery
import json
from PIL import Image
import base64
import io
import numpy as np
from io import StringIO
from google.oauth2 import service_account
import base64, sys, json; 

def predict_json(project, model, instances, version=None):
    
    # Create the ML Engine service object.
    # To authenticate set the environment variable
    # GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
    service_account_file = "cpb100-97d0ce37bc40.json"

    credentials = service_account.Credentials.from_service_account_file(
    service_account_file)
    service = googleapiclient.discovery.build('ml', 'v1',credentials=credentials)
    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:

        name += '/versions/{}'.format(version)
    response = service.projects().predict(
        name=name,
        body= {'instances':instances}
    ).execute()
    if 'error' in response:
        raise RuntimeError(response['error'])
    return response['predictions']

img = base64.b64encode(open("6.png", "rb").read()).decode()
json_content =  {"image_bytes":{"b64": json.dumps(img)}}

project = 'cpb100-245606'
model = 'demo_model'
preds = predict_json(project,model,json_content,version='v2')
print(preds)






'''
 https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive/08_image/flowers_fromscratch.ipynb
%%bash
IMAGE_URL=gs://cloud-ml-data/img/flower_photos/sunflowers/1022552002_2b93faf9e7_n.jpg

# Copy the image to local disk.
gsutil cp $IMAGE_URL flower.jpg

# Base64 encode and create request message in json format.
python -c 'import base64, sys, json; img = base64.b64encode(open("flower.jpg", "rb").read()).decode(); print(json.dumps({"image_bytes":{"b64": img}}))' &> request.json
 '''
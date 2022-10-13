from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import json


subscription_key = ""
endpoint = ""
 
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
def azure_ocr_api(image_url):
        #local_image_url = "Cheque083654.jpeg"
        read_response = computervision_client.read_in_stream(open("./Images/" + image_url,'rb'),  raw=True)
        #read_response = computervision_client.read_in_stream(open(local_image_url,'rb'),  raw=True)

        # Get the operation location (URL with an ID at the end) from the response
        read_operation_location = read_response.headers["Operation-Location"]
        # Grab the ID from the URL
        operation_id = read_operation_location.split("/")[-1]

        # Call the "GET" API and wait for it to retrieve the results 
        while True:
            read_result = computervision_client.get_read_result(operation_id)
            if read_result.status not in ['notStarted', 'running']:
                break
            time.sleep(1)
        list = []
        if read_result.status == OperationStatusCodes.succeeded:
            for text_result in read_result.analyze_result.read_results:

                for line in text_result.lines:
                    list.append(line.text)
        # print(list)
        # pass
        return list
# azure_ocr_api()        
print("End of Computer Vision quickstart.")
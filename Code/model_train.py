import json
from ibm_watson import VisualRecognitionV4
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('-L_ISbMRp4t_bFoGMrQIeTG2n9Qy3pdd1QmKQxGF3al2')
visual_recognition = VisualRecognitionV4(
    version='2019-02-11',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/d9acfb96-cfe0-48b5-9859-e26d687fa469')

result = visual_recognition.train(
    collection_id='d7169bfd-fa76-4d4f-b96a-05e56218631b').get_result()
print(json.dumps(result, indent=2))

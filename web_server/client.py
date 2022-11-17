from __future__ import print_function
import requests
import json
import cv2

addr = 'http://localhost:5000'
endpoint_url = addr + '/api/convert'

content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('apple.jpeg')
_, img_encoded = cv2.imencode('.jpg', img)
response = requests.post(endpoint_url, data=img_encoded.tostring(), headers=headers)
print(json.loads(response.text))

# expected output: {u'message': u'image received. size=124x124'}
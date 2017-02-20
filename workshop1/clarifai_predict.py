from clarifai import rest
from clarifai.rest import ClarifaiApp

app = ClarifaiApp('client id', 'client secret')
model = app.models.get("general-v1.3")

# predict with the model
print model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

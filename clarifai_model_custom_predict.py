from clarifai import rest
from clarifai.rest import ClarifaiApp

# authenticate
app = ClarifaiApp("CLIENT-ID", "CLIENT-SECRET")

model_id = 'dogs_ais'

# get model
model = app.models.get(model_id)

# image to check against model
imgs = [
		("Brown Rabbit", "https://s-media-cache-ak0.pinimg.com/736x/32/00/3b/32003bd128bebe99cb8c655a9c0f00f5.jpg"),
		("Black Shibe", "http://www.shibas.org/images/blacktanShiba_v02.jpg"),
		("Brown Shoe", "http://www.selleys.com.au/assets/560/shoe-2.jpg"),
		("Gray Wolf", "http://nativenewsonline.net/wp-content/uploads/2013/12/wolf-gray-color-beautiful-kewl1.jpg"),
		("Gray Cat", "https://s-media-cache-ak0.pinimg.com/736x/92/9d/3d/929d3d9f76f406b5ac6020323d2d32dc.jpg")
	]

# list of confidences
confidences = []

for img in imgs:
	
	# predict with the model
	results = model.predict_by_url(img[1])

	confidences.append((img[0],results["outputs"][0]["data"]["concepts"][0]["value"]))

# sort confidences descending
confidences.sort(key=lambda tup: tup[1], reverse=True)

# print columns
print "\nImage\t\t\tConfidence"

# print each confidence
for confidence in confidences:
	print confidence[0] + "\t\t" + str(confidence[1])

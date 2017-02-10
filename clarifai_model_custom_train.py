from clarifai import rest
from clarifai.rest import ClarifaiApp

# authenticate
app = ClarifaiApp("L3VAPszWS9okOhmLPn7laCfBzh162RZiahXKDQPx", "ieY1oToUXqQ9bw18cZpsnv3b_NbAkuGXowIH37ku")

# urls of images to train the model with
train_urls = [
	"http://www.pbh2.com/wordpress/wp-content/uploads/2013/11/shiba-inu.jpg",
	"http://images.shibashake.com/wp-content/blogs.dir/7/files/2014/01/P1000907-640x480.jpg",
	"http://www.personalthrows.com/assets/images/ShibaInuFace_50x60RGF_ProdIMG.jpg",
	"http://cdnimg.in/wp-content/uploads/2015/08/Shiba-Inu-Gets-Himself-Stuck-Inside-a-Bush-Gives-Zero-Fks1.jpg?cfaea8",
	"http://images.shibashake.com/wp-content/blogs.dir/7/files/2010/02/IMG_1122-520x390.jpg",
	"http://orig11.deviantart.net/557f/f/2014/119/5/7/squishy_by_marustagram-d7gd3vk.jpg",
	"https://cdn.shopify.com/s/files/1/0601/4169/files/Smile1_large.jpg?6251597665711593980",
	"https://masakadoshiba.files.wordpress.com/2012/05/dsc_0033.jpg"
	]

# feed the app each image 
for train_url in train_urls:
	app.inputs.create_image_from_url(
		url = train_url,
		concepts = ['shiba-inu'],
		not_concepts = None,
		crop = None,
		metadata = None,
		allow_duplicate_url = True
	)

# create the model
model = app.models.create('dogs_ais', concepts=['shiba-inu'])

# train the model
model.train()

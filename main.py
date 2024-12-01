from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np

BUCKET_NAME = "plant-disease-models-p26"

TOMATO_CLASS_NAMES = [
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

POTATO_CLASS_NAMES = [
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy"
]

CORN_CLASS_NAMES = [
    "Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy"
]



model = None

def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    
def predict_tomato(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "tomato.keras",
            "/tmp/tomato.keras",
        )
        model = tf.keras.models.load_model("/tmp/tomato.keras")
    
    image = request.files["file"]
    
    image = np.array(Image.open(image).resize((256,256)))
    # image = image/255
    img_array = tf.expand_dims(image,0)
    
    predictions = model.predict(img_array)
    print(predictions)
    
    predicted_class = TOMATO_CLASS_NAMES[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    
    return {"class": predicted_class, "confidence":confidence}
    
def predict_potato(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "potato.keras",
            "/tmp/potato.keras",
        )
        model = tf.keras.models.load_model("/tmp/potato.keras")
    
    image = request.files["file"]
    
    image = np.array(Image.open(image).resize((256,256)))
    # image = image/255
    img_array = tf.expand_dims(image,0)
    
    predictions = model.predict(img_array)
    print(predictions)
    
    predicted_class = POTATO_CLASS_NAMES[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    
    return {"class": predicted_class, "confidence":confidence}

def predict_corn(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "corn.keras",
            "/tmp/corn.keras",
        )
        model = tf.keras.models.load_model("/tmp/corn.keras")
    
    image = request.files["file"]
    
    image = np.array(Image.open(image).resize((256,256)))
    # image = image/255
    img_array = tf.expand_dims(image,0)
    
    predictions = model.predict(img_array)
    print(predictions)
    
    predicted_class = CORN_CLASS_NAMES[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    
    return {"class": predicted_class, "confidence":confidence}

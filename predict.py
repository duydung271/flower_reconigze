import PIL
import numpy as np
import tensorflow as tf
from tensorflow import keras


model = tf.keras.models.load_model('flower_model.h5')
img_height = 180
img_width = 180
class_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']


def predict(flower_path):
    img = keras.preprocessing.image.load_img(
        flower_path, target_size=(img_height, img_width)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch


    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    return {'name':class_names[np.argmax(score)], 'score': 100 * np.max(score)}

    # print(
    #     "This image most likely belongs to {} with a {:.2f} percent confidence."
    #     .format(class_names[np.argmax(score)], 100 * np.max(score))
    # )
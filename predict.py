import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('model/best_model.keras')

class_names = ['EOSINOPHIL', 'LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL']

def predict(image_path):
    img = tf.keras.utils.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = np.max(predictions[0]) * 100
    
    print(f"Cell type: {predicted_class}")
    print(f"Confidence: {confidence:.1f}%")
    
    if predicted_class == 'NEUTROPHIL':
        print("detectd")
    
    return predicted_class, confidence

# Test on a validation image
import os
test_image = '/Users/vishishtbhatnagar/Desktop/hematic-cnn/data/val/NEUTROPHIL/' + \
    os.listdir('/Users/vishishtbhatnagar/Desktop/hematic-cnn/data/val/NEUTROPHIL/')[0]

predict(test_image)
# Load requirments
from tensorflow import keras
from PIL import Image
import numpy as np
import os


class img_predictor:
    def __init__(self, ver="1"):
        # Parameters
        model_path = "./models/ver."+ver+"/model_inc.hdf5"
        self.model = keras.models.load_model(model_path)
        self.img_size = (299,299)
        self.labels = os.listdir("")

    def predict(self, image):
        # Pre-process image
        """transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])

        p_image = transform(image)
        p_image = p_image.numpy()
        """
        p_image = Image.fromarray(image)
        p_image = p_image.resize(self.img_size)

        p_image = np.asarray(p_image)
        p_image = p_image / 255
        p_image = p_image.tolist()

        # Predict image
        pred = self.model.predict([p_image])
        pred_idx = np.argmax(pred)

        ## TODO return prediction with meaningful json container?
        return pred_idx

"""
Requirement:
Use PIL.Image to open image file 
Use numpy.asarray to convert image into numpy array
Pass the converted numpy array to predict function

or

Pass numpy array of image to predict function
"""
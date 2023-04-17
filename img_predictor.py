
# Load requirments
from tensorflow import keras
from torchvision import transforms

class img_predictor:
    def __init__(self, ver="1"):
        # Parameters
        model_path = "./models/ver."+ver+"/model_inc.hdf5"
        self.model = keras.models.load_model(model_path)

    def predict(self, image):
        # Pre-process image
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])

        p_image = transform(image)
        p_image = p_image.numpy()

        # Predict image
        pred = self.model.predict(p_image)

        ## TODO return prediction with meaningful json container?
        return pred
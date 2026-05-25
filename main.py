from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

# ==========================================
# Initialize FastAPI
# ==========================================

app = FastAPI(
    title="Real vs Fake Detection API",
    description="CNN Model Deployment using FastAPI",
    version="1.0"
)

# ==========================================
# Enable CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# Load CNN Model
# ==========================================

model = load_model("Custom_model_final.h5")

# ==========================================
# Image Size
# Must match training size
# ==========================================

IMG_SIZE = 224

# ==========================================
# Image Preprocessing
# ==========================================

def preprocess_image(image):

    # Convert image to RGB
    image = image.convert("RGB")

    # Resize image
    image = image.resize((IMG_SIZE, IMG_SIZE))

    # Convert image to numpy array
    image_array = np.array(image)

    # IMPORTANT:
    # No normalization because
    # training used raw pixel values

    # Expand dimensions
    image_array = np.expand_dims(image_array, axis=0)

    return image_array

# ==========================================
# Home Route
# ==========================================

@app.get("/")
def home():

    return {
        "message": "CNN FastAPI API Running Successfully"
    }

# ==========================================
# Health Check Route
# ==========================================

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

# ==========================================
# Prediction Route
# ==========================================

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    try:

        # Read uploaded image
        contents = await file.read()

        # Open image
        image = Image.open(io.BytesIO(contents))

        # Preprocess image
        processed_image = preprocess_image(image)

        # Predict
        prediction = model.predict(processed_image)[0][0]

        # Debugging
        print("Raw Prediction:", prediction)

        # ==========================================
        # Label Mapping
        #
        # real = 1
        # fake = 0
        # ==========================================

        if prediction > 0.5:

            predicted_class = "real"
            confidence = float(prediction)

        else:

            predicted_class = "fake"
            confidence = 1 - float(prediction)

        # Return API response
        return {

            "filename": file.filename,
            "prediction": predicted_class,
            "confidence": f"{confidence*100:.2f}%"

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
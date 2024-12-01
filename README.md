
---

# Plant Disease Prediction API

This API provides endpoints to predict plant diseases from images of crops such as tomatoes, potatoes, and corn. The model predicts the disease by classifying images into predefined classes based on the trained models for each crop.

## Setup

1. **Google Cloud Storage Setup**: 
   - Ensure that your Google Cloud Storage bucket (`plant-disease-models-p26`) is accessible and the necessary model files (`tomato.keras`, `potato.keras`, `corn.keras`) are uploaded to the bucket.
   
2. **Model Files**:
   - The following models are downloaded from the Google Cloud Storage bucket when the API is called:
     - `tomato.keras`
     - `potato.keras`
     - `corn.keras`

## Running the Application

To run the FastAPI application, use `uvicorn`:

```bash
uvicorn app:app --reload
```

This will start the server on `http://127.0.0.1:8000`.

## Endpoints

### 1. **Predict Tomato Disease**
   **Endpoint**: `/predict_tomato/`  
   **Method**: `POST`  
   **Request Body**: A file upload (image of a tomato plant).  
   **Response**:
   ```json
   {
     "class": "Tomato___Bacterial_spot",
     "confidence": 90.45
   }
   ```
   - **class**: The predicted disease class for the tomato plant.
   - **confidence**: The confidence of the model in the prediction.

### 2. **Predict Potato Disease**
   **Endpoint**: `/predict_potato/`  
   **Method**: `POST`  
   **Request Body**: A file upload (image of a potato plant).  
   **Response**:
   ```json
   {
     "class": "Potato___Early_blight",
     "confidence": 87.60
   }
   ```
   - **class**: The predicted disease class for the potato plant.
   - **confidence**: The confidence of the model in the prediction.

### 3. **Predict Corn Disease**
   **Endpoint**: `/predict_corn/`  
   **Method**: `POST`  
   **Request Body**: A file upload (image of a corn plant).  
   **Response**:
   ```json
   {
     "class": "Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot",
     "confidence": 92.30
   }
   ```
   - **class**: The predicted disease class for the corn plant.
   - **confidence**: The confidence of the model in the prediction.

## How it Works

- The API receives an image of a plant via a `POST` request at one of the disease prediction endpoints.
- The image is resized to `256x256` and passed through the respective plant disease model.
- The model predicts the disease class and confidence level.
- The response includes the predicted class and confidence.

## Example Usage

### Predict Tomato Disease

Send a `POST` request to `/predict_tomato/` with a file named `file` containing an image:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict_tomato/' \
  -F 'file=@tomato_image.jpg'
```

Response:

```json
{
  "class": "Tomato___Bacterial_spot",
  "confidence": 90.45
}
```

---

## Notes

- The model files are downloaded from a Google Cloud Storage bucket when an endpoint is accessed for the first time.
- Ensure that your Google Cloud credentials are set up correctly for accessing the storage bucket.

---


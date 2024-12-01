# Plant Disease Prediction API

This API predicts plant diseases for various crops using pre-trained machine learning models for **Tomato**, **Potato**, and **Corn** diseases. The models classify plant images into various disease categories based on input images.

## Prerequisites

To use this API, you need to have the following Python libraries installed:

- **FastAPI** - for building the web API
- **Uvicorn** - for serving the FastAPI app
- **python-multipart** - for handling file uploads
- **Pydantic** - for data validation
- **NumPy** - for numerical operations
- **Pillow** - for image processing
- **Google Cloud Storage SDK** (`google-cloud-storage`) - for interacting with Google Cloud Storage
- **TensorFlow** (version `2.16.1`) - for running the machine learning models
- **Keras** (version `3.3.3`) - for loading the Keras models

You can install the necessary libraries using `pip`:

```bash
pip install fastapi uvicorn python-multipart pydantic numpy pillow google-cloud-storage tensorflow==2.16.1 keras==3.3.3

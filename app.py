from flask import Flask, render_template, request, jsonify, send_file
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
from io import BytesIO
from PIL import Image
import os
import logging

app = Flask(__name__)

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Check if CUDA (GPU) is available and set the device accordingly
if torch.cuda.is_available():
    device = torch.device("cuda")
    logging.info("Using GPU for image generation.")
else:
    device = torch.device("cpu")
    logging.info("GPU not available, using CPU for image generation.")

# Initialize the model with error handling
try:
    AUTH_TOKEN = os.getenv('AUTH_TOKEN')
    if not AUTH_TOKEN:
        raise ValueError("AUTH_TOKEN environment variable is not set")
    
    model_id = "CompVis/stable-diffusion-v1-4"
    # Load the model to the selected device (either GPU or CPU)
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
    pipe.to(device)  # Load the model on the selected device

    logging.info(f"Model loaded on {device}")

except Exception as e:
    logging.error(f"Error loading model: {str(e)}")
    raise

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    text_prompt = data.get("prompt", "")

    # Ensure prompt is not empty
    if not text_prompt.strip():
        logging.error("Empty prompt received")
        return jsonify({"error": "Prompt cannot be empty"}), 400

    try:
        logging.info(f"Generating image for prompt: {text_prompt}")

        # Start timer for logging purposes
        # Generate the image with autocast for mixed precision (if needed)
        with autocast(device.type):
            image = pipe(text_prompt, guidance_scale=8.5).images[0]

        logging.info("Image generated successfully")

    except Exception as e:
        logging.error(f"Error generating image: {str(e)}")
        return jsonify({"error": "Image generation failed", "details": str(e)}), 500
    
    # Save the image to an in-memory file
    img_io = BytesIO()
    image.save(img_io, "PNG")
    img_io.seek(0)

    # Clear GPU memory (if using GPU)
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    return send_file(img_io, mimetype="image/png")

if __name__ == "__main__":
    # To prevent timeout, set `threaded=True` or use `gunicorn` for production
    app.run(debug=True, threaded=True)

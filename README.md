
# Text-to-Image Generator with Real-Time Emotion Detection: FaceVibe

### Project Link: - https://letsdoitbycode-text-to-image-generator.hf.space

The Text-to-Image Generator is an AI-powered web application that generates high-quality images from user-provided text prompts. Leveraging Hugging Face's Stable Diffusion model, the application transforms descriptive text into vivid and detailed visuals, making it ideal for creative projects, concept visualization, and artistic experimentation.

### Key Features
Key Objectives
- Seamless Text-to-Image Conversion: Allow users to input descriptive prompts and receive corresponding images that visually interpret the text.
- Accessible Web Interface: Provide an easy-to-use, interactive platform where users can generate images directly from their browser.
- Flexible Prompting for Visual Exploration: Enable users to experiment with different prompts to explore a wide variety of generated visualizations.
- AI-Powered Image Generation: Uses Hugging Face’s Stable Diffusion model to create high-quality images based on textual prompts.
- Interactive Image Generation: Users can experiment with different prompts to explore various visualizations.

### How It Works
- Text Input: Users enter a descriptive text prompt, like "a futuristic city skyline at sunset."
- Text-to-Image Model: The prompt is processed by Hugging Face's Stable Diffusion model, which uses embeddings and a generative neural network to create a corresponding image.
- Image Display: The generated image is displayed on the app interface, available for download.


### Installation
1. Clone the repository
   ```sh
   git clone https://github.com/letsdoitbycode/Text-to-Image-Generator.git
   cd Text-to-Image-Generator
   ```

3. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   

4. Install the required packages:
   ```sh
   pip install flask torch diffusers transformers accelerate gunicorn python-dotenv
   pip install requirements.txt
   ```

4. API key setup for Application:
   ```sh
   touch .env
   paste your API key in .env file as AUTH_TOKEN='API_KEY'
   touch .gitignore
   add .env in the file to secure the API key
   To test the API key, follow below mentioned steps
   ```

### API Key Setup

To run the Text-to-Image Generator, you’ll need a Hugging Face API Token:

- Go to the Hugging Face website https://huggingface.co .
- Sign in or create an account.
- Navigate to Account Settings > API token and click Generate new token.
- Copy the generated token and add it in your Python code (StableDiffusionImage.ipynb) file in place of ```plaintext self.authorization_token = "" ```.

   
6. Run the Flask app:
    ```sh
    python app.py
    ```


### Project Structure
```plaintext
YouTube-Video-Summarization-App/
│
├── app.py                                              # Main Flask application
├── templates/
│   └── index.html                                      # Main HTML file
├── static/
│   ├── style.css                                       # CSS styles
├── .gitignore
├── StableDiffusionImage.ipynb                          # python file for the execution
├── requirements.txt                                    # requirements for the project
└── README.md                                           # This README file
```

## Demo Application Interface

![Screenshot (23)](https://github.com/user-attachments/assets/3aaea3a9-ee95-4a76-9c29-14516b66f633)



## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.





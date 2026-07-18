# Import required libraries
import os
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client using API key stored in .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create Flask application
app = Flask(__name__)


# Displays the main webpage
@app.route("/")
def index():
    return render_template("index.html")

# Image Generation Route
@app.route("/generateimages/<prompt>")
def generate(prompt):
    print("Prompt:", prompt)
    try:
        # Generate image using OpenAI GPT Image API
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )
        return jsonify(response.model_dump())
    except Exception as e:
        # Return error message if image generation fails
        return jsonify({
            "error": str(e)
        })

# Run Flask Application
if __name__ == "__main__":
    app.run(debug=True)
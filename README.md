# AI-Image-Generator-using-Flask-OpenAI-GPT-Image-API
An AI-powered Image Generator web application built with **Python, Flask, HTML, CSS, and JavaScript**. The application generates high-quality images from natural language prompts using the **OpenAI GPT Image API.



## 📌 Project Overview

This project allows users to enter a text prompt and generate AI-created images through a simple web interface.

The application sends the user's prompt to the OpenAI Image Generation API and displays the generated image directly on the webpage.

---

## ✨ Features

- Generate AI images from text prompts
- Modern responsive UI
- Flask backend
- OpenAI GPT Image API integration
- Loading animation while generating images
- Error handling
- Environment variable support (.env)

---

## 🛠 Technologies Used

- Python 3.x
- Flask
- OpenAI Python SDK
- HTML5
- CSS3
- JavaScript
- dotenv

---

## 📂 Project Structure

```
AI-Image-Generator/
│
├── app.py
├── requirements.txt
├── .env.example
├── README.md
│
├── templates/
│      └── index.html
│
├── static/
│      ├── style.css
│      └── script.js
│
└── screenshots/
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Image-Generator.git

cd AI-Image-Generator
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Create .env File

```text
OPENAI_API_KEY=your_api_key_here
```

---

### Run Application

```bash
python app.py
```

---

Open Browser

```
http://127.0.0.1:5000
```

---

## 🖼 Example Prompt

```
A futuristic city at sunset with flying cars
```

---

## 📸 Output

The application generates an AI image based on the given prompt and displays it instantly.

---

## 🔒 Environment Variables

Never upload your actual API key.

Create

```
.env
```

and store

```text
OPENAI_API_KEY=your_api_key
```

---

## 📦 Requirements

```
Flask
openai
python-dotenv
```

Install

```bash
pip install Flask openai python-dotenv
```

---

## 🚀 Future Improvements

- Download generated image
- Image history
- Multiple image generation
- User authentication
- Prompt history
- Image size selection
- Dark Mode
- Deployment on Render

---

## 📖 References

- OpenAI API Documentation
  https://platform.openai.com/docs

- Flask Documentation
  https://flask.palletsprojects.com/

- Python Documentation
  https://docs.python.org/3/

- HTML Documentation (MDN)
  https://developer.mozilla.org/

---


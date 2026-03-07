# Artwork Recommendation System

## Overview

A hybrid artwork recommendation system combining a **Flask backend** with a **React frontend**.
The system provides personalized artwork recommendations using deep learning models and hybrid recommendation techniques.

The application also includes a **chatbot interface**, **user profiles**, and a **social-media-style feed** for interacting with artworks.

---

# Features

### Backend

* Flask REST API
* Hybrid recommendation engine
* Image + text embedding generation
* JWT authentication
* Trending artwork detection
* User interaction tracking (likes)

### Frontend

* React-based UI
* Chatbot interface
* Artwork feed
* User profile system
* Liked artworks page

### Recommendation System

The backend combines multiple approaches:

* Content-based filtering (CLIP embeddings)
* Collaborative filtering (user-item interactions)
* Hybrid recommendation system
* Image captioning using BLIP

### Machine Learning

* CLIP (OpenAI) for image/text embeddings
* BLIP for image captioning
* Cosine similarity for recommendation ranking

---

# Technologies Used

## Backend

* Python
* Flask
* PyTorch
* Transformers
* Pandas
* NumPy
* Scikit-learn
* SciPy
* Datasets (HuggingFace)

## Frontend

* React.js
* Node.js
* NPM

---

# Prerequisites

### Backend

* Python **3.10+**
* **uv** package manager

Install uv if you don't have it:

### Frontend

* Node.js **16+**
* NPM

---

# Installation

## Download Embeddings File

Create this folder:

```
server/
```

Then place the embeddings file inside it:

```
server/combined_embeddings.npy
```

Download the file from:

https://drive.google.com/file/d/1tsCP3zYCchn2MkGmqhdbIKWG4x9PU28Y/view

---

# Backend Setup

### 1. Create virtual environment

```bash
uv venv
```

Activate environment:

**Linux / Mac**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

---

### 2. Install dependencies

```bash
uv pip install flask pandas python-dotenv transformers numpy torch datasets scikit-learn scipy pillow requests pyjwt flask-cors openpyxl
```

---

### 3. Run backend server

```bash
cd server
python server.py
```

The backend will run on:

```
http://localhost:5000
```

---

# Frontend Setup

### 1. Navigate to frontend

```bash
cd frontend
```

### 2. Install dependencies

```bash
npm install
```

### 3. Start development server

```bash
npm start
```

The frontend will run on:

```
http://localhost:3000
```

# Running the Application

Start backend:

```
cd server
python server.py
```

Start frontend:

```
cd frontend
npm run build
npm start
```

Then open:

```
http://localhost:3000
```

---

# Demo

Video demonstration:

https://drive.google.com/file/d/1d9XqGEEgRTkqlYxNz-tHt-RkJrIK2Qbz/view

---

# Notes

* Backend must be running before using the frontend
* Ensure `combined_embeddings.npy` is placed inside the **server** folder
* The frontend communicates with the Flask API running on **port 5000**

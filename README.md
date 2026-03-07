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
* HuggingFace Datasets

## Frontend

* React.js
* Node.js
* NPM

---

# Prerequisites

### Backend

* Python **3.10+**
* **uv** package manager

### Frontend

* Node.js **16+**
* NPM

---

# Installing uv

Install **uv** depending on your operating system.

### Linux / macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart the terminal and verify:

```bash
uv --version
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Restart the terminal and verify:

```powershell
uv --version
```

---

# Installation

## Download Embeddings File

Place the embeddings file in the **project root**:

```
combined_embeddings.npy
```

Download from:

https://drive.google.com/file/d/1tsCP3zYCchn2MkGmqhdbIKWG4x9PU28Y/view

---

# Backend Setup

---

### 1. Install dependencies

```bash
uv sync
```

---

### 2. Run backend server

From the project root:

```bash
uv run server.py
```

Backend runs on:

```
http://localhost:5000
```

---

# Frontend Setup

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start development server:

```bash
npm start
```

Frontend runs on:

```
http://localhost:3000
```

---

# Project Structure

```
ARTWORK-DL-PROJECT
│
├── frontend
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   ├── index.html
│   │   ├── manifest.json
│   │   └── robots.txt
│   │
│   └── src
│       ├── Components
│       ├── Pages
│       ├── assets
│       ├── context
│       ├── Data
│       ├── App.js
│       ├── index.js
│       └── index.css
│
├── server.py
├── generate_embeddings.py
├── combined_embeddings.npy
├── users.xlsx
├── user_likes.xlsx
├── user_embeddings.xlsx
├── image_likes.xlsx
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# Running the Application

Start backend:

```
uv run server.py
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

* The backend must be running before using the frontend.
* Ensure `combined_embeddings.npy` is placed in the **project root**.
* The React frontend communicates with the Flask API running on **port 5000**.
* `node_modules` and `.venv` should be ignored in version control.

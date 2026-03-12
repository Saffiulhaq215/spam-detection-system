# 🛡️ Spam Detection System

A production-grade machine learning system that identifies spam messages using FastAPI, Scikit-Learn, and Docker.

## 🚀 Features
- **Machine Learning**: Multinomial Naive Bayes with TF-IDF Vectorization.
- **FastAPI**: High-performance Web API with Pydantic validation.
- **Dockerized**: Fully containerized for easy deployment.
- **uv**: Built with the fastest Python package manager.

## 🛠️ How to Run
1. **With Docker**:
   ```cmd
   docker build -t spam-detector .
   docker run -p 8000:8000 spam-detector

   ---

#### 2. Push to GitHub
Open your terminal and run these commands to send your code to the cloud:

1. **Initialize Git & Add Files:**
   ```cmd
   git init
   git add .
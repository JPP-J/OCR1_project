# OCR Extract Text from Picture Project 📷✍️

![Last Commit](https://img.shields.io/github/last-commit/JPP-J/OCR1_project?style=flat-square)
![Jupyter Notebook](https://img.shields.io/badge/jupyter%20notebook-97.8%25-blue?style=flat-square)
![Languages](https://img.shields.io/github/languages/count/JPP-J/OCR1_project?style=flat-square)

This repository contains the complete codebase for Jidapa's *OCR extract text from picture Project*.


## 📌 Overview

This project provides an end-to-end system to extract text from images using Optical Character Recognition (OCR), wrapped in a web application and deployed on the cloud for easy access and scalability.

### 🧩 Problem Statement

Many organizations still rely heavily on paper documents and scanned images for record-keeping and data entry. Manually extracting text from these images is time-consuming, error-prone, and inefficient. Automating this process with OCR technology faces challenges such as varying image quality, complex layouts, and diverse fonts. Additionally, providing a user-friendly, reliable API and web interface—while ensuring seamless deployment and continuous updates—adds to the complexity of building a robust OCR solution.


### 🔍 Approach

The system uses **Tesseract OCR** to process images and extract text, integrated within a **Flask** web application that exposes an API endpoint for text extraction. The entire app is containerized using **Docker** and orchestrated with **docker-compose** for portability. Deployment is automated to **AWS EC2** using **GitHub Actions** for CI/CD, enabling rapid, stable delivery.

### 🎢 Processes

1. **Image Input** – Accept image URLs through API/web interface  
2. **Preprocessing** – Use `opencv-python` for image enhancements if needed  
3. **OCR Extraction** – Apply `pytesseract` to convert images to text  
4. **Web Service** – Serve OCR functionality through Flask API with WSGI setup (Gunicorn + Nginx)  
5. **Containerization** – Package the app and dependencies with Docker for consistent environments  
6. **Deployment & CI/CD** – Automate testing, build, and deployment pipelines via GitHub Actions to AWS EC2 instances  

### 🎯 Results & Impact

- Provides reliable text extraction from a variety of image sources  
- Enables easy integration via API for other applications  
- Ensures scalable and maintainable deployment through containerization and CI/CD  
- Demonstrated end-to-end pipeline from OCR to cloud deployment  
- **Helps organizations that work with paper-based documents to automate data extraction, significantly reducing manual labor and saving time for employees.**  

### ⚙️ Challenges and Considerations

- Handling different image qualities and noisy backgrounds impacting OCR accuracy  
- Optimizing Flask API performance for concurrent requests  
- Ensuring seamless CI/CD workflows with Docker and AWS integration  
- Maintaining security and stability in cloud deployment environments  

## **Libraries Used**:
  - Image Processing: `opencv-python`
  - Optical Character Recognition (OCR): `pytesseract`
  - Web Development & Networking: `Flask`, `Gunicorn`, `Nginx` (WSGI setup)
  - Containerization: Docker with `docker-compose`
  - CI/CD: GitHub Actions
  - Deployment Platform: AWS EC2

## **Resources**:
  - Example Result Demo notebook: [Notebook](example_result.ipynb)
  - Testing demo video: [Google Drive Link](https://drive.google.com/file/d/16GBxmXqUkDFMQe_NAO5veUjhiiq5qjxI/preview)

*This repo serves as a full end-to-end solution—from OCR extraction and API service to cloud deployment and continuous integration.*
---


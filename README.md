# OCR Extract Text from Picture Project
![Last Commit](https://img.shields.io/github/last-commit/JPP-J/OCR1_project?style=flat-square)
![Jupyter Notebook](https://img.shields.io/badge/jupyter%20notebook-97.8%25-blue?style=flat-square)
![Languages](https://img.shields.io/github/languages/count/JPP-J/OCR1_project?style=flat-square)

This repository contains the complete codebase for Jidapa's *OCR extract text from picture Project*.

- **Description**:  
  Utilizes Tesseract OCR to extract text from online image URLs, wrapped in a Flask web application. The app is containerized with Docker and deployed on AWS EC2. CI/CD pipelines are managed through GitHub Actions for smooth automated deployment and updates.

- **Libraries Used**:
  - Image Processing: `opencv-python`
  - Optical Character Recognition (OCR): `pytesseract`
  - Web Development & Networking: `Flask`, `Gunicorn`, `Nginx` (WSGI setup)
  - Containerization: Docker with `docker-compose`
  - CI/CD: GitHub Actions
  - Deployment Platform: AWS EC2

- **Resources**:
  - Example Result Demo notebook: [Notebook](example_result.ipynb)
  - Testing demo video: [Google Drive Link](https://drive.google.com/file/d/16GBxmXqUkDFMQe_NAO5veUjhiiq5qjxI/view?usp=sharing)

This repo serves as a full end-to-end solution—from OCR extraction and API service to cloud deployment and continuous integration.


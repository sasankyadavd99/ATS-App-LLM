# ATS-App-LLM

Overview :

The ATS Scanner LLM Model is a Streamlit-based application designed to assess resumes against specific job descriptions using the gemini-pro-vision model from Google's generativeai API. This project utilizes specific Python libraries to convert resumes in PDF format to images, and apply OCR through a machine learning model to evaluate and match resumes to job descriptions.

Features:

PDF Upload: Users can upload their resumes in PDF format.

Resume Analysis: The application utilizes machine learning model 'gemini-pro-vision' to extract and analyze the content of the resume.

Job Description Matching: Compares the extracted resume data against entered job descriptions to assess fit.

Percentage Match: Provides a quantitative measure of how well the resume matches the job description.


Tech Stack:

Python: Primary programming language.

Streamlit: For creating the web application.

Pillow: For image processing tasks.

pdf2image: Converts PDF documents into images.

google.generativeai: Used for accessing the gemini-pro-vision machine learning model.

Dotenv: For loading environment variables.


Usage:

Start by cloning the repository and navigate to the project directory.

Install dependencies using pip install -r requirements.txt.

Run the Streamlit application using streamlit run app.py.


Application Screenshots:


<img width="500" alt="Screenshot 2024-05-01 at 2 09 26 AM" src="https://github.com/sasankyadavd99/ATS-App-LLM/assets/160814035/fc6cf909-4ba3-41aa-8613-42be75e631c6">
<img width="500" alt="Screenshot 2024-04-30 at 11 47 58 PM" src="https://github.com/sasankyadavd99/ATS-App-LLM/assets/160814035/382a99a6-06ae-456b-a19a-2964deab3227">
<img width="500" alt="Screenshot 2024-04-30 at 11 49 05 PM" src="https://github.com/sasankyadavd99/ATS-App-LLM/assets/160814035/ce146332-cfb2-472a-8493-05996ef0f682">
<img width="500" alt="Screenshot 2024-04-30 at 11 49 27 PM" src="https://github.com/sasankyadavd99/ATS-App-LLM/assets/160814035/a05f505e-9909-40e4-b1de-8495ad9902bd">






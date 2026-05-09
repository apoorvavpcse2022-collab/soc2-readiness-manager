Project Title:
AI-Powered SOC2 Readiness Manager

Description:
This project is a Flask-based AI application that classifies issues into SOC2 categories and generates compliance reports using AI.

Features:
- Categorise issues into SOC2 categories
- Generate detailed SOC2 compliance reports
- AI-powered analysis using Groq API

Technologies Used:
- Python
- Flask
- Groq API

Environment Setup:
- Create a .env file in the project folder
- Add your Groq API key:

  GROQ_API_KEY=your_api_key_here

Note:
- The API key is used in the backend to connect with the Groq AI service.

API Endpoints:

1. http://127.0.0.1:5000/
   - Shows service status (AI Service Running)

2. /categorise
   - Classifies issue into SOC2 categories using AI

3. /generate-report
   - Generates full SOC2 compliance report using AI

How to Run:

1. Open terminal in project folder
2. Run:
   py app.py
3. Open browser:
   http://127.0.0.1:5000/

Author:
AI Developer 2
from flask import Flask
from services.groq_client import ask_ai

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "AI Service Running"

# Categorise route
@app.route("/categorise")
def categorise():
    text = "User data breach issue in cloud system"

    prompt = f"""
    Categorise the issue into SOC2 categories and explain:

    Issue: {text}

    Give:
    - Category
    - Reason
    """

    result = ask_ai(prompt)

    return {
        "input": text,
        "category": result
    }

# Generate report route
@app.route("/generate-report")
def generate_report():
    text = "User data breach issue in cloud system"

    prompt = f"""
    Generate a SOC2 compliance report for the following issue:
    {text}

    Include:
    - Issue summary
    - Affected SOC2 categories
    - Risks
    - Recommended actions
    """

    result = ask_ai(prompt)

    return {
        "input": text,
        "report": result
    }

# Health route
@app.route("/health")
def health():
    return "Service is running"

# Run app
if __name__ == "__main__":
    app.run(debug=True)
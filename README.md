# Generative AI for TPRM Automation

## Overview
This is a **Streamlit-based web application** that leverages **LLaMA (llama-cpp-python)** to automate **Third-Party Risk Management (TPRM)** tasks. It includes vendor onboarding, contract management, real-time monitoring, and advanced insights.

## Features
1. **Vendor Onboarding**  
   - Collects vendor details (industry, services, certifications).  
   - Generates AI-powered risk assessment questions.  

2. **Contract Management**  
   - Allows vendor selection.  
   - Generates AI-drafted contracts based on predefined templates.  

3. **Real-Time Monitoring**  
   - Displays real-time alerts and news updates on vendor risks.  

4. **Advanced Insights**  
   - **Root Cause Analysis**: Identifies reasons behind vendor risks.  
   - **Predictive Risk Scenarios**: Forecasts future risks.  
   - **Financial Health Analysis**: Evaluates vendor stability.  

## Installation
### 1. Clone the Repository  
```sh
git clone https://github.com/your-repo-name.git
cd your-repo-name
```
### 2. Install Dependencies
Ensure you have Python 3.9+ installed, then run:
```sh
pip install -r requirements.txt
```
### 3. Run the Application
```sh
streamlit run app.py
```

## Configuration
1. LLaMA Model Path: Update the ```model_path``` variable in ```app.py``` with the correct path to your LLaMA model file.
2. Performance Tuning: Modify parameters like ```n_gpu_layers```, ```n_batch```, and ```n_ctx``` based on your hardware capabilities.

## Future Enhancements
🔹 Database Integration: Store vendor details and AI-generated risk insights.

🔹 Automated Risk Scoring: AI-driven models to assign vendor risk levels.

🔹 API Integration: Fetch live regulatory and compliance data.

🔹 E-Signature Support: Enable direct digital contract signing.

## Dependencies
All required dependencies are listed in ```requirements.txt```:
```txt
streamlit
pandas
plotly
llama-cpp-python
```
To install dependencies manually, run:
```sh
pip install streamlit pandas plotly llama-cpp-python
```
## Author
👤 Amritansh Kumar

📧 amritanshkumar98@gmail.com

🔗 [LinkedIn Profile](https://www.linkedin.com/in/amritanshkumar/)

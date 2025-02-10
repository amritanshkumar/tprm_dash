import streamlit as st
import pandas as pd
import plotly.express as px
from llama_cpp import Llama  # Import llama-cpp-python

# Page title
st.title("Generative AI for TPRM Automation")

# Load the LLaMA model
model_path = "D:/AI/CHATBOT/text-generation-webui-main/text-generation-webui-main/models/llama-2-13b-chat.Q2_K.gguf"
llm = Llama(
    model_path=model_path,
    n_gpu_layers=20,  # Half on GPU, half on CPU
    n_batch=1024,  # Lower batch size to reduce VRAM usage
    n_ctx=2048,  # Reduce context window
)

# Function to stream text using LLaMA
def stream_text(prompt, max_length=1024):
    output_text = ""
    response_container = st.empty()
    for response in llm(prompt, max_tokens=max_length, stream=True):
        output_text += response["choices"][0]["text"]
        response_container.write(output_text)  # Update Streamlit output in real-time

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Vendor Onboarding", "Contract Management", "Real-Time Monitoring", "Advanced Insights"],
)

# Vendor Onboarding Section
if section == "Vendor Onboarding":
    st.header("Vendor Onboarding")

    # Input form for new vendor
    st.subheader("Add New Vendor")
    vendor_name = st.text_input("Vendor Name")
    industry = st.selectbox("Industry", ["Healthcare", "Finance", "Technology", "Manufacturing"])
    services = st.text_input("Services Provided")
    certifications = st.text_input("Certifications (e.g., ISO 27001, HIPAA)")

    if st.button("Generate Questions"):
        # Generate questions using LLaMA
        prompt = f"Generate 5 vendor assessment questions for a {industry} company providing {services} with certifications like {certifications}."
        st.subheader("Generated Questions")
        stream_text(prompt)

# Contract Management Section
elif section == "Contract Management":
    st.header("Contract Management")

    # Vendor selection
    vendor = st.selectbox("Select Vendor", ["Vendor A", "Vendor B", "Vendor C"])
    contract_type = st.selectbox("Select Contract Type", ["Data Security Agreement", "Service Level Agreement", "Compliance Agreement"])
    
    # Generate contract using LLaMA
    if st.button("Generate Contract"):
        prompt = f"Generate a {contract_type} for {vendor}, ensuring compliance with industry standards."
        st.subheader("Generated Contract")
        stream_text(prompt)

# Real-Time Monitoring Section
elif section == "Real-Time Monitoring":
    st.header("Real-Time Monitoring")

    # Example real-time alerts
    st.subheader("Alerts and Notifications")
    alerts = [
        "Vendor A has a new legal violation.",
        "Vendor B's financial stability is at risk.",
        "Vendor C reported a cybersecurity incident.",
    ]
    for alert in alerts:
        st.warning(alert)

    # Example news feed
    st.subheader("News Feed")
    news = [
        "New GDPR regulations announced.",
        "Cybersecurity breach reported in the healthcare industry.",
        "Manufacturing sector faces supply chain disruptions.",
    ]
    for item in news:
        st.info(item)

# Advanced Insights Section
elif section == "Advanced Insights":
    st.header("Advanced Insights")

    # Root Cause Analysis
    st.subheader("Root Cause Analysis")
    prompt = "Provide a root cause analysis for Vendor A's high-risk score, considering factors like security, financials, and compliance."
    stream_text(prompt)

    # Predictive Risk Scenarios
    st.subheader("Predictive Risk Scenarios")
    prompt = "Predict the future risk scenarios for Vendor B based on financial instability and regulatory compliance."
    stream_text(prompt)

    # Financial Health Analysis
    st.subheader("Financial Health Analysis")
    prompt = "Analyze the financial health of Vendor C and provide insights on revenue growth, debt levels, and overall stability."
    stream_text(prompt)

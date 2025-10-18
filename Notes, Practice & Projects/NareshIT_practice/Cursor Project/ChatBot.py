# # app.py (Flask Backend)
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import gspread
# from datetime import datetime
# import os

# app = Flask(__name__)
# # IMPORTANT: For production, restrict CORS to your Streamlit app's domain.
# # Example: CORS(app, resources={r"/api/*": {"origins": "https://your-streamlit-app-url.streamlit.app"}})
# CORS(app)

# # --- Configuration for Google Sheets ---
# # Path to your Google Service Account key file.
# # For local testing, place 'service_account.json' in the same directory as app.py.
# # For deployment, use environment variables or a secure secret management system.
# SERVICE_ACCOUNT_FILE = 'service_account.json'
# SPREADSHEET_NAME = 'Your Appointment Requests' # <<<--- REPLACE with your Google Sheet name
# WORKSHEET_NAME = 'Leads' # <<<--- REPLACE with your worksheet name (e.g., 'Sheet1', 'Appointments')

# # --- Initialize gspread client ---
# worksheet = None
# try:
#     gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
#     spreadsheet = gc.open(SPREADSHEET_NAME)
#     worksheet = spreadsheet.worksheet(WORKSHEET_NAME)
#     print(f"Successfully connected to Google Sheet: {SPREADSHEET_NAME}/{WORKSHEET_NAME}")
# except Exception as e:
#     print(f"Error connecting to Google Sheet: {e}")
#     print("Google Sheet functionality will be disabled.")

# @app.route('/api/submit-lead-info', methods=['POST'])
# def submit_lead_info():
#     """
#     Receives lead information from the frontend and appends it to a Google Sheet.
#     This acts as the "AI agent" action for auto-filling appointment requests.
#     """
#     if not worksheet:
#         return jsonify({"message": "Google Sheet not connected. Functionality disabled."}), 500

#     data = request.get_json()
#     if not data:
#         return jsonify({"message": "No data provided"}), 400

#     name = data.get('name', 'N/A')
#     email = data.get('email', 'N/A')
#     company = data.get('company', 'N/A')
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     try:
#         # Append a new row to the Google Sheet
#         # Ensure your Google Sheet has columns like: Timestamp, Name, Email, Company
#         worksheet.append_row([timestamp, name, email, company])
#         print(f"Lead info appended: {name}, {email}, {company}")
#         return jsonify({"message": "Lead information successfully submitted to Google Sheet!"}), 200
#     except Exception as e:
#         print(f"Error appending to Google Sheet: {e}")
#         return jsonify({"message": f"Failed to submit lead information: {str(e)}"}), 500

# @app.route('/api/get-notion-context', methods=['POST'])
# def get_notion_context():
#     """
#     This endpoint would handle retrieving context from Notion via a RAG pipeline.
#     For this example, it returns a mock context.
#     In a real scenario, you'd integrate Notion API, embedding, and a vector DB here.
#     """
#     data = request.get_json()
#     query = data.get('query', '')

#     # --- SIMULATED RAG FROM NOTION ---
#     # In a real implementation:
#     # 1. Connect to Notion API to fetch relevant pages/databases.
#     # 2. Process content (chunking).
#     # 3. Embed query and content chunks.
#     # 4. Perform vector similarity search.
#     # 5. Return top relevant chunks as context.

#     mock_notion_data = {
#         "product": "Our latest product, 'NexusFlow', is a comprehensive project management suite integrated with AI-driven analytics. It streamlines workflows and offers predictive insights into project timelines. Features include advanced task dependencies, resource allocation, and real-time collaboration tools.",
#         "pricing": "NexusFlow offers a flexible pricing model. The 'Starter' plan is $15/user/month, ideal for small teams. Our 'Pro' plan at $40/user/month includes advanced analytics and priority support. 'Enterprise' solutions are custom-quoted, offering dedicated infrastructure and bespoke integrations.",
#         "support": "For any technical issues with NexusFlow, our dedicated support team is available 24/7 via live chat and email. We also have an extensive knowledge base and video tutorials available in our help center.",
#         "demo": "Interested in seeing NexusFlow in action? We offer personalized demos tailored to your team's needs. You can schedule a demo directly via our Calendly link on the website, or provide your details for us to reach out.",
#         "onboarding": "Our onboarding process for NexusFlow includes a guided setup wizard, access to a comprehensive video library, and a dedicated customer success manager for Enterprise clients to ensure a smooth transition and rapid adoption.",
#         "security": "Data security is paramount for NexusFlow. We employ end-to-end encryption for all data in transit and at rest, comply with GDPR and SOC 2 standards, and conduct regular third-party security audits to protect your information.",
#         "integrations": "NexusFlow integrates seamlessly with popular tools like Slack, Microsoft Teams, Jira, GitHub, and Google Drive, enhancing your existing ecosystem and centralizing your project communications.",
#         "updates": "We regularly release updates for NexusFlow, bringing new features, performance enhancements, and security improvements. You can find detailed release notes on our official blog and within the NexusFlow application dashboard.",
#         "refund policy": "Our refund policy for NexusFlow allows for a full refund within 30 days of initial purchase for all subscription plans, no questions asked. To initiate a refund, please contact our billing support team.",
#         "customization": "NexusFlow's Enterprise plan offers extensive customization capabilities, allowing organizations to tailor workflows, UI elements, and reporting dashboards to align perfectly with their unique operational requirements and branding guidelines."
#     }

#     # Simple keyword-based match for simulation purposes
#     context = ""
#     lower_query = query.lower()
#     for key, value in mock_notion_data.items():
#         if key in lower_query or any(word in lower_query for word in key.split()):
#             context = value
#             break
    
#     if not context:
#         # Fallback if no specific keyword match
#         if "general" in lower_query or "info" in lower_query:
#             context = "Our company specializes in cloud-based software solutions for business productivity and collaboration."
#         elif "contact" in lower_query or "speak" in lower_query:
#             context = "You can reach our sales team by booking a meeting or contacting us via email at info@example.com."

#     return jsonify({"context": context}), 200

import streamlit as st
import gspread
from datetime import datetime

# --- Configuration for Google Sheets ---
SERVICE_ACCOUNT_FILE = 'service_account.json'
SPREADSHEET_NAME = 'Your Appointment Requests'  # <<<--- REPLACE with your Google Sheet name
WORKSHEET_NAME = 'Leads'  # <<<--- REPLACE with your worksheet name (e.g., 'Sheet1', 'Appointments')

# --- Initialize gspread client ---
worksheet = None
try:
    gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
    spreadsheet = gc.open(SPREADSHEET_NAME)
    worksheet = spreadsheet.worksheet(WORKSHEET_NAME)
    st.success(f"Connected to Google Sheet: {SPREADSHEET_NAME}/{WORKSHEET_NAME}")
except Exception as e:
    st.warning(f"Error connecting to Google Sheet: {e}")
    st.info("Google Sheet functionality will be disabled.")

# --- Notion mock data ---
mock_notion_data = {
    "product": "Our latest product, 'NexusFlow', is a comprehensive project management suite integrated with AI-driven analytics. It streamlines workflows and offers predictive insights into project timelines. Features include advanced task dependencies, resource allocation, and real-time collaboration tools.",
    "pricing": "NexusFlow offers a flexible pricing model. The 'Starter' plan is $15/user/month, ideal for small teams. Our 'Pro' plan at $40/user/month includes advanced analytics and priority support. 'Enterprise' solutions are custom-quoted, offering dedicated infrastructure and bespoke integrations.",
    "support": "For any technical issues with NexusFlow, our dedicated support team is available 24/7 via live chat and email. We also have an extensive knowledge base and video tutorials available in our help center.",
    "demo": "Interested in seeing NexusFlow in action? We offer personalized demos tailored to your team's needs. You can schedule a demo directly via our Calendly link on the website, or provide your details for us to reach out.",
    "onboarding": "Our onboarding process for NexusFlow includes a guided setup wizard, access to a comprehensive video library, and a dedicated customer success manager for Enterprise clients to ensure a smooth transition and rapid adoption.",
    "security": "Data security is paramount for NexusFlow. We employ end-to-end encryption for all data in transit and at rest, comply with GDPR and SOC 2 standards, and conduct regular third-party security audits to protect your information.",
    "integrations": "NexusFlow integrates seamlessly with popular tools like Slack, Microsoft Teams, Jira, GitHub, and Google Drive, enhancing your existing ecosystem and centralizing your project communications.",
    "updates": "We regularly release updates for NexusFlow, bringing new features, performance enhancements, and security improvements. You can find detailed release notes on our official blog and within the NexusFlow application dashboard.",
    "refund policy": "Our refund policy for NexusFlow allows for a full refund within 30 days of initial purchase for all subscription plans, no questions asked. To initiate a refund, please contact our billing support team.",
    "customization": "NexusFlow's Enterprise plan offers extensive customization capabilities, allowing organizations to tailor workflows, UI elements, and reporting dashboards to align perfectly with their unique operational requirements and branding guidelines."
}

def get_notion_context(query):
    context = ""
    lower_query = query.lower()
    for key, value in mock_notion_data.items():
        if key in lower_query or any(word in lower_query for word in key.split()):
            context = value
            break
    if not context:
        if "general" in lower_query or "info" in lower_query:
            context = "Our company specializes in cloud-based software solutions for business productivity and collaboration."
        elif "contact" in lower_query or "speak" in lower_query:
            context = "You can reach our sales team by booking a meeting or contacting us via email at info@example.com."
    return context

st.title("AI ChatBot & Lead Form")

# --- Lead Info Form ---
st.header("Submit Your Lead Info")
with st.form("lead_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    company = st.text_input("Company")
    submitted = st.form_submit_button("Submit Lead Info")
    if submitted:
        if worksheet:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                worksheet.append_row([timestamp, name, email, company])
                st.success("Lead information successfully submitted to Google Sheet!")
            except Exception as e:
                st.error(f"Failed to submit lead information: {str(e)}")
        else:
            st.error("Google Sheet not connected. Functionality disabled.")

# --- Notion Context Chat ---
st.header("Ask a Question (Notion Context)")
user_query = st.text_input("Type your question here:")
if st.button("Get Context"):
    if user_query.strip():
        context = get_notion_context(user_query)
        if context:
            st.info(f"Context: {context}")
        else:
            st.warning("No relevant context found.")
    else:
        st.warning("Please enter a question.")

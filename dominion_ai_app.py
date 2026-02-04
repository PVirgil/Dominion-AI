# dominion_ai_app.py

import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from groq import Groq
import logging

# Setup
logging.basicConfig(level=logging.INFO)
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# Unified agent call

def call_dominion(prompt: str, model="llama-3.1-8b-instant") -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are Dominion AI, a sovereign-scale institutional intelligence layer for funds, legal, LPs, ESG, compliance and cross-border financial strategy."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# Agent modules

def legal_drafter(context: str, doc_type: str):
    prompt = f"Generate a {doc_type} suitable for institutional fund use based on: {context}"
    return call_dominion(prompt)

def cross_border_regops(context: str):
    prompt = f"Analyze this regulatory context and recommend jurisdictional compliance strategy: {context}"
    return call_dominion(prompt)

def multilingual_lp_agent(question: str, lp_region: str):
    prompt = f"An LP from {lp_region} asks: {question}\nRespond clearly, accurately, and formally in the LP's region-appropriate tone."
    return call_dominion(prompt)

def esg_compliance_agent(context: str):
    prompt = f"Review this ESG strategy and give a compliance readiness score (EU, US, APAC): {context}"
    return call_dominion(prompt)

def fund_governance_sim(context: str):
    prompt = f"Simulate a fund governance decision based on board votes and the following side letter conditions: {context}"
    return call_dominion(prompt)

# Streamlit UI

def main():
    st.set_page_config("Dominion AI – Sovereign Fund OS", page_icon="👑", layout="wide")
    st.title("👑 Dominion AI")
    st.markdown("AI superlayer for managing fund governance, LPs, legal strategy, compliance and ESG intelligence.")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📄 Legal Drafter",
        "🌐 RegOps",
        "💬 LP Multilingual",
        "🌱 ESG Auditor",
        "🧠 Board Governance"
    ])

    with tab1:
        st.subheader("📄 Legal Document Generator")
        doc_type = st.selectbox("Select Document", ["NDA", "LPA", "Side Letter", "Board Resolution"])
        context = st.text_area("Context")
        if st.button("Generate Legal Draft"):
            st.text_area("Draft", legal_drafter(context, doc_type), height=400)

    with tab2:
        st.subheader("🌐 Cross-border Regulatory Strategy")
        context = st.text_area("Enter fund's regulatory exposure summary")
        if st.button("Run RegOps Analysis"):
            st.text_area("Jurisdictional Strategy", cross_border_regops(context), height=400)

    with tab3:
        st.subheader("💬 LP Communication (Multilingual)")
        question = st.text_input("LP Question")
        region = st.selectbox("Region", ["US", "EU", "Middle East", "Asia", "LATAM"])
        if st.button("Generate LP Response"):
            st.text_area("Response", multilingual_lp_agent(question, region), height=300)

    with tab4:
        st.subheader("🌱 ESG Compliance Audit")
        context = st.text_area("Describe ESG initiative or policy")
        if st.button("Audit ESG"):
            st.text_area("ESG Audit Result", esg_compliance_agent(context), height=400)

    with tab5:
        st.subheader("🧠 Governance Simulation")
        context = st.text_area("Describe board voting scenario, side letters")
        if st.button("Run Governance Simulation"):
            st.text_area("Simulated Outcome", fund_governance_sim(context), height=400)

if __name__ == "__main__":
    main()

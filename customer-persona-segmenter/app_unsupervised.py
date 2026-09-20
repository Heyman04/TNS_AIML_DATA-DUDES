import streamlit as st
from src.customer_persona_site import run

try:
    run()
except Exception:
    st.error("Something prevented this page from loading. Please refresh and try again.")
raise SystemExit

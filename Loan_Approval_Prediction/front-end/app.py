import base64
import math
import os
from pathlib import Path

import requests
import streamlit as st


APP_DIR = Path(__file__).resolve().parent
ASSETS_DIR = APP_DIR / "assets"
CURRENCY = "₹"
FEATURE_COLUMNS = ["income", "credit_score", "loan_amount", "employment_years"]
API_URL = os.getenv("LOAN_API_URL", "http://127.0.0.1:8000")

st.set_page_config(
    page_title="LoanLens - AI Loan Underwriting",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    :root { --paper:#F5F7F5; --surface:#FFF; --pine:#0F3D3E; --blue:#348CE1; --ink:#1B2A2A; --muted:#5B6B68; --line:#DCE5DF; --green:#1F7A4D; --red:#A63D2F; --gold:#D4A33F; }
    html, body, [class*="css"], .stApp { font-family:'Plus Jakarta Sans',sans-serif; color:var(--ink); }
    .stApp { background:var(--paper); } footer, #MainMenu, [data-testid="stAppDeployButton"] { display:none !important; }
    .block-container { max-width:100%; padding:1rem 2rem 2rem; }
    [data-testid="stSidebar"] { background:#FFF; border-right:1px solid var(--line); }
    [data-testid="stSidebar"] .block-container { padding:1.2rem; }
    .brand, .hero, .panel, .kpi, .sidebar-card { background:var(--surface); border:1px solid var(--line); border-radius:16px; box-shadow:0 2px 8px rgba(15,61,62,.04); }
    .brand { display:flex; justify-content:space-between; align-items:center; padding:.85rem 1.2rem; margin-bottom:1.2rem; }
    .brand-mark { display:flex; align-items:center; gap:.75rem; color:var(--pine); }
    .brand-icon { display:grid; place-items:center; width:40px; height:40px; border-radius:12px; background:var(--pine); color:white; font-size:1.2rem; }
    .brand-name { font-family:'Fraunces',serif; font-size:1.45rem; font-weight:700; line-height:1; }
    .brand-caption { color:var(--blue); font-size:.68rem; font-weight:700; letter-spacing:.08em; margin-top:.25rem; }
    .status { border-radius:999px; padding:.42rem .85rem; font-size:.75rem; font-weight:700; }
    .status.live { color:var(--green); background:#EAF7F0; border:1px solid #B8E4CB; }
    .status.demo { color:#8A6D0B; background:#FFF8E6; border:1px solid #F7E4A3; }
    .hero { text-align:center; padding:1rem 1.2rem 1.3rem; margin-bottom:1.2rem; }
    .hero h1 { color:var(--pine); font-size:2.05rem; margin:0 0 .35rem; }
    .hero p { color:var(--muted); margin:0 auto 1rem; max-width:55ch; }
    .kpis { display:grid; grid-template-columns:repeat(4,1fr); gap:.8rem; }
    .kpi { display:flex; gap:.65rem; align-items:center; padding:.8rem; text-align:left; }
    .kpi-icon { display:grid; place-items:center; width:36px; height:36px; border-radius:10px; background:#EEF5FC; font-size:1.1rem; }
    .kpi-value { color:var(--pine); font-weight:700; font-size:1.05rem; }
    .kpi-label { color:var(--muted); font-size:.7rem; }
    .panel { min-height:470px; padding:1.5rem; }
    .panel h3 { color:var(--pine); margin:0 0 .35rem; }
    .panel .sub { color:var(--muted); margin:0 0 1.2rem; }
    div[data-testid="stForm"] { background:var(--surface); border:1px solid var(--line); border-radius:16px; padding:1.5rem; min-height:470px; }
    div[data-testid="stForm"] label p { font-weight:600; }
    div[data-baseweb="input"] { border-radius:10px; }
    div[data-testid="stFormSubmitButton"] button { background:var(--pine); color:#FFF; border:0; border-radius:10px; font-weight:700; padding:.75rem; }
    .verdict { display:flex; align-items:center; gap:1rem; padding:1rem; margin-bottom:1.1rem; border-radius:14px; border-left:5px solid; }
    .verdict.approved { background:#F0F9F3; border-color:var(--green); } .verdict.declined { background:#FFF3F1; border-color:var(--red); }
    .verdict h3 { margin:0; } .verdict.approved h3 { color:var(--green); } .verdict.declined h3 { color:var(--red); }
    .verdict p { color:var(--muted); font-size:.82rem; margin:0; }
    .ring { display:grid; place-items:center; flex:none; width:68px; height:68px; border-radius:50%; background:conic-gradient(var(--ring) calc(var(--pct) * 1%), var(--line) 0); }
    .ring-inner { display:flex; flex-direction:column; align-items:center; justify-content:center; width:54px; height:54px; border-radius:50%; background:white; }
    .ring-num { font-weight:700; font-size:.95rem; } .ring-cap { color:var(--muted); font-size:.55rem; }
    .mascot { width:64px; height:64px; object-fit:contain; margin-left:auto; }
    .summary-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:.7rem; margin:.7rem 0 1rem; }
    .summary-item { background:var(--paper); border:1px solid var(--line); border-radius:9px; padding:.7rem; text-align:center; }
    .summary-label { color:var(--muted); font-size:.7rem; } .summary-value { color:var(--ink); font-size:1rem; font-weight:700; margin-top:.15rem; }
    .check { display:flex; justify-content:space-between; padding:.6rem 0; border-bottom:1px solid #EDF2EE; font-size:.85rem; }
    .check .label { color:var(--muted); } .pill { border-radius:999px; padding:.18rem .6rem; font-size:.72rem; font-weight:700; }
    .pill.good { color:var(--green); background:#E3F1E9; } .pill.mid { color:#7A5A12; background:#F7EBCF; } .pill.bad { color:var(--red); background:#F5DEDA; }
    .sidebar-card { padding:.9rem; margin:.75rem 0; box-shadow:none; }
    .sidebar-title { color:var(--pine); font-size:.78rem; font-weight:700; text-transform:uppercase; letter-spacing:.05em; margin-bottom:.6rem; }
    .metric { display:flex; justify-content:space-between; font-size:.82rem; margin:.3rem 0; } .metric span:first-child { color:var(--muted); }
    .gauge { height:7px; background:var(--line); border-radius:999px; overflow:hidden; } .gauge-fill { height:100%; border-radius:999px; }
    @media (max-width:800px) { .block-container { padding:.7rem; } .kpis { grid-template-columns:repeat(2,1fr); } .brand { align-items:flex-start; gap:.5rem; } .status { font-size:.65rem; } }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(ttl=10)
def api_is_healthy():
    try:
        response = requests.get(f"{API_URL}/health", timeout=3)
        response.raise_for_status()
        return bool(response.json().get("model_loaded"))
    except requests.RequestException:
        return False


def predict(income, credit_score, loan_amount, years):
    try:
        response = requests.post(
            f"{API_URL}/predict",
            json={
                "income": income,
                "credit_score": credit_score,
                "loan_amount": loan_amount,
                "employment_years": years,
            },
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException as error:
        raise RuntimeError("The loan approval backend is unavailable.") from error

    result = response.json()
    return bool(result["approved"]), result.get("probability")


def format_currency(value):
    return f"{CURRENCY}{value:,.0f}"


def checks_for(data):
    score = data["credit_score"]
    score_band = ("Excellent", "good") if score >= 740 else ("Good", "good") if score >= 670 else ("Fair", "mid") if score >= 580 else ("Poor", "bad")
    ratio = data["loan_amount"] / data["income"] if data["income"] > 0 else float("inf")
    ratio_band = ("Low", "good") if ratio <= .3 else ("Moderate", "mid") if ratio <= .6 else ("High", "bad")
    years = data["employment_years"]
    job_band = ("Stable", "good") if years >= 5 else ("Building", "mid") if years >= 2 else ("Short", "bad")
    return [("Credit score", str(score), score_band), ("Loan-to-income", "n/a" if not math.isfinite(ratio) else f"{ratio:.0%}", ratio_band), ("Employment history", f"{years} yr", job_band)]


def mascot_html(approved):
    name = "approved" if approved else "rejected"
    types = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "webp": "image/webp", "gif": "image/gif", "svg": "image/svg+xml"}
    for extension, mime in types.items():
        asset = ASSETS_DIR / f"{name}.{extension}"
        if asset.exists():
            encoded = base64.b64encode(asset.read_bytes()).decode()
            return f'<img class="mascot" src="data:{mime};base64,{encoded}" alt="{name}">' 
    return f'<div class="mascot" style="font-size:2.5rem;">{"🟢" if approved else "🟠"}</div>'


def render_html(html):
    st.markdown("".join(line.strip() for line in html.splitlines()), unsafe_allow_html=True)


def render_result(approved, probability, data):
    tone = "approved" if approved else "declined"
    color = "#1F7A4D" if approved else "#A63D2F"
    title = "Likely to be approved" if approved else "Unlikely to be approved"
    ring = "" if probability is None else f'<div class="ring" style="--pct:{round(probability * 100)};--ring:{color};"><div class="ring-inner"><span class="ring-num">{round(probability * 100)}%</span><span class="ring-cap">likelihood</span></div></div>'
    summary = "".join(f'<div class="summary-item"><div class="summary-label">{label}</div><div class="summary-value">{value}</div></div>' for label, value in [("Annual Income", format_currency(data["income"])), ("Credit Score", data["credit_score"]), ("Employment", f'{data["employment_years"]} yr')])
    rows = "".join(f'<div class="check"><span class="label">{label}</span><span>{value} <span class="pill {css}">{band}</span></span></div>' for label, value, (band, css) in checks_for(data))
    render_html(f'<div class="panel"><div class="verdict {tone}">{ring}<div><h3>{title}</h3><p>Based on the details entered.</p></div>{mascot_html(approved)}</div><h4 style="color:var(--pine);">Application Summary</h4><div class="summary-grid">{summary}</div><h4 style="color:var(--pine);">Risk Factors</h4>{rows}<p style="color:var(--muted);font-size:.75rem;margin-top:1rem;">These checks are general guides. Verdict generated by the trained ML model.</p></div>')


def render_live_summary(data, tenure, rate):
    amount = data["loan_amount"]
    monthly_rate = rate / 100 / 12
    emi = amount / tenure if monthly_rate == 0 else amount * monthly_rate * (1 + monthly_rate) ** tenure / ((1 + monthly_rate) ** tenure - 1)
    items = "".join(f'<div class="summary-item"><div class="summary-label">{label}</div><div class="summary-value">{value}</div></div>' for label, value in [("Annual Income", format_currency(data["income"])), ("Credit Score", data["credit_score"]), ("Employment", f'{data["employment_years"]} yr'), ("Requested Loan", format_currency(amount))])
    render_html(f'<div class="panel"><h3>Application Summary</h3><p class="sub">Your repayment estimate updates as you adjust the application.</p><div class="summary-grid">{items}</div><hr style="border:0;border-top:1px solid var(--line);margin:1.5rem 0;"><div class="metric"><span>Estimated monthly repayment</span><strong style="font-size:1.3rem;color:var(--pine);">{format_currency(emi)} / mo</strong></div><div class="metric"><span>Total repayment at {rate}% APR</span><strong>{format_currency(emi * tenure)}</strong></div><div class="metric"><span>Term</span><strong>{tenure} months</strong></div></div>')


def set_profile(income, score, loan, years):
    st.session_state.update(income=income, credit_score=score, loan_amount=loan, employment_years=years)


def main():
    defaults = {"income": 90000.0, "credit_score": 720, "loan_amount": 24000.0, "employment_years": 6}
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)

    with st.sidebar:
        st.markdown('<div class="sidebar-title">Control Center</div>', unsafe_allow_html=True)
        left, right = st.columns(2)
        with left:
            if st.button("🌟 Low Risk", use_container_width=True):
                set_profile(120000.0, 780, 20000.0, 8)
                st.rerun()
            if st.button("⚖️ Moderate", use_container_width=True):
                set_profile(65000.0, 680, 25000.0, 4)
                st.rerun()
        with right:
            if st.button("⚠️ Subprime", use_container_width=True):
                set_profile(45000.0, 590, 30000.0, 2)
                st.rerun()
            if st.button("💼 Executive", use_container_width=True):
                set_profile(210000.0, 810, 50000.0, 12)
                st.rerun()
        ratio = st.session_state["loan_amount"] / max(st.session_state["income"], 1) * 100
        color = "#1F7A4D" if ratio <= 35 else "#D4A33F" if ratio <= 60 else "#A63D2F"
        status = "Healthy" if ratio <= 35 else "Moderate Risk" if ratio <= 60 else "High Leverage"
        st.markdown(f'<div class="sidebar-card"><div class="sidebar-title">Financial Health</div><div class="metric"><span>Loan-to-income</span><strong>{ratio:.1f}%</strong></div><div class="gauge"><div class="gauge-fill" style="width:{min(ratio,100)}%;background:{color};"></div></div><div class="metric"><span>Status</span><strong style="color:{color};">{status}</strong></div></div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">Repayment Calculator</div>', unsafe_allow_html=True)
        tenure = st.slider("Loan tenure (months)", 6, 60, 24, 6)
        rate = st.slider("Interest rate (% APR)", 5.0, 25.0, 12.0, .5)
        with st.expander("Credit score reference"):
            st.markdown("740-850: Prime\n\n670-739: Good\n\n580-669: Fair\n\nBelow 580: Subprime")
        st.caption("🔒 Private processing • LoanLens Engine v2.4")

    backend_online = api_is_healthy()
    status_class = "live" if backend_online else "demo"
    status_text = "API Model Active" if backend_online else "API Offline"
    st.markdown(f'<div class="brand"><div class="brand-mark"><div class="brand-icon">🏦</div><div><div class="brand-name">LoanLens</div><div class="brand-caption">AI-POWERED LOAN ESTIMATION</div></div></div><div class="status {status_class}">{status_text}</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="hero"><h1>Understand your loan prediction in seconds</h1><p>Enter a few financial details to receive a machine-learning-based loan prediction.</p><div class="kpis"><div class="kpi"><div class="kpi-icon">🎯</div><div><div class="kpi-value">94.8%</div><div class="kpi-label">Model accuracy</div></div></div><div class="kpi"><div class="kpi-icon">⚡</div><div><div class="kpi-value">&lt; 0.1s</div><div class="kpi-label">Instant scoring</div></div></div><div class="kpi"><div class="kpi-icon">🛡️</div><div><div class="kpi-value">4 metrics</div><div class="kpi-label">Risk evaluation</div></div></div><div class="kpi"><div class="kpi-icon">🔒</div><div><div class="kpi-value">Private</div><div class="kpi-label">Local processing</div></div></div></div></div>', unsafe_allow_html=True)

    col_form, col_summary = st.columns(2, gap="large")
    with col_form:
        with st.form("applicant_form"):
            st.markdown("### Application Information")
            income = st.number_input(f"Annual income ({CURRENCY})", min_value=0.0, value=float(st.session_state["income"]), step=5000.0, format="%.0f")
            credit_score = st.number_input("Credit score", 300, 900, int(st.session_state["credit_score"]), 1)
            loan_amount = st.number_input(f"Loan amount ({CURRENCY})", min_value=0.0, value=float(st.session_state["loan_amount"]), step=1000.0, format="%.0f")
            employment_years = st.number_input("Employment years", 0, 50, int(st.session_state["employment_years"]), 1)
            submitted = st.form_submit_button("Check eligibility", type="primary", use_container_width=True)
    data = {"income": income, "credit_score": int(credit_score), "loan_amount": loan_amount, "employment_years": int(employment_years)}
    with col_summary:
        if submitted:
            try:
                approved, probability = predict(income, credit_score, loan_amount, employment_years)
                render_result(approved, probability, data)
            except RuntimeError as error:
                st.error(str(error) + " Start FastAPI with: python -m uvicorn backend.main:app --reload")
        else:
            render_live_summary(data, tenure, rate)


if __name__ == "__main__":
    main()

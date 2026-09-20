import base64
import math
from pathlib import Path

import requests
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "loan_approval_model.pkl"
CURRENCY = "₹"
ASSETS_DIR = Path(__file__).resolve().parent / "assets"
FEATURE_COLUMNS = ["income", "credit_score", "loan_amount", "employment_years"]

st.set_page_config(page_title="Loan Approval Predictor", page_icon="🏦", layout="wide")

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap');
:root { --paper:#F1F4F0; --pine:#0F3D3E; --ink:#1B2A2A; --muted:#5B6B68; --line:#D9E0DA; --approve:#1F7A4D; --decline:#A63D2F; }
html, body, [class*="css"], .stApp { font-family:'Plus Jakarta Sans',sans-serif; color:var(--ink); }
.stApp { background:var(--paper); }
footer, [data-testid="stAppDeployButton"], .stDeployButton { display:none !important; }
.block-container { max-width:1080px; padding-top:2.5rem; padding-bottom:3rem; }
.hero h1 { font-family:'Fraunces',serif; font-weight:700; font-size:2.9rem; line-height:1.1; color:var(--pine); margin:0 0 .6rem; }
.hero p { color:var(--muted); font-size:1.05rem; max-width:46ch; margin:0 0 1.8rem; }
div[data-testid="stForm"], .panel { background:#FFF; border:1px solid var(--line); border-radius:16px; padding:1.6rem; box-shadow:0 1px 2px rgba(15,61,62,.04); }
div[data-testid="stForm"] label p { font-weight:600; font-size:.92rem; }
div[data-baseweb="input"], div[data-baseweb="base-input"] { border-radius:10px; }
div[data-testid="stFormSubmitButton"] button { background:var(--pine); color:#FFF; border:none; border-radius:10px; padding:.7rem 1.2rem; font-weight:600; }
div[data-testid="stFormSubmitButton"] button:hover { background:#17595B; color:#FFF; }
.panel { min-height:100%; }
.panel h3 { font-family:'Fraunces',serif; font-weight:600; font-size:1.6rem; margin:0 0 .3rem; color:var(--ink); }
.panel .sub { color:var(--muted); margin:0 0 1.4rem; }
.verdict { display:flex; align-items:center; gap:1.6rem; margin-bottom:1.6rem; }
.verdict.approved h3 { color:var(--approve); } .verdict.declined h3 { color:var(--decline); }
.ring { flex:none; width:150px; height:150px; border-radius:50%; background:conic-gradient(var(--ring) calc(var(--pct) * 1%), var(--line) 0); display:grid; place-items:center; }
.ring-inner { width:116px; height:116px; border-radius:50%; background:#FFF; display:flex; flex-direction:column; align-items:center; justify-content:center; }
.ring-num { font-family:'Fraunces',serif; font-weight:700; font-size:2rem; line-height:1; } .ring-cap { font-size:.7rem; color:var(--muted); margin-top:.25rem; text-align:center; }
.mascot { flex:none; width:96px; height:96px; margin-left:auto; object-fit:contain; } .mascot svg { width:100%; height:100%; }
.checks { border-top:1px solid var(--line); }
.check { display:flex; justify-content:space-between; align-items:center; padding:.8rem 0; border-bottom:1px solid var(--line); font-size:.95rem; }
.check .label { color:var(--muted); } .check .value { font-weight:600; margin-right:.7rem; }
.pill { display:inline-block; min-width:82px; text-align:center; padding:.2rem .7rem; border-radius:999px; font-size:.8rem; font-weight:600; }
.pill.good { background:#E3F1E9; color:#1F7A4D; } .pill.mid { background:#F7EBCF; color:#7A5A12; } .pill.bad { background:#F5DEDA; color:#A63D2F; }
.note { color:var(--muted); font-size:.85rem; margin-top:1.2rem; }
@media (max-width:640px) { .hero h1 { font-size:2.2rem; } .verdict { flex-direction:column; align-items:flex-start; } .mascot { margin-left:0; } }
@media (prefers-reduced-motion:reduce) { * { transition:none !important; } }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

BACKEND_URL = "http://127.0.0.1:8000"

def demo_probability(income, credit_score, loan_amount, years):
    z = (credit_score - 650) / 60 + min(years, 15) / 10 + (income / max(loan_amount, 1) - 3) / 2 - 1.0
    return 1 / (1 + math.exp(-z))


def predict(income, credit_score, loan_amount, years):
    response = requests.post(
        f"{BACKEND_URL}/predict",
        json={
            "income": income,
            "credit_score": credit_score,
            "loan_amount": loan_amount,
            "employment_years": years,
        },
        timeout=10,
    )

    response.raise_for_status()

    result = response.json()

    return bool(result["approved"]), result["probability"]


def quick_checks(income, credit_score, loan_amount, years):
    if credit_score >= 740:
        score_band = ("Excellent", "good")
    elif credit_score >= 670:
        score_band = ("Good", "good")
    elif credit_score >= 580:
        score_band = ("Fair", "mid")
    else:
        score_band = ("Poor", "bad")

    ratio = loan_amount / income if income > 0 else float("inf")
    ratio_band = ("Low", "good") if ratio <= 0.3 else ("Moderate", "mid") if ratio <= 0.6 else ("High", "bad")
    ratio_text = f"{ratio:.0%}" if math.isfinite(ratio) else "n/a"
    job_band = ("Stable", "good") if years >= 5 else ("Building", "mid") if years >= 2 else ("Short", "bad")
    return [("Credit score", str(credit_score), score_band), ("Loan as share of income", ratio_text, ratio_band), ("Time in employment", f"{years} yr", job_band)]


COIN_HAPPY = '<svg viewBox="0 0 100 100" role="img" aria-label="Smiling coin"><circle cx="50" cy="50" r="46" fill="#E9B949" stroke="#B98A1E" stroke-width="4"/><circle cx="36" cy="42" r="5" fill="#1B2A2A"/><circle cx="64" cy="42" r="5" fill="#1B2A2A"/><path d="M32 58 Q50 78 68 58" fill="none" stroke="#1B2A2A" stroke-width="4" stroke-linecap="round"/></svg>'
COIN_SAD = '<svg viewBox="0 0 100 100" role="img" aria-label="Sad coin"><circle cx="50" cy="50" r="46" fill="#D9B85F" stroke="#A9832A" stroke-width="4"/><path d="M28 37 L43 32 M72 37 L57 32" stroke="#1B2A2A" stroke-width="3.5" stroke-linecap="round"/><circle cx="36" cy="45" r="5" fill="#1B2A2A"/><circle cx="64" cy="45" r="5" fill="#1B2A2A"/><path d="M34 70 Q50 56 66 70" fill="none" stroke="#1B2A2A" stroke-width="4" stroke-linecap="round"/></svg>'
IMAGE_TYPES = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "webp": "image/webp", "gif": "image/gif", "svg": "image/svg+xml"}


def mascot_html(approved):
    name = "approved" if approved else "rejected"
    for extension, mime in IMAGE_TYPES.items():
        asset = ASSETS_DIR / f"{name}.{extension}"
        if asset.exists():
            encoded = base64.b64encode(asset.read_bytes()).decode()
            alt = "Loan approved" if approved else "Loan rejected"
            return f'<img class="mascot" src="data:{mime};base64,{encoded}" alt="{alt}">' 
    return f'<div class="mascot">{COIN_HAPPY if approved else COIN_SAD}</div>'


def render_html(block):
    compact = "".join(line.strip() for line in block.splitlines())
    st.markdown(compact, unsafe_allow_html=True)


def render_result(approved, probability, checks):
    tone = "approved" if approved else "declined"
    color = "#1F7A4D" if approved else "#A63D2F"
    title = "Likely to be approved" if approved else "Unlikely to be approved"
    ring_html = ""
    if probability is not None:
        pct = round(probability * 100)
        ring_html = f'<div class="ring" style="--pct:{pct}; --ring:{color};"><div class="ring-inner"><span class="ring-num">{pct}%</span><span class="ring-cap">approval likelihood</span></div></div>'

    rows = "".join(f'<div class="check"><span class="label">{label}</span><span><span class="value">{value}</span><span class="pill {css}">{band}</span></span></div>' for label, value, (band, css) in checks)
    render_html(f'<div class="panel"><div class="verdict {tone}">{ring_html}<div><h3>{title}</h3><p class="sub" style="margin:0;">Based on the details entered.</p></div>{mascot_html(approved)}</div><div class="checks">{rows}</div><p class="note">These checks are general guides. The verdict comes from the trained model.</p></div>')


def render_empty():
    render_html('<div class="panel"><h3>No result yet</h3><p class="sub">Fill in the applicant details and select Check eligibility.</p></div>')


st.markdown('<div class="hero"><h1>Loan Approval Predictor</h1><p>Enter the applicant details to see how the trained model rates the application.</p></div>', unsafe_allow_html=True)


col_form, col_result = st.columns([1, 1], gap="large")
with col_form:
    with st.form("applicant"):
        income = st.number_input(f"Annual income ({CURRENCY})", min_value=0.0, value=90000.0, step=5000.0, format="%.0f")
        credit_score = st.number_input("Credit score", min_value=300, max_value=900, value=720, step=1)
        loan_amount = st.number_input(f"Loan amount ({CURRENCY})", min_value=0.0, value=24000.0, step=1000.0, format="%.0f")
        years = st.number_input("Employment years", min_value=0, max_value=50, value=6, step=1)
        submitted = st.form_submit_button("Check eligibility", type="primary", use_container_width=True)

with col_result:
    if submitted:
        approved, probability = predict(income, credit_score, loan_amount, years)
        render_result(approved, probability, quick_checks(income, credit_score, loan_amount, years))
    else:
        render_empty()
import time
import requests
import pandas as pd
import streamlit as st

API_URL = "http://127.0.0.1:8000/predict"
DEMO_USERNAME, DEMO_PASSWORD = "dude", "dude123"
PERSONAS = {
    "Premium Customer": ("Customers with strong purchasing power and high engagement.", "Personalise benefits and loyalty recognition.", "#0f766e", 86),
    "High-Income Low-Spender": ("Customers with meaningful purchasing power who are selective spenders.", "Use relevant recommendations to deepen engagement.", "#2563eb", 52),
    "Budget-Conscious Customer": ("Customers who make considered, value-led spending decisions.", "Lead with accessible value and clear savings.", "#0891b2", 30),
}


def setup():
    st.set_page_config("Customer Persona", layout="wide", initial_sidebar_state="collapsed")
    st.markdown("""<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
    .stApp{background:#fcfefd;color:#123b40;font-family:'DM Sans',sans-serif} #MainMenu,footer,header{visibility:hidden}.block-container{max-width:1180px;padding:1.7rem 2.2rem 3rem}
    .brand{color:#167b76;font-size:.74rem;font-weight:700;letter-spacing:.17em}.display,.title,.persona{font-family:'Playfair Display',serif;color:#123b40;letter-spacing:-.04em}.display{font-size:3.5rem;line-height:1.1;margin:.75rem 0 1rem;max-width:760px}.title{font-size:2.3rem;margin:.4rem 0 .7rem}.lead,.copy{color:#668187;line-height:1.7}.lead{font-size:1.08rem;max-width:660px}.navbrand{font-weight:700;letter-spacing:.1em;padding:.5rem 0 1.6rem;border-bottom:1px solid #e8f0ef;margin-bottom:1.5rem}.navbrand span{color:#117c76}.hero,.result-hero{border:1px solid #d8ebe8;border-radius:28px;padding:4.2rem;background:linear-gradient(118deg,#ecf8f6,#f9fdfc)}.card,.shell,.metric{background:#fff;border:1px solid #dcebea;box-shadow:0 12px 32px rgba(20,68,68,.045)}.card{border-radius:20px;padding:1.6rem;min-height:180px}.shell{border-radius:24px;padding:2.35rem}.metric{border-radius:16px;padding:1.25rem}.cardtitle{font-weight:700;font-size:1.18rem;color:#123b40;margin:.65rem 0}.index,.label{color:#167b76;font-size:.73rem;font-weight:700;letter-spacing:.12em}.persona{font-size:2.65rem;margin:.55rem 0}.score{height:12px;border-radius:99px;background:#dcefeb;overflow:hidden;margin:.75rem 0}.fill{height:100%;border-radius:99px;background:#117c76}.step{text-align:center;padding:1rem}.stepno{width:35px;height:35px;border-radius:50%;background:#e4f4f1;color:#117c76;font-weight:700;display:inline-flex;align-items:center;justify-content:center}.login{max-width:470px;margin:8vh auto;background:#fff;border:1px solid #dcebea;border-radius:25px;padding:2.75rem;box-shadow:0 22px 64px rgba(12,67,65,.08)}.stButton>button{border-radius:10px;min-height:46px;font-weight:700;border:1px solid #cddfdd;color:#245c5a}.stButton>button[kind="primary"]{background:#117c76;color:white;border-color:#117c76}.stTextInput input,.stNumberInput input{border-radius:10px;border-color:#cddfdd}@media(max-width:700px){.block-container{padding:1rem}.hero{padding:2.4rem 1.5rem}.display{font-size:2.5rem}.shell{padding:1.4rem}.login{padding:2rem 1.45rem;margin-top:3vh}}
    </style>""", unsafe_allow_html=True)
    for key, value in {"logged":False,"page":"login","prediction":None,"income":None,"score":None}.items(): st.session_state.setdefault(key,value)


def go(page): st.session_state.page=page; st.rerun()
def nav():
    st.markdown('<div class="navbrand">CUSTOMER <span>PERSONA</span></div>',unsafe_allow_html=True)
    a,b,c,_,e=st.columns([1,1,1,4,1])
    with a:
        if st.button("Home",use_container_width=True):go("home")
    with b:
        if st.button("Analyse",use_container_width=True):go("analysis")
    with c:
        if st.button("Insights",use_container_width=True):go("insights")
    with e:
        if st.button("Logout",use_container_width=True): st.session_state.logged=False;st.session_state.prediction=None;go("login")


def login():
    st.markdown('<div class="login"><div class="brand">CUSTOMER PERSONA</div><div class="title">Understand Your Customers Better</div><p class="lead">Sign in to turn customer signals into clear, useful behavioural insight.</p>',unsafe_allow_html=True)
    with st.form("signin"):
        user=st.text_input("Username",placeholder="Enter your username")
        password=st.text_input("Password",type="password",placeholder="Enter your password")
        submit=st.form_submit_button("Sign In",type="primary",use_container_width=True)
    st.markdown('</div>',unsafe_allow_html=True)
    if submit:
        if user==DEMO_USERNAME and password==DEMO_PASSWORD: st.session_state.logged=True;go("home")
        else: st.error("We couldn’t sign you in with those details. Please check your username and password.")


def home():
    nav();st.markdown('<div class="hero"><div class="brand">CUSTOMER INTELLIGENCE</div><div class="display">Know Your Customer. Understand Their Behaviour.</div><div class="lead">Explore how income and spending patterns shape customer behaviour. Customer Persona turns meaningful customer signals into a clear behavioural view.</div></div>',unsafe_allow_html=True);st.write('')
    for col,(n,title,text) in zip(st.columns(3),[("01","Understand","Bring annual income and spending behaviour into one focused profile."),("02","Segment","Identify the behavioural group that best reflects each customer."),("03","Discover","Use a clear persona to guide relevant conversations.")]):
        with col: st.markdown(f'<div class="card"><div class="index">{n}</div><div class="cardtitle">{title}</div><div class="copy">{text}</div></div>',unsafe_allow_html=True)
    st.write('');_,center,_=st.columns([1.3,1.4,1.3])
    with center:
        if st.button("Analyse a Customer",type="primary",use_container_width=True):go("analysis")


def analysis():
    nav();st.markdown('<div class="brand">CUSTOMER ANALYSIS</div><div class="title">Build a customer profile</div><p class="lead">Enter two customer signals to identify their behavioural persona.</p>',unsafe_allow_html=True)
    st.markdown('<div class="shell"><div class="cardtitle">Customer details</div><p class="copy">Use annual income in thousands of US dollars and a spending score from 0 to 100.</p>',unsafe_allow_html=True)
    with st.form("analyse"):
        left,right=st.columns(2)
        with left: income=st.number_input("Annual Income",min_value=.1,max_value=1000.,value=75.,step=1.,format="%.1f");st.caption("Currency: USD ($) · Amount in thousands")
        with right: score=st.slider("Spending Score",0,100,50);st.caption("0 = lower spending behaviour · 100 = higher spending behaviour")
        submit=st.form_submit_button("Analyse Customer",type="primary",use_container_width=True)
    st.markdown('</div>',unsafe_allow_html=True)
    if submit:
        with st.spinner("Analysing customer behaviour…"):
            time.sleep(.75)
            try:
                response=requests.post(API_URL,json={"annual_income_k":float(income),"spending_score":float(score)},timeout=12)
                result=response.json() if response.status_code==200 else None
                if not isinstance(result,dict) or "persona" not in result or "cluster" not in result: raise ValueError
            except requests.exceptions.Timeout: st.error("The analysis is taking longer than expected. Please try again in a moment.");return
            except (requests.RequestException,ValueError): st.error("We’re unable to analyse this customer right now. Please check the details and try again shortly.");return
        st.session_state.prediction=result;st.session_state.income=float(income);st.session_state.score=int(score);go("result")


def result():
    nav();data=st.session_state.prediction
    if not data: st.info("Start with a customer analysis to view a persona.");return
    persona=data.get("persona","Customer Persona");desc,focus,color,_=PERSONAS.get(persona,("This customer has been assigned to a behavioural group based on the details provided.","Use this persona to guide a relevant customer experience.","#117c76",50));income=st.session_state.income or data.get("annual_income_k",0);score=st.session_state.score if st.session_state.score is not None else data.get("spending_score",0)
    st.markdown('<div class="brand">ANALYSIS RESULT</div><div class="title">Customer persona identified</div>',unsafe_allow_html=True);st.markdown(f'<div class="result-hero"><div class="label">CUSTOMER PERSONA</div><div class="persona">{persona}</div><div class="copy">{desc}</div></div>',unsafe_allow_html=True);st.write('')
    for col,(label,value) in zip(st.columns(3),[('Cluster',str(data.get('cluster'))),('Annual Income',f'${income:,.1f}K'),('Spending Score',f'{int(score)}/100')]):
        with col:st.markdown(f'<div class="metric"><div class="copy">{label}</div><div class="cardtitle">{value}</div></div>',unsafe_allow_html=True)
    st.write('');left,right=st.columns([1.25,1])
    with left:st.markdown(f'<div class="metric"><div class="cardtitle">Spending behaviour</div><div class="score"><div class="fill" style="width:{float(score)}%"></div></div><div class="copy">{int(score)} out of 100 — a direct view of relative spending activity.</div></div>',unsafe_allow_html=True)
    with right:st.markdown(f'<div class="metric"><div class="cardtitle">Recommended focus</div><div class="copy">{focus}</div></div>',unsafe_allow_html=True)
    st.write('');a,b,_=st.columns([1.4,1.2,2])
    with a:
        if st.button("Analyse Another Customer",type="primary",use_container_width=True):st.session_state.prediction=None;go("analysis")
    with b:
        if st.button("View Insights",use_container_width=True):go("insights")


def insights():
    nav();st.markdown('<div class="brand">CUSTOMER INSIGHTS</div><div class="title">Three clear behavioural views</div><p class="lead">Personas create a shared language for interpreting customer behaviour and making each interaction more relevant.</p>',unsafe_allow_html=True)
    for col,(name,(desc,_,color,width)) in zip(st.columns(3),PERSONAS.items()):
        with col:st.markdown(f'<div class="card"><div class="cardtitle"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:{color};margin-right:8px"></span>{name}</div><div class="copy">{desc}</div><div class="score" style="margin-top:1.4rem"><div class="fill" style="width:{width}%;background:{color}"></div></div></div>',unsafe_allow_html=True)
    st.write('')
    chart_left,chart_right=st.columns(2)
    with chart_left:
        st.markdown('<div class="cardtitle">Spending behaviour by persona</div><p class="copy">A simple comparison of the typical spending patterns represented by each persona.</p>',unsafe_allow_html=True)
        spending=pd.DataFrame({"Persona":["Premium Customer","High-Income Low-Spender","Budget-Conscious Customer"],"Spending score":[82,34,29]}).set_index("Persona")
        st.bar_chart(spending,color="#117c76",height=260)
    with chart_right:
        st.markdown('<div class="cardtitle">Income and spending map</div><p class="copy">Each point shows the general relationship between annual income and spending behaviour.</p>',unsafe_allow_html=True)
        map_data=pd.DataFrame({"Annual income (USD thousands)":[30,75,70],"Spending score":[30,75,30],"Persona":["Budget-Conscious Customer","Premium Customer","High-Income Low-Spender"],"Scale":[180,260,220]})
        st.scatter_chart(map_data,x="Annual income (USD thousands)",y="Spending score",color="Persona",size="Scale",height=260)
    st.write('');st.markdown('<div class="brand">HOW IT WORKS</div><div class="title">From details to direction</div>',unsafe_allow_html=True)
    for col,(number,label) in zip(st.columns(4),[(1,'Enter details'),(2,'Analyse behaviour'),(3,'Identify group'),(4,'View persona')]):
        with col:st.markdown(f'<div class="step"><div class="stepno">{number}</div><div class="cardtitle">{label}</div></div>',unsafe_allow_html=True)


def run():
    setup()
    if not st.session_state.logged: login()
    elif st.session_state.page=="home": home()
    elif st.session_state.page=="analysis": analysis()
    elif st.session_state.page=="result": result()
    else: insights()


run()    

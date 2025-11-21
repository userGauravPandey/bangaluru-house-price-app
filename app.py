import streamlit as st
import pickle
import pandas as pd

# ---------------------- Page Config ----------------------
st.set_page_config(
    page_title="Bengaluru House Price Predictor",
    page_icon="🏡",
    layout="centered"
)

# ---------------------- Custom CSS -----------------------
st.markdown("""
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 900;
            color: #2E86C1;
            text-align: center;
        }
        .sub-title {
            font-size: 20px;
            text-align: center;
            color: #5D6D7E;
            margin-bottom: 20px;
        }
        .footer {
            margin-top: 40px;
            text-align: center;
            font-size: 16px;
            color: #7F8C8D;
        }
        .footer span {
            color: #E74C3C;
            font-weight: 700;
        }
        .box {
            padding: 20px;
            border-radius: 15px;
            background-color: #F8F9F9;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------- Title -----------------------------
st.markdown('<div class="main-title">🏡 Bengaluru House Price Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">ML Model Powered — Clean • Fast • Accurate</div>', unsafe_allow_html=True)

# ---------------------- Load Model ------------------------
with open("Pipeline.pkl", "rb") as f:
    Pipeline = pickle.load(f)

# ---------------------- Input Box -------------------------
st.markdown('<div class="box">', unsafe_allow_html=True)

location = st.text_input("📍 Location")
total_sqft = st.number_input("📏 Total Area (sqft)", value=1000.0, min_value=200.0, max_value=20000.0)
bhk = st.number_input("🛏️ BHK", min_value=1, max_value=10, value=2)
bath = st.number_input("🚿 Bathrooms", min_value=1, max_value=10, value=2)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------- Prediction ------------------------
if st.button("🔮 Predict Price", use_container_width=True):
    try:
        df = pd.DataFrame([{
            "location": location,
            "total_sqft": total_sqft,
            "bhk": bhk,
            "bath": bath
        }])

        pred =Pipeline.predict(df)[0]
        price_rupees=pred*1_00_000
        if pred>=100:
            crore=pred / 100
            st.success(f"Estimated Price:**₹{crore:.2f}Crores**")
        else:
            st.success(f"💰 Estimated Price: **₹ {pred:.2f}Lakhs**")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# ---------------------- Footer ---------------------------
st.markdown('<div class="footer">Made with ❤️ by <span>Gaurav Pandey</span></div>', unsafe_allow_html=True)
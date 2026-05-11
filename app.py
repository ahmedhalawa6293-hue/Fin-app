import streamlit as st

# إعدادات الصفحة بستايل شبابي وقوي
st.set_page_config(page_title="FinCompare", page_icon="⚡", layout="centered")

# إضافة ستايل CSS للألوان والخطوط
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    h1 {
        color: #BF94FF; 
        text-align: center;
    }
    .stButton>button {
        background-color: #BF94FF;
        color: black;
        border-radius: 20px;
        font-weight: bold;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# اللوجو والعنوان
st.markdown("<h1>⚡ FinCompare</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>الخلاصة.. عشان تقسط صح!</p>", unsafe_allow_info=True)

st.divider()

# المدخلات
amount = st.number_input("المبلغ المطلوب (جنيه)", value=10000)
months = st.selectbox("مدة التقسيط (شهور)", [3, 6, 12, 18, 24])

companies = [
    {"name": "Valu (ڤاليو)", "interest": 0.15, "icon": "🟧"},
    {"name": "Halan (حالا)", "interest": 0.12, "icon": "🟩"},
    {"name": "Sympl (سيمبل)", "interest": 0.0, "icon": "🟦"}
]

if st.button("وريني الأوفر دلوقتي!"):
    st.success("لقينا لك أحسن عروض:")
    for co in companies:
        total = amount + (amount * co['interest'] * (months/12))
        st.markdown(f"""
        <div style="background-color: #262730; padding: 20px; border-radius: 15px; margin-bottom: 10px; border: 1px solid #BF94FF;">
            <h3 style="color: white; margin: 0;">{co['icon']} {co['name']}</h3>
            <p style="color: #BF94FF; font-size: 20px; margin: 5px 0;">القسط: <b>{total/months:,.2f} جنيه/شهر</b></p>
            <small style="color: #888;">إجمالي المبلغ: {total:,.2f} جنيه</small>
        </div>
        """, unsafe_allow_html=True)

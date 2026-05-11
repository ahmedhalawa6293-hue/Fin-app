import streamlit as st

st.title("💰 FinCompare | قارن قبل ما تقسط")
amount = st.number_input("المبلغ اللي عايز تقسطه (بالجنيه)", value=10000)
months = st.selectbox("مدة التقسيط (شهور)", [3, 6, 9, 12, 18, 24])

companies = [
    {"name": "ڤاليو (Valu)", "interest": 0.15},
    {"name": "حالا (Halan)", "interest": 0.12},
    {"name": "أمان (Aman)", "interest": 0.18}
]

if st.button("قارن العروض"):
    for co in companies:
        total = amount + (amount * co['interest'] * (months/12))
        st.write(f"### {co['name']}")
        st.write(f"إجمالي المبلغ: {total:,.2f} جنيه | القسط: {total/months:,.2f} جنيه/شهر")
        st.divider()

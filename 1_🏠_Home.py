import streamlit as st
from datetime import datetime, timedelta
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo
from streamlit_extras.switch_page_button import switch_page

add_logo(
    "https://muwuzzuf.com/logos/l6zrcpVygq4D3LK8SzjzTrz855qmONM8N10NUSQR.png",
    height=140,
)

st.title("📲 WE TECH Training - Helper APP")
st.markdown("---")

st.markdown(
    '<div style="background-color: #E8F4FD; padding: 10px; border-radius: 10px; border-left: 4px solid #3498DB; direction: rtl;">'
    '<h3 style="color: #3498DB; margin-top: 0; width: 100%; text-align: right;">تحديثات</h3>'
    '<ul style="list-style-type: disc; padding-inline-start: 30px; color: #333; font-family: Cairo; direction: rtl;">'
    "<li>تم اضافة كل الايام.</li>"
    "<li>تم اضافة كل الايام.</li>"
    "<li>جاري اضافة ال quiz اليسا عملينو.</li>"
    "</ul>"
    "</div>",
    unsafe_allow_html=True,
)

st.write("")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    quiz_page = st.button("✍Take A Quiz !!")
    if quiz_page:
        switch_page("Quiz")
with col2:
    sla_chat = st.button("💬 Find SLA of CASE ⌚")
    if sla_chat:
        switch_page("Sla_Chat")
with col3:
    q_search = st.button("🔍 Search Question ❓")
    if q_search:
        switch_page("Question_Lookup")
with col4:
    case_detect = st.button("🔭 Case_Detection")
    if case_detect:
        switch_page("Case_Detection")
with col5:
    pdf = st.button("📚 Matrial PDFS")
    if pdf:
        switch_page("Matrial PDFS")

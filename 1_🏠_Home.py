import streamlit as st
from datetime import datetime, timedelta
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo
from streamlit_extras.switch_page_button import switch_page
import pytz  # Import the pytz library

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
    '<li><span style="font-size: 14px;">يتم الأن اضافة اسئله ال Quiz الثاني.</span></li>'
    "</ul>"
    "</div>",
    unsafe_allow_html=True,
)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    quiz_page = st.button("✍Take A Quiz !!")
    if quiz_page:
        switch_page("Quiz")
with col2:
    pdf_page = st.button("⏬ Download PDF Files")
    if pdf_page:
        switch_page("Matrial_PDFS")
with col3:
    sla_chat = st.button("💬 Find SLA of CASE ⌚")
    if sla_chat:
        switch_page("Sla_Chat")


def format_time_difference(time_difference):
    total_seconds = int(time_difference.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds


def main():
    colored_header(
        label="⏳ Quiz Countdown",
        description="",
        color_name="violet-70",
    )

    cairo_timezone = pytz.timezone("Africa/Cairo")  # Set Cairo timezone

    quiz_dates = {
        "Second Quiz": cairo_timezone.localize(
            datetime(2023, 8, 22)
        ),  # Set Cairo timezone
        "Third Quiz": cairo_timezone.localize(
            datetime(2023, 8, 31)
        ),  # Set Cairo timezone
    }

    card_style = "background-color: #333; padding: 15px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); border: 1px solid #555; border-radius: 5px; margin-bottom: 10px;"
    quiz_name_style = "color: #00aaff;"
    time_style = "color: #fff;"
    countdown_style = "color: #ff5733;"

    for quiz_name, quiz_date in quiz_dates.items():
        time_difference = quiz_date - datetime.now(cairo_timezone)
        hours, minutes, seconds = format_time_difference(time_difference)

        countdown_div = f"<div id='{quiz_name}_countdown' style='{countdown_style}'>{hours:02}:{minutes:02}:{seconds:02}</div>"

        # Using HTML to format the text and apply the card style
        st.write(
            f"<div style='{card_style}'>"
            f"<strong style='{quiz_name_style}'>{quiz_name}:</strong> "
            f"<u style='{time_style}'>{quiz_date.strftime('%B %d, %Y')}</u> - Countdown:{countdown_div}"
            f"</div>",
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()

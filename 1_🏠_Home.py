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
    '<div style="background-color: #E8F4FD; padding: 15px; border-radius: 5px; border-left: 4px solid #3498DB; direction: rtl;">'
    '<h3 style="color: #3498DB; margin-top: 0; width: 100%; text-align: right;">تحديثات</h3>'
    '<ul style="list-style-type: disc; padding-inline-start: 55px; color: #333; font-family: Cairo; direction: rtl;">'
    "<li>تم تحديث ملفات ال PDF ليوم 12 (Bad Line Quality).</li>"
    "<li>SLA CHAT دلوقتي متاح,تقدر تعرف اي SLA بلأسم ال في ال PDF.</li>"
    "<li>دلوقتي تقدر تخطار الايام الانت عاوز تحل اسأله ال QUIZ بتاعتها.</li>"
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
        switch_page("Matrial_PDFS")


def time_until(target_date):
    current_time = datetime.now()
    time_difference = target_date - current_time
    return time_difference


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

    quiz_dates = {
        "Second Quiz": datetime(2023, 8, 22, 10, 0, 0),  # Replace with your quiz time
        "Third Quiz": datetime(2023, 8, 31, 15, 30, 0),  # Replace with your quiz time
    }

    card_style = "background-color: #333; padding: 15px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); border: 1px solid #555; border-radius: 5px; margin-bottom: 10px;"
    quiz_name_style = "color: #00aaff;"
    time_style = "color: #fff;"
    countdown_style = "color: #ff5733;"

    for quiz_name, quiz_date in quiz_dates.items():
        time_difference = time_until(quiz_date)
        hours, minutes, seconds = format_time_difference(time_difference)

        countdown_div = f"<div id='{quiz_name}_countdown' style='{countdown_style}'>{hours:02}:{minutes:02}:{seconds:02}</div>"

        # Using HTML to format the text and apply the card style
        st.write(
            f"<div style='{card_style}'>"
            f"<strong style='{quiz_name_style}'>{quiz_name}:</strong> "
            f"<u style='{time_style}'>{quiz_date.strftime('%B %d, %Y %I:%M %p')}</u> - Countdown: {countdown_div}"
            f"</div>",
            unsafe_allow_html=True,
        )

        # JavaScript for live countdown updates
        st.markdown(
            f"""
            <script>
                function updateCountdown_{quiz_name}() {{
                    var countdownDiv = document.getElementById('{quiz_name}_countdown');
                    var now = new Date().getTime();
                    var targetTime = new Date('{quiz_date.strftime('%Y-%m-%dT%H:%M:%S')}').getTime();
                    var timeDifference = targetTime - now;

                    var hours = Math.floor(timeDifference / (1000 * 60 * 60));
                    var minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
                    var seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

                    countdownDiv.innerHTML = hours.toString().padStart(2, '0') + ':' + minutes.toString().padStart(2, '0') + ':' + seconds.toString().padStart(2, '0');

                    if (timeDifference <= 0) {{
                        countdownDiv.style.color = 'green';
                        countdownDiv.innerHTML = 'Time is up!';
                    }} else {{
                        setTimeout(updateCountdown_{quiz_name}, 1000);
                    }}
                }}
                updateCountdown_{quiz_name}();
            </script>
            """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()

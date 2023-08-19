import streamlit as st
from data import data

st.title("📚 WE Training Material PDF")

st.markdown(
    '<div style="background-color: #e6f7ff; padding: 10px; border-radius: 5px; font-family: Cairo; direction: rtl;">'
    '<span style="color: #0066cc; font-weight: bold;">🔰 ال PDF(S) الهنا عبارة عن سكرين شوت لكل Slide من علي ال sharepoint ومعملها join.</span>'
    "</div>",
    unsafe_allow_html=True,
)

# Add an empty space
st.write("")

st.markdown(
    '<div style="background-color: #ffeeba; padding: 10px; border-radius: 5px; font-family: Cairo; direction: rtl;">'
    '<span style="color: #ff9900; font-weight: bold;">⚠️ممكن تخطار يوم معين من ال Box التحت.</span>'
    "</div>",
    unsafe_allow_html=True,
)

st.write("")

st.info(
    "💽 Google Drive Link: [Link](https://drive.google.com/drive/folders/1Ll06MG9uSDZzj1N5e23Z1BqAuHXpA7ZV?usp=drive_link)"
)

st.markdown("---")

# Create a list of all day names
all_days = ["Please Select an Option"] + [
    day["day_name"] for day in data
]  # Adding "Please Select" option

# Style for the select box label
label_style = "font-size: 18px; font-weight: bold;"

# Add a selectbox for searching and filtering days
selected_day = st.selectbox("Select a day:", all_days)

# Display message if no option is selected
if selected_day == "Please Select an Option":
    st.warning("Please select an option to show PDF files.")

# Display the selected day's folders and files
elif selected_day and selected_day != "":
    selected_day_data = next(day for day in data if day["day_name"] == selected_day)
    expander = st.expander(label=selected_day_data["day_name"], expanded=True)
    with expander:
        for pdf_name, pdf_link in selected_day_data["pdf_files"].items():
            st.markdown(
                f"[{pdf_name}]({pdf_link})"
            )  # Use the provided pdf_link directly

# Optionally, display a message if no results are found
if not selected_day or selected_day == "":
    st.warning("Please select a day.")

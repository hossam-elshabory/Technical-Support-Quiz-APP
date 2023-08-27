import os
import streamlit as st

# Create a dictionary to store item names as keys and their corresponding image filenames as values
items = {
    "Day 14 - Unable to obtain IP": ["Day 14 - Unable to obtain IP.png"],
    "Day 15 - Browsing": [
        "Day 15 - Browsing.png",
        "Day 15 - Browsing certain websites.png",
    ],
    "Day 16 Logical Instability": ["Day 16 Logical Instability.png"]
    # Add more items and image filenames as needed
}

# Get a list of sorted item names in descending order
sorted_items = sorted(items.keys(), reverse=True)


# Streamlit app
def main():
    st.title("🔭 Case Detection Tree")

    st.markdown(
        '<div style="background-color: #e6f7ff; padding: 10px; border-radius: 5px; font-family: Cairo; direction: rtl;">'
        '<span style="color: #0066cc; font-weight: bold;">🔰 اختر اليوم و صورة ال Case Detection هتطلعلك.</span>'
        "</div>",
        unsafe_allow_html=True,
    )

    st.write("")

    # Create a selection box to choose an item
    selected_item = st.selectbox(
        "Select The Day",
        [""] + sorted_items,
    )

    # Show a warning message if no item is selected
    if not selected_item:
        st.warning("Please select the day to display the case detection tree images.")
        return

    # Display the selected item name
    expander = st.expander(f"Case Detection Image for {selected_item}", expanded=True)

    # Get the list of image filenames for the selected item
    image_filenames = items[selected_item]

    # Display each image inside the expander
    for image_filename in image_filenames:
        image_path = os.path.join("images", image_filename)
        expander.image(image_path, caption=image_filename, use_column_width=True)


if __name__ == "__main__":
    main()

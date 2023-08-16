import streamlit as st
import random
import time
import pandas as pd  # Import pandas for the DataFrame and SLA function

# Sample DataFrame (replace this with your actual data)
data = {"name": ["John", "Jane", "Alice", "Bob"], "SLA": [3, 2, 4, 5]}
df = pd.DataFrame(data)


# Your SLA function
def get_sla_by_name(input_name, dataframe):
    try:
        sla = dataframe[dataframe["name"] == input_name]["SLA"].values[0]
        return sla
    except IndexError:
        return None


st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Process user input and get SLA
    input_name = prompt.strip()  # Assuming user input is just the name
    sla_result = get_sla_by_name(input_name, df)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        if sla_result is not None:
            response = f"The SLA for {input_name} is `{sla_result}`"
        else:
            response = f"Sorry, I couldn't find the SLA for {input_name}"

        # Simulate typing
        for chunk in response.split():
            time.sleep(0.05)
            message_placeholder.markdown(chunk + "▌")
        message_placeholder.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

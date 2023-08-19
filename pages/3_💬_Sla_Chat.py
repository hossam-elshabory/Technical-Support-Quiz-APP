import streamlit as st
import pandas as pd
import fuzzywuzzy
from fuzzywuzzy import process

df = pd.read_csv("./sla.csv")


def get_sla_by_name(input_name, dataframe):
    try:
        input_name_lower = input_name.lower()
        sla = dataframe[dataframe["case"].str.lower() == input_name_lower][
            "Normal SLA"
        ].values[0]
        return sla
    except IndexError:
        return None


st.title("⌚ SLA Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("SLA Name ?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    input_name = prompt.strip()

    sla_result = get_sla_by_name(input_name, df)

    if sla_result is not None:
        response = f"✅ {input_name} SLA = `{sla_result}`"

        sla_row = df[df["case"].str.lower() == input_name.lower()]

        with st.chat_message("assistant"):
            st.markdown(response)
            st.dataframe(sla_row, hide_index=True)

    else:
        matched_cases = process.extract(
            input_name, df["case"], limit=3, scorer=fuzzywuzzy.fuzz.token_sort_ratio
        )

        matches = []
        for match in matched_cases:
            case = match[0]
            score = match[1]

            if score > 40:
                matches.append(case)

        if matches:
            response = f"⛔ Failed to find an exact match for `{input_name}` but found these partial matches:"

            matches_df = df[df["case"].isin(matches)]

            with st.chat_message("assistant"):
                st.markdown(response)
                st.dataframe(matches_df, hide_index=True)

        else:
            response = f"Sorry, could not find any matches for `{input_name}`"

            with st.chat_message("assistant"):
                st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

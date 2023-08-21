import streamlit as st
import difflib
from questions import questions


def calculate_similarity(query, question):
    words_query = query.lower().split()
    words_question = question.lower().split()
    sim_ratio = difflib.SequenceMatcher(None, words_query, words_question).ratio()
    return sim_ratio


def search_questions(query):
    results = []
    for q in questions:
        similarity = calculate_similarity(query, q["eng_question"])
        if similarity >= 0.4:
            q["similarity"] = similarity
            results.append(q)
    return results


def highlight_text(text, color):
    return f'<span style="color:{color};">{text}</span>'


st.title("🔍 Question Similarity Search")

st.markdown(
    '<div style="background-color: #e6f7ff; padding: 10px; border-radius: 5px; font-family: Cairo; direction: rtl;">'
    '<span style="color: #0066cc; font-weight: bold;">اكتب السؤال هنا و الاسئله الشبهو هتطلعلك</span>'
    "</div>",
    unsafe_allow_html=True,
)

st.write("")

query = st.text_input("Enter a question to search:")

if query:
    matching_questions = search_questions(query)
    if matching_questions:
        st.header("Matching Questions:")
        for q in matching_questions:
            with st.expander(f"Q : {q['eng_question']}"):
                st.write(f"Similarity: {q['similarity']:.2f}")
                st.markdown(
                    f"Correct Answer: {highlight_text(q['correct_answer'], 'green')}",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f"Day: {highlight_text(q['day'], 'yellow')}", unsafe_allow_html=True
                )

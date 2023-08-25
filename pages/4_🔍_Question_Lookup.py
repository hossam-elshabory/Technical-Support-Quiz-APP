import streamlit as st
import difflib
from questions import questions


def calculate_similarity(query, question):
    words_query = query.lower().split()
    words_question = question.lower().split()
    sim_ratio = difflib.SequenceMatcher(None, words_query, words_question).ratio()
    return sim_ratio


def search_questions(query, similarity_threshold):
    results = []
    for q in questions:
        similarity = calculate_similarity(query, q["eng_question"])
        if similarity >= similarity_threshold:
            q["similarity"] = similarity
            results.append(q)
    return results


def highlight_text(text, color):
    return f'<span style="color:{color};">{text}</span>'


st.title("🔍 Question Similarity Search")

st.markdown(
    '<div style="background-color: #FFF3C2; border-left: 6px solid #FF9800; padding: 10px; border-radius: 5px; display: flex; align-items: center; direction: rtl; font-family: Cairo;">'
    '<span style="color: #333; font-weight: bold; margin-right: 10px;">⚠ اكتب السؤال و حدد نسبة التشابه و هيظهرلك الاسئله الشبه السؤال دا !</span>'
    "</div>",
    unsafe_allow_html=True,
)

st.write("")

st.markdown(
    '<div style="background-color: #e6f7ff; padding: 10px; border-radius: 5px; font-family: Cairo; direction: rtl;">'
    '<span style="color: #0066cc; font-weight: bold;">🔰  غير في نسبة التشابه التحت من ال Slider للبحث علي اسأله بنسبة تشابه اقل/اكثر.</span>'
    "</div>",
    unsafe_allow_html=True,
)

st.write("")

st.markdown(
    '<div style="background-color: #FFF3C2; border-left: 6px solid #FF9800; padding: 10px; border-radius: 5px; display: flex; align-items: center; direction: rtl; font-family: Cairo;">'
    '<span style="color: #333; font-weight: bold; margin-right: 10px;">⚠ الازم تدوس Search بعد اي تغيير تعملو!</span>'
    "</div>",
    unsafe_allow_html=True,
)

st.write("")

# Encapsulate everything in a form
with st.form("question_search_form"):
    query = st.text_input("Enter a question to search:")
    reset_button = st.form_submit_button("Search")
    similarity_threshold = st.slider("Similarity Threshold (%)", 20, 100, 50, step=5)

# Convert the percentage value to a float between 0 and 1
similarity_threshold /= 100

if reset_button or query:
    matching_questions = search_questions(query, similarity_threshold)
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
    else:
        st.error("❌ No matching questions found.")

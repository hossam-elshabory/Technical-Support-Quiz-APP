import streamlit as st
from questions import questions
import random
from typing import Set


default_days = ["Day 08 - Voice Cases"]


def main():
    st.title("WE Training Quiz Archive.📦")
    st.markdown("---")

    if "question_index" not in st.session_state:
        initialize_session_state()

    question_index = st.session_state.question_index
    score = st.session_state.score
    wrong_answers = st.session_state.wrong_answers

    display_message_to_users()  # Display message first

    st.write("")

    display_filter_options()  # Then display multiselect widget

    st.markdown("---")

    if "selected_days" in st.session_state:
        selected_days = st.session_state.selected_days
        filtered_questions = filter_questions_by_days(questions, selected_days)
        total_questions = len(filtered_questions)
    else:
        selected_days = set()
        filtered_questions = questions
        total_questions = len(questions)

    display_progress_score(
        question_index, score, total_questions_in_day=len(filtered_questions)
    )
    restart_button()

    st.markdown("---")

    if question_index < len(filtered_questions):
        question_data = filtered_questions[question_index]

        display_question(question_index + 1, question_data)

        for option in question_data["options"]:
            if st.button(option, key=option):
                selected_option = option
                check_answer(selected_option, question_data, score, wrong_answers)
                st.experimental_rerun()

        st.markdown("---")
        display_progress_bar(question_index, len(filtered_questions))

    else:
        display_quiz_results(score, len(filtered_questions), wrong_answers)


def initialize_session_state():
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.wrong_answers = []
    st.session_state.total_questions = len(
        questions
    )  # Store the total number of questions
    random.shuffle(questions)
    for question in questions:
        random.shuffle(question["options"])


def display_filter_options():
    days = set([question["day"] for question in questions])
    sorted_days = sorted(days, reverse=True)  # Sort the days in descending order
    selected_days = st.multiselect(
        "Select days of Quiz:",
        ["All"] + sorted_days,
        default=default_days,  # Add the default days
    )
    if "All" in selected_days:
        selected_days = sorted_days
    st.session_state.selected_days = selected_days


def filter_questions_by_days(questions, selected_days):
    if "All" in selected_days:
        return questions
    return [question for question in questions if question["day"] in selected_days]


def display_message_to_users():
    st.markdown(
        '<div style="background-color: yellow; padding: 10px; border-radius: 5px; font-family: Cairo; direction: rtl;">'
        '<span style="color: black; font-weight: bold;">نتأكد من الأسئلة و احنا بنحل, لو حد لقي سؤال شاكيك فيه بيعت علي الجروب</span>'
        "</div>",
        unsafe_allow_html=True,
    )


def display_progress_score(question_index, score, total_questions_in_day):
    st.write(f"Question: {question_index + 1}/{total_questions_in_day}")
    st.write(f"Score: {score}/{total_questions_in_day}")


def display_question(question_number, question_data):
    st.subheader(question_data["eng_question"])
    st.markdown(
        f'<div style="text-align: right; direction: rtl; font-family: Cairo, sans-serif;">'
        f'{question_data["arabic_question"]}'
        f"</div>",
        unsafe_allow_html=True,
    )
    st.markdown("---")


def check_answer(selected_option, question_data, score, wrong_answers):
    if selected_option == question_data["correct_answer"]:
        score += 1
    else:
        wrong_answers.append(
            {
                "eng_question": question_data["eng_question"],
                "arabic_question": question_data["arabic_question"],
                "selected_answer": selected_option,
                "correct_answer": question_data["correct_answer"],
            }
        )
    st.session_state.question_index += 1
    st.session_state.score = score
    st.session_state.wrong_answers = wrong_answers


def display_progress_bar(question_index, total_questions):
    progress = question_index / total_questions
    st.progress(progress, "Progress")
    if progress == 1.0:
        st.markdown(
            "<style>div.stProgress > div > div {background-color: green;}</style>",
            unsafe_allow_html=True,
        )


def display_quiz_results(score, total_questions, wrong_answers):
    st.subheader("Quiz Completed!")
    percentage_correct = (score / total_questions) * 100
    st.subheader("Final Score:")
    st.markdown(f"**Correct Answers:** {score} out of {total_questions}")
    st.markdown(
        f"**Percentage Correct:** {percentage_correct:.1f}%", unsafe_allow_html=True
    )
    st.markdown("---")
    if len(wrong_answers) > 0:
        st.markdown(
            "#### <span style='color:red; font-weight:bold;'>Wrong Answered Questions:</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<style> .red-bold { color: red; font-weight: bold; } </style>",
            unsafe_allow_html=True,
        )
        for index, wrong_answer in enumerate(wrong_answers, start=1):
            display_wrong_answer(wrong_answer, index)


def display_wrong_answer(wrong_answer, index):
    expander = st.expander(f"Question {index}: {wrong_answer['eng_question']}")
    with expander:
        st.subheader("English Question:")
        st.write(wrong_answer["eng_question"])
        st.subheader("Arabic Question:")
        st.markdown(
            f'<div style="text-align: right; direction: rtl;">{wrong_answer["arabic_question"]}</div>',
            unsafe_allow_html=True,
        )
        formatted_selected_answer = color_answer(
            wrong_answer["selected_answer"], wrong_answer["correct_answer"]
        )
        formatted_correct_answer = color_answer(
            wrong_answer["correct_answer"], wrong_answer["correct_answer"]
        )
        st.markdown(f"Your Answer: {formatted_selected_answer}", unsafe_allow_html=True)
        st.markdown(
            f"Correct Answer: {formatted_correct_answer}", unsafe_allow_html=True
        )


def restart_button():
    if st.button("Restart Quiz"):
        initialize_session_state()
        st.experimental_rerun()


def color_answer(answer, correct_answer):
    if answer == correct_answer:
        return f'<span style="color:green">{answer}</span>'
    else:
        return f'<span style="color:red">{answer}</span>'


if __name__ == "__main__":
    main()

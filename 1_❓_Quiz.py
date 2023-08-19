import streamlit as st
from questions import questions
import random

PASSWORD = "123"


def main():
    st.title("WE Tranning Quiz Archive.📦")
    st.markdown("---")

    if "question_index" not in st.session_state:
        initialize_session_state()

    question_index = st.session_state.question_index
    score = st.session_state.score
    wrong_answers = st.session_state.wrong_answers

    authenticated = st.session_state.get("authenticated", False)

    if authenticated:
        display_message_to_users()
        restart_button()
        if question_index < len(questions):
            question_data = questions[question_index]

            display_question(question_index + 1, question_data)

            for option in question_data["options"]:
                if st.button(option, key=option):
                    selected_option = option
                    check_answer(selected_option, question_data, score, wrong_answers)
                    st.experimental_rerun()

            st.markdown("---")
            display_progress_bar(question_index, len(questions))

        else:
            display_quiz_results(score, len(questions), wrong_answers)

    else:
        authenticate()


def authenticate():
    # Display the pop-up message with updated styling
    st.markdown(
        '<div style="background-color: #FFDD00; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; font-family: Cairo, sans-serif; color: black;">'
        "دا مش كويز رسمي او تبع اي حاجة رسمية خاصة بلتدريب الرسمي, دي مجرد اداه مجمعه كل الاسئلة بتاعت الكويزات اليومية البنحلها كل يوم عشان ندرب عليها تاني."
        "</div>",
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        '<div style="background-color: #FFDD00; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; font-family: Cairo, sans-serif; color: red;">'
        "الباسورد 123 و دا مش كويز رسمي"
        "</div>",
        unsafe_allow_html=True,
    )
    password_input = st.sidebar.text_input(
        "", type="password", key="password_input", help="كود الباسورد: 123"
    )
    if password_input == PASSWORD:
        st.session_state["authenticated"] = True
        st.experimental_rerun()


def initialize_session_state():
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.wrong_answers = []

    # Shuffle the questions list
    random.shuffle(questions)

    # Shuffle answer options for each question
    for question in questions:
        random.shuffle(question["options"])


def display_message_to_users():
    st.markdown(
        '<div style="background-color: yellow; padding: 10px; border-radius: 5px; font-family: Cairo; direction: rtl;">'
        '<span style="color: black; font-weight: bold;">نتأكد من الأسئلة و احنا بنحل, لو حد لقي سؤال شاكيك فيه بيعت علي الجروب</span>'
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("---")


def display_question(question_number, question_data):
    st.sidebar.header("Quiz Progress")
    st.sidebar.write(f"Question: {question_number}/{len(questions)}")
    st.sidebar.write(f"Score: {st.session_state.score}/{len(questions)}")

    # Display English question
    st.subheader(question_data["eng_question"])

    # Display Arabic question (right-to-left) using Cairo font
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

    # Calculate the percentage of correct answers
    percentage_correct = (score / total_questions) * 100

    # Display final score card
    st.subheader("Final Score:")
    st.markdown(f"**Correct Answers:** {score} out of {total_questions}")
    st.markdown(
        f"**Percentage Correct:** {percentage_correct:.1f}%", unsafe_allow_html=True
    )

    st.markdown("---")

    st.sidebar.subheader("Quiz Results")
    st.sidebar.write(f"Final Score: {score}/{total_questions}")

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
    if st.sidebar.button("Restart Quiz"):
        initialize_session_state()
        st.experimental_rerun()
    st.sidebar.markdown("---")


def color_answer(answer, correct_answer):
    if answer == correct_answer:
        return f'<span style="color:green">{answer}</span>'
    else:
        return f'<span style="color:red">{answer}</span>'


if __name__ == "__main__":
    main()

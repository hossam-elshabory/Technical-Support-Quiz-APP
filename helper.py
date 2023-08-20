def add_day_to_questions(questions):
    days = [
        "Day 03 - Network fundamentals",
        "Day 04 - New line Registration",
        "Day 05 - Fixed Voice Migration",
        "Day 06 - Tools and New subscription",
        "Day 07 - Tools and Follow Up",
    ]

    for i, question in enumerate(questions):
        day_index = i // 10
        if day_index < len(days):
            question["day"] = days[day_index]


if __name__ == "__main__":
    from questions import questions

    add_day_to_questions(questions)

    with open("questions_mod.py", "w", encoding="utf-8") as file:
        file.write("questions = " + repr(questions))

def is_valid_score(score):
    return 1 <= score <= 10


def evaluate_skills(students):
    errors = []

    for skill in ["UX Design", "Structured Programming", "Data Structures"]:
        score = students[skill]
        if not is_valid_score(score):
            errors.append(f"Invalid score for {skill}. Please enter a score between 1 and 10.")

    if errors:
        for error in errors:
            print(error)
        return False

    return True


def print_student_dictionary(students):
    print("\nStudent dictionary:")
    for key, value in students.items():
        print(f"{key}: {value}")


def determine_best_match(students):
    skills = {key: value for key, value in students.items() if key != "name"}
    best_skill = max(skills, key=skills.get)
    best_score = skills[best_skill]

    print(f"\nBest match:")
    print(f"{students['name']} has the highest score in {best_skill} ({best_score}).")

    for skill, score in skills.items():
        if score >= 8:
            print(f"- Strong candidate for {skill}.")
        elif score >= 5:
            print(f"- Potential in {skill}, but improvement is needed.")
        else:
            print(f"- May struggle with {skill} and should practice more.")


students = {
    "name": input("Enter the name of the student: "),
    "UX Design": int(input("Rate your skill score at UX Design (1-10): ")),
    "Structured Programming": int(input("Rate your skill score at Structured Programming (1-10): ")),
    "Data Structures": int(input("Rate your skill score at Data Structures (1-10): ")),
}

if evaluate_skills(students):
    print_student_dictionary(students)
    determine_best_match(students)

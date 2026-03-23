import re


special_characters_list = [
    '@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\\', '|', '}', '{', '~', ':', '[', ']'
]


def rejection(firstName: str, lastName: str, jobTitle: str, feedback: str) -> str:
    if feedback != "":
        return (
            f"Dear {firstName} {lastName},\nAfter careful evaluation of your application for the position of "
            f"{jobTitle},\nat this moment we have decided to proceed with another candidate. \nHere we would "
            f"like to provide you our feedback about the interview.\n{feedback}\nWe wish you the best in "
            f"finding your future desired career.\nPlease do not hesitate to contact us with any questions.\n"
            f"Sincerely,\nHR Department of XYZ"
        )
    else:
        return (
            f"Dear {firstName} {lastName},\nAfter careful evaluation of your application for the position of "
            f"{jobTitle},\nat this moment we have decided to proceed with another candidate. \nWe wish you "
            f"the best in finding your future desired career.\nPlease do not hesitate to contact us with "
            f"any questions.\nSincerely,\nHR Department of XYZ"
        )


def jobOffer(firstName: str, lastName: str, jobTitle: str, annualSalary: float, startingDate: str) -> str:
    return (
        f"Dear {firstName} {lastName},\nAfter careful evaluation of your application for the position of "
        f"{jobTitle},\nwe are glad to offer you the job.\nYour salary will be {annualSalary} euro annually.\n"
        f"Your start date will be on {startingDate}. Please do not hesitate to contact us with any questions.\n"
        f"Sincerely,\nHR Department of XYZ"
    )


def is_name_valid(name: str) -> bool:
    if len(name) > 1 and len(name) < 11 and name[0].isupper() and not name.isnumeric():
        for letter in name:
            if letter in special_characters_list:
                return False
        return True
    else:
        return False


def is_title_valid(jobTitle: str) -> bool:
    if not len(jobTitle) < 10 and not jobTitle.isnumeric():
        return True
    return False


def is_salary_valid(salary_str: str) -> bool:
    try:
        clean_val = salary_str.replace('.', '').replace(',', '.')
        val = float(clean_val)
        if 20000.00 <= val <= 80000.00:
            return True
        return False
    except ValueError:
        return False


def is_date_valid(startingDate: str) -> bool:
    pattern = r"^202[12]-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    match = re.fullmatch(pattern, startingDate)
    return bool(match)


def is_letter_type_valid(letterType: str) -> bool:
    print(letterType)
    if letterType == "Rejection" or letterType == "Job Offer":
        return True
    else:
        return False


def askMailType() -> str:
    return input("Job Offer or Rejection? ")


def askFirstName() -> str:
    return input("First name: ")


def askLastName() -> str:
    return input("Last name: ")


def askJobTitle() -> str:
    return input("Job title: ")


def askAnnualSalary() -> float:
    return input("Annual salary: ")


def askStartDate() -> str:
    return input("Start date: ")


def is_job_type_valid(mailType: str) -> bool:
    if mailType == "Job Offer" or mailType == "Rejection":
        return True
    else:
        return False


def askMoreLetters() -> str:
    return input("More Letters? (Yes or No) ")


def is_more_letters_valid(moreLetters: str) -> bool:
    if moreLetters == "Yes" or moreLetters == "No":
        return True
    else:
        return False


def askFeedback() -> str:
    return input("Feedback? (Yes or No) ")


def is_feedback_valid(feedback: str) -> bool:
    if feedback == "Yes" or feedback == "No":
        return True
    else:
        return False


def enterFeedback() -> str:
    return input("Enter your Feedback (One Statement) ")


def letterQuestions() -> None:
    mailType = askMailType()
    while not is_job_type_valid(mailType):
        print("Input error Enter a valid type of mail, such as 'Job Offer' or 'Rejection'.")
        mailType = askMailType()
    firstName = askFirstName()
    while not is_name_valid(firstName):
        print("Input error Name must be 2-10 characters, start with a capital letter,\n"
              "Not be a number, and contain no special characters (@#$%!*&).")
        firstName = askFirstName()
    lastName = askLastName()
    while not is_name_valid(lastName):
        print("Input error Name must be 2-10 characters, start with a capital letter,\n"
              "Not be a number, and contain no special characters (@#$%!*&).")
        lastName = askLastName()
    jobTitle = askJobTitle()
    while not is_title_valid(jobTitle):
        print("Input error Job title must be at least 10 characters long and cannot be only numbers.")
        jobTitle = askJobTitle()
    if mailType == "Job Offer":
        annualSalary = askAnnualSalary()
        if not is_salary_valid(annualSalary):
            print("Input error Please enter a numeric value (e.g., 45000).")
            annualSalary = askAnnualSalary()
    if mailType == "Job Offer":
        startDate = askStartDate()
        if not is_date_valid(startDate):
            print("Input error Date must be in YYYY-MM-DD format and within the years 2021-2022.")
            startDate = askStartDate()
    if mailType == "Job Offer":
        print("Here is the final letter to send:")
        print(jobOffer(firstName, lastName, jobTitle, annualSalary, startDate))
    if mailType == "Rejection":
        feedback = askFeedback()
        while not is_feedback_valid(feedback):
            print("Input error Please enter either 'Yes' or 'No'")
            feedback = askFeedback()
        if feedback == "Yes":
            writtenFeedback = input("Feedback: ")
        else:
            writtenFeedback = ""
    if mailType == "Rejection":
        print("Here is the final letter to send:")
        print(rejection(firstName, lastName, jobTitle, writtenFeedback))


while True:
    moreLetters = askMoreLetters()
    while not is_more_letters_valid(moreLetters):
        print("Input error Please enter either 'Yes' or 'No'")
        moreLetters = askMoreLetters()
    if moreLetters == "Yes":
        letterQuestions()
    else:
        break
from ask import answer_question


if __name__ == "__main__":
    isRunning = True

    agent = answer_question()

    while isRunning:
        message = str(input("Message:"))

        if not message:
            isRunning = False

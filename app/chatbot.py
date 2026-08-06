from app.ai import ask_ai

def get_user_question():
    return input("Please enter a valid question")

def is_exit_command(question):
    return question.lower() ==  "exit"

def  display_answer(answer):
    return print(f"\n AI : {answer} \n")


def start_chat():
    while True:
        question = get_user_question()
        if question.strip() == "":
            print("Please enter a valid question")
            continue
        if is_exit_command(question):
            break
        try :
            response = ask_ai(question)
            display_answer(response)
            
        except Exception as e:
            print(f"Error , {e}")


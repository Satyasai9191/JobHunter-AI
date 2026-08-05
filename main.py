# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# llm = ChatGroq(
#     model = "llama-3.3-70b-versatile"
# )

# response = llm.invoke(
#     "Who am I ?"
# )

# print(type(response))

# print(dir(response))

# print(response)

# from dotenv import load_dotenv

# from langchain_groq import ChatGroq

# load_dotenv()

# llm = ChatGroq(
#     model = "llama-3.3-70b-versatile"
# )


# while True:

#     question = input("Please enter a question:")

#     if question.lower() == "exit":   
#         print("Good Bye!🥳")
#         break

#     response = llm.invoke(question)

#     print(f"\n AI: {response.content}\n")




# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# llm = ChatGroq(
#     model= "llama-3.3-70b-versatile"
# )


# def ask_ai(question):
#     response = llm.invoke(question)
#     return response.content

# while True:

#         question  = input("Please enter the question:")

#         if question.lower() == "exit":
#             print("Good Bye ! 🥳")
#             break
#         try:
#             response = ask_ai(question)

#             print(f"\n AI : {response}\n")

#         except Exception as e :
#             print(f"Error :{e}")



from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


llm = ChatGroq(
    model = "llama-3.3-70b-versatile"
)

def ask_ai(question):
    response = llm.invoke(question)
    return response.content
count = 0
longest_question = ''

while True:
    question = input("Please enter a question:")
    if question.strip() == "":
        print("Please enter a valid question.")
        continue
    elif len(question)> len(longest_question):
            
    elif question.lower() == "exit":
        
        print(f"SessionSummary "
         "------------------"
        " Question asked :" , {count}
         )
        print("Good Bye !🥳")
        print(longest_question)
        break
    count = count + 1

    try:

        response = ask_ai(question)
        print(f"\n AI : {response}\n")
    except Exception as e:
        print(f"Error , {e}")

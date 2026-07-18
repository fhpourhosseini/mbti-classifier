from predict import predict_personality
from questions import questions

def ask_answer(question_number, question_text):
    while True:
        raw = input(f"{question_number}/60: {question_text}\n(-3 = strongly disagree, 3 = strongly agree): ")
        try:
            answer = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if not -3 <= answer <= 3:
            print(f"Please enter a value between -3 and 3.")
            continue
        return answer
    
def take_test():
    answers = []
    for i, question_text in enumerate(questions, start=1):
        answer = ask_answer(i, question_text)
        answers.append(answer)
    return answers

if __name__ == "__main__":
    my_answers = take_test()
    result = predict_personality(my_answers)
    print(f"\nPredicted personality type: {result}")


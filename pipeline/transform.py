from pipeline.errors import (
    InvalidNumberOfAnswersError,
    InvalidAnswerTypeError,
    InvalidAnswerValueError,
    InvalidPersonalityTypeError
)

valid_types = [
    "INTJ", "INTP", "ENTJ", "ENTP", 
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ", 
    "ISTP", "ISFP", "ESTP", "ESFP"
    ]

def parse_answers(raw_answers):
    if len(raw_answers) != 60:
        raise InvalidNumberOfAnswersError(f"Erwartet 60 Antworten, bekommen: {len(raw_answers)}")
    
    answers = []
    for raw in raw_answers:
        try:
            answer = int(raw)
        except ValueError:
            raise InvalidAnswerTypeError(f"Antwort kann nicht in Integer umgewandelt werden: {raw}")
        if not -3 <= answer <= 3:
            raise InvalidAnswerValueError(f"Ungültige Antwort: {answer}")
        answers.append(answer)
    return answers

def parse_personality_type(raw_type):
    personality_type = raw_type.upper()
    if personality_type not in valid_types:
        raise InvalidPersonalityTypeError(f"Ungültiger Persönlichkeits Typ: {personality_type}")
    return personality_type


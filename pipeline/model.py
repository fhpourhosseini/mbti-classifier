class TestAnswers:
    def __init__(self, answers, personality_type=None):
        self.answers = answers
        self.personality_type = personality_type

    def __repr__(self):
        return f"TestAnswers(answers={self.answers[0:5]}..., personality_type={self.personality_type})"
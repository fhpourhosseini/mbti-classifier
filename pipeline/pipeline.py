import logging
from pipeline.extract import extract
from pipeline.model import Test
from pipeline.transform import parse_answers, parse_personality_type
from pipeline.errors import (
    InvalidNumberOfAnswersError,
    InvalidAnswerTypeError,
    InvalidAnswerValueError,
    InvalidPersonalityTypeError
)

logger = logging.getLogger(__name__)

class Pipeline:
    def __init__(self, filepath):
        self.filepath = filepath

    def run(self):
        results = []
        for row in extract(self.filepath):
            row_id = row[0]
            try:
                answers = parse_answers(row[1:61])
                personality_type = parse_personality_type(row[61])
                results.append(Test(answers, personality_type))
            except (
                InvalidNumberOfAnswersError,
                InvalidAnswerTypeError, 
                InvalidAnswerValueError,
                InvalidPersonalityTypeError
            ) as e:
                logger.warning(f"Zeile ID={row_id} übersprungen: {e}")
        return results
    
    def __repr__(self):
        return f"Pipeline(filepath={self.filepath})"
    
        


import csv
import logging
from pipeline.model import TestAnswers
from pipeline.transform import parse_answers, parse_personality_type
from pipeline.errors import (
    InvalidNumberOfAnswersError,
    InvalidAnswerTypeError,
    InvalidAnswerValueError,
    InvalidPersonalityTypeError
)

logger = logging.getLogger(__name__)

def extract(filepath):
    with open(filepath, encoding="cp1252") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            row_id = row[0]
            try:
                answers = parse_answers(row[1:61])
                personality_type = parse_personality_type(row[61])
                yield TestAnswers(answers, personality_type)
            except (
                InvalidNumberOfAnswersError,
                InvalidAnswerTypeError, 
                InvalidAnswerValueError,
                InvalidPersonalityTypeError
            ) as e:
                logger.warning(f"Zeile ID={row_id} übersprungen: {e}")



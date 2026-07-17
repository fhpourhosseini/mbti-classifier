import numpy as np
from pipeline.transform import valid_types

def build_features(test_answers_list):
    return np.array([ta.answers for ta in test_answers_list])

def build_labels(test_answers_list):
    return np.array([valid_types.index(ta.personality_type) for ta in test_answers_list])


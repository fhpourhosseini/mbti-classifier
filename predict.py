import numpy as np
from tensorflow import keras
from pipeline.transform import valid_types, parse_answers

def predict_personality(answers, model_path="models/model.keras"):
    model = keras.models.load_model(model_path)
    parsed_answers = parse_answers(answers)
    X = np.array([parsed_answers])
    prediction = model.predict(X)
    predicted_index = np.argmax(prediction)
    return valid_types[predicted_index]

if __name__ == "__main__":
    example_answers = [1, -2, 0, 3, -1] * 12
    result = predict_personality(example_answers)
    print(f"Predicted personality type: {result}")


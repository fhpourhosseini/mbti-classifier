# MBTI Personality Classifier

Ein ML-Projekt, das den MBTI-Persönlichkeitstyp (16 Klassen) aus 60 Fragen (Werte -3 bis 3) vorhersagt. Umgesetzt mit einem MLP in TensorFlow/Keras.

## Setup

pip install -r requirements.txt

## Ausführen

Eigenen Test machen und Vorhersage bekommen:
python take_test.py

Vorhersage mit Beispiel-Antworten (ohne Test):
python predict.py

ETL-Pipeline testen:
python main.py

Modell neu trainieren:
python train.py

## Projektstruktur

- main.py – startet die ETL-Pipeline
- train.py – trainiert und vergleicht mehrere Modelle
- predict.py – lädt das Modell und macht eine Vorhersage
- take_test.py – stellt die 60 Fragen im Terminal und macht eine Vorhersage
- questions.py – die 60 Fragetexte
- data/ – Rohdaten (16P.csv)
- models/ – gespeichertes, trainiertes Modell
- pipeline/ – ETL-Code (extract, transform, errors, model)
- ml/ – ML-Code (dataset, trainer)

## Ergebnis

Bestes Modell: ~98.3 % Accuracy (Hidden Layers 265-128-64-32, Dropout 0.2)
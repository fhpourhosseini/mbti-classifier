from sklearn.model_selection import train_test_split
from main import main
from ml.dataset import build_features, build_labels
from ml.trainer import Trainer

data = main()
X = build_features(data)
y = build_labels(data)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model_configs = [
    {"hidden_layers": (32,), "dropout": 0.0},
    {"hidden_layers": (64, 32), "dropout": 0.0},
    {"hidden_layers": (64, 32), "dropout": 0.2},
    {"hidden_layers": (128, 64, 32), "dropout": 0.0},
    {"hidden_layers": (128, 64, 32), "dropout": 0.3},
]

candidates = []
for config in model_configs:
    trainer = Trainer(hidden_layers=config["hidden_layers"], dropout=config["dropout"])
    trainer.train(X_train, y_train)
    result = trainer.evaluate(X_test, y_test)
    print(f"{config} -> Accuracy: {result['accuracy']:.4f}")
    candidates.append((trainer, result["accuracy"]))

best_trainer, best_accuracy = max(candidates, key=lambda pair: pair[1])
best_trainer.save("models/model.keras")
print(f"Best model has accuracy: {best_accuracy:.4f}")
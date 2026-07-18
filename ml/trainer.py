from tensorflow import keras

class Trainer:
    def __init__(self, hidden_layers=(64, 32), dropout=0.0):
        self.hidden_layers = hidden_layers
        self.dropout = dropout

        layers = [keras.layers.Input(shape=(60,))]
        for units in hidden_layers:
            layers.append(keras.layers.Dense(units, activation="relu"))
            if dropout > 0:
                layers.append(keras.layers.Dropout(dropout))
        layers.append(keras.layers.Dense(16, activation="softmax"))

        self.model = keras.Sequential(layers)
        self.model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"]
    )

    def train(self, X_train, y_train, epochs=50):
        early_stopping = keras.callbacks.EarlyStopping(
            monitor="val_loss", patience=5, restore_best_weights=True
        )
        return self.model.fit(
            X_train, y_train,
            epochs=epochs,
            validation_split=0.2,
            callbacks=[early_stopping]
        )

    def evaluate(self, X_test, y_test):
        loss, accuracy = self.model.evaluate(X_test, y_test)
        return {"loss": loss, "accuracy": accuracy}

    def save(self, path):
        self.model.save(path)

    def __repr__(self):
        return f"Trainer(hidden_layers={self.hidden_layers}, dropout={self.dropout})"
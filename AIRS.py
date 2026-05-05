import numpy as np

#np.random.seed(42)

def generate_dummy_data(samples=20, features=5):
    X = np.random.rand(samples, features)
    y = np.random.randint(0, 2, samples)
    return X, y


class AIRS:
    def __init__(self, num_detectors=5):
        self.num_detectors = num_detectors

    def train(self, X, y):
        indices = np.random.choice(len(X), self.num_detectors, replace=False)

        print("Selected Detector Indices:", indices)

        self.detectors = X[indices]
        self.detector_labels = y[indices]

        print("\nSelected Detectors:")
        print(self.detectors)

        print("\nDetector Labels:")
        print(self.detector_labels)

    def predict(self, X):
        predictions = []

        for sample in X:
            distances = np.linalg.norm(self.detectors - sample, axis=1)
            nearest = np.argmin(distances)
            predictions.append(self.detector_labels[nearest])

        return predictions


X, y = generate_dummy_data()

split = int(0.8 * len(X))

train_X, test_X = X[:split], X[split:]
train_y, test_y = y[:split], y[split:]

airs = AIRS()
airs.train(train_X, train_y)

pred = airs.predict(test_X)

print("\nPredictions:", pred)
print("Actual Labels:", test_y)

accuracy = np.mean(pred == test_y)
print("\nAccuracy:", accuracy)

#Because dummy randomly generated data does not contain meaningful class patterns. The implementation demonstrates AIRS classification mechanics rather than real predictive performance.
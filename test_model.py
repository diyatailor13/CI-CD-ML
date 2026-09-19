import pickle


def test_model():

    # Load trained model
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)

    # Test input
    features = [[5.1, 3.5, 1.4, 0.2]]

    # Make prediction
    prediction = model.predict(features)

    # Check that prediction was generated
    assert prediction is not None

    # Check that prediction belongs to an Iris class
    assert prediction[0] in [0, 1, 2]
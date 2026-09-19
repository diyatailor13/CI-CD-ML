import pickle

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Iris flower measurements
# [sepal length, sepal width, petal length, petal width]
features = [[5.1, 3.5, 1.4, 0.2]]

# Make prediction
prediction = model.predict(features)

print("Input Features:", features)
print("Predicted Class:", prediction[0])

# Convert class number to flower name
if prediction[0] == 0:
    print("Predicted Flower: Setosa")
elif prediction[0] == 1:
    print("Predicted Flower: Versicolor")
else:
    print("Predicted Flower: Virginica")
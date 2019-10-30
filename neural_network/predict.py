from neural_network.common_functions import predict, prediction_to_label

text = ''

prediction = predict(text)
print(prediction)
print(prediction_to_label(prediction))

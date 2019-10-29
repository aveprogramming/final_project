from neural_network.common_functions import predict, prediction_to_label

text = '''Charles Kennedy is far too canny to make any grand claims about how his party may fare at the general election.In his 22 years in the Commons, he has seen his fair share of such claims dashed on the rocks of bitter experience and, he might say, the UK's political and electoral system. But even his caution cannot hide the fact that this is a party and a leader that believes it may well be on the way to something special in a few months' time. "Look, I have already said I am not going to put any artificial limits on our ambitions this time around," he said. He still seems to accept that the most likely outcome is another Labour victory of some sort. 
'''

prediction = predict(text)
print(prediction)
print(prediction_to_label(prediction))

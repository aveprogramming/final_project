import re
import numpy as np
import pickle
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[?|!|\'|"|#|]', r'', text)
    text = re.sub(r'[.|,|)|(|\|/]', r' ', text)
    text = re.sub('[0-9]+', '', text)
    text = text.strip()
    text = text.replace("\n", " ")
    text = re.sub(r'[\t+]', '', text)
    text = re.sub('[—|–|‐|“|“|®|²|•|µ|‡|°|º|±|−|│|∆|≤|·|]', ' ', text)
    text = re.sub('[ +]', ' ', text)
    return text


def y_encoder(labels):
    lab2idx = {'business': 0, 'politics': 1, 'tech': 2, 'showbiz':3}
    y = []
    for labs in labels:
        y_ = [0, 0, 0, 0]
        for lab in labs:
            try:
                y_[lab2idx[lab]] = 1
            except KeyError:
                continue
        y.append(y_)
    return np.array(y), lab2idx.keys()


def prediction_to_label(y_pred):
    lab2idx = {0: 'business', 1: 'politics', 2: 'tech', 3: 'showbiz'}
    label = []
    for i in range(len(y_pred)):
        if y_pred[i] == 1:
            label.append(lab2idx[i])
    return label


MAX_SEQUENCE_LENGTH = 100

with open('/Users/allateterukova/final_project/neural_network/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


def raw_data2vectors(_text,):

    _vectors = tokenizer.texts_to_sequences(_text)
    _vectors = pad_sequences(_vectors, maxlen=MAX_SEQUENCE_LENGTH)
    return _vectors


model = load_model('/Users/allateterukova/final_project/neural_network/classification_model.h5')


def predict(x):
    x = (clean_text(x))
    x = raw_data2vectors([x])
    # x_head = (clean_text(x_head))
    # x_head = raw_data2vectors([x_head])

    # y_pred = model.predict([x, x_head])
    y_pred = model.predict([x])
    y_pred[y_pred >= 0.35] = 1
    y_pred[y_pred < 0.35] = 0
    for predictions in y_pred:
        predictions = np.array(predictions, dtype='int')
        return predictions

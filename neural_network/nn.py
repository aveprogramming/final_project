import pandas as pd
import re
import pickle
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Embedding, SpatialDropout1D, LSTM, Bidirectional, Dense, BatchNormalization
from keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report
from neural_network.common_functions import y_encoder, raw_data2vectors


business = pd.read_csv('/Users/allateterukova/final_project/neural_network/dataset/business.txt', sep='\t', encoding='utf-8')
politics = pd.read_csv('/Users/allateterukova/final_project/neural_network/dataset/politics.txt', sep='\t', encoding='utf-8')
technology = pd.read_csv('/Users/allateterukova/final_project/neural_network/dataset/technology.txt', sep='\t', encoding='utf-8')
showbiz = pd.read_csv('/Users/allateterukova/final_project/neural_network/dataset/tvshowbiz.txt', sep='\t', encoding='utf-8')
business.columns = ['heading', "text", "label", 'time']
politics.columns = ['heading', "text", "label", 'time']
showbiz.columns = ['heading', "text", "label", 'time']
technology.columns = ['heading', "text", "label", 'time']
data = pd.concat([business, politics, technology, showbiz], axis=0)
data = data.drop(columns='time')
categories = ['business',  'politics',  'tech', 'showbiz']
# print(data.head(5))

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')


def clean_text(text):
    text = text.lower()
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    text = BAD_SYMBOLS_RE.sub('', text)
    text = text.replace('x', '')
    text = ' '.join(word for word in text.split())
    return text



data['text'] = data['text'].apply(clean_text)
data['text'] = data['text'].str.replace('\d+', '')


MAX_NB_WORDS = 50000
MAX_SEQUENCE_LENGTH = 100
EMBEDDING_DIM = 100
tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
tokenizer.fit_on_texts(data['text'].values)
word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

# X = tokenizer.texts_to_sequences(data['text'].values)
# X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)
X = raw_data2vectors(data['text'])
print('Shape of data tensor:', X.shape)


Y = y_encoder(data['label'].values)
print('Shape of label tensor:', Y.shape)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10, random_state=42)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)


model = Sequential()
model.add(Embedding(MAX_NB_WORDS, EMBEDDING_DIM, input_length=X.shape[1]))
model.add(BatchNormalization())
model.add(SpatialDropout1D(0.2))
model.add(Bidirectional(LSTM(300, dropout=0.5, recurrent_dropout=0.2)))
model.add(Dense(4, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

epochs = 10
batch_size = 512

history = model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size,validation_split=0.1,callbacks=[EarlyStopping(monitor='val_loss', patience=3, min_delta=0.0001)])

accr = model.evaluate(X_test, Y_test)
print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accr[0],accr[1]))

print(model.summary())


y_pred = model.predict(X_test)
y_pred[y_pred >= 0.35] = 1
y_pred[y_pred < 0.35] = 0


print(classification_report(Y_test, y_pred, target_names=categories))
model.save('classification_model.h5')

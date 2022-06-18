import numpy as np
import nltk
import json
import pickle
import re
import random
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from nltk.stem import WordNetLemmatizer
import tensorflow as tf


tokenized_words=[]
classes = []
doc = []
ignoring_words = ['?', '!']
data_file = open('intents.json').read()
intents = json.loads(data_file)

for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern) #tokenizing
        tokenized_words.extend(w)
        doc.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(words.lower()) for words in tokenized_words if w not in ignoring_words] #lemmatization

lemmatized_words = sorted(list(set(lemmatized_words))) 
classes = sorted(list(set(classes)))

pickle.dump(lemmatized_words,open('lem_words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

training_data = []

empty_array = [0] * len(classes)

for d in doc:

    bag_of_words = []

    pattern = d[0]

    pattern = [lemmatizer.lemmatize(word.lower()) for word in pattern]

    for w in lemmatized_words:

        bag_of_words.append(1) if w in pattern else bag_of_words.append(0)

    output_row = list(empty_array)

    output_row[classes.index(d[1])] = 1

    training_data.append([bag_of_words, output_row])

random.shuffle(training_data)

training = np.array(training_data)

train_x = list(training[:,0])

train_y = list(training[:,1])

bot_model = Sequential()
bot_model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
bot_model.add(Dropout(0.5))
bot_model.add(Dense(64, activation='relu'))
bot_model.add(Dropout(0.5))
bot_model.add(Dropout(0.25))
bot_model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = tf.keras.optimizers.SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
bot_model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

x_train = np.array(train_x)
y_train = np.array(train_y)
hist = bot_model.fit(x_train, y_train, epochs=200, batch_size=5, verbose=1)

bot_model.save('chatbot_model.h5', hist)
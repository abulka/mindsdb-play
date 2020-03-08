# Data taken from http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/

from mindsdb import Predictor
import pprint

DEBUG_LOG_LEVEL = 10
INFO_LOG_LEVEL = 20
WARNING_LOG_LEVEL = 30
ERROR_LOG_LEVEL = 40
NO_LOGS_LOG_LEVEL = 50

ANDY_LOGLEVEL = INFO_LOG_LEVEL

print("training")
# tell mindsDB what we want to learn and from what data
Predictor(name='spam_test', log_level=ANDY_LOGLEVEL).learn(
    to_predict='answer', # the column we want to learn to predict given all the data in the file
    from_data="spam_small.csv", # the path to the file where we can learn from, (note: can be url)
    use_gpu=False,
    stop_training_in_x_seconds=60
)

# use the model to make predictions
tests = [
    {'text': 'how are you going, what have you been doing today', 'is_spam': None, 'confidence': 0},
    {'text': 'ready to buy a new dvd today?', 'is_spam': None, 'confidence': 0},
    {'text': 'WINNER!!', 'is_spam': None, 'confidence': 0},
]
for test in tests:
    print("predicting...")
    result = Predictor(name='spam_test', log_level=ANDY_LOGLEVEL).predict(when={'conversation': test['text']})
    test['is_spam'] = result[0]['answer']
    test['confidence'] = result[0]['answer_confidence']

pprint.pprint(tests)
print("done")


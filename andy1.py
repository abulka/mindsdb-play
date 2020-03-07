from mindsdb import Predictor

DEBUG_LOG_LEVEL = 10
INFO_LOG_LEVEL = 20
WARNING_LOG_LEVEL = 30
ERROR_LOG_LEVEL = 40
NO_LOGS_LOG_LEVEL = 50

# tell mindsDB what we want to learn and from what data
Predictor(name='andy1_test', log_level=NO_LOGS_LOG_LEVEL).learn(
    to_predict='answer', # the column we want to learn to predict given all the data in the file
    from_data="andy1.csv", # the path to the file where we can learn from, (note: can be url)
    use_gpu=True
)

# use the model to make predictions
result = Predictor(name='andy1_test', log_level=NO_LOGS_LOG_LEVEL).predict(when={'info1': 1,'info2':1})
print(f"The predicted result for low numbers is {result[0]['answer']} with {result[0]['answer_confidence']}")

result = Predictor(name='andy1_test', log_level=NO_LOGS_LOG_LEVEL).predict(when={'info1': 500,'info2':500})
print(f"The predicted result for high numbers is {result[0]['answer']} with {result[0]['answer_confidence']}")

print("done")


"""
Script that trains graph-conv models on Tox21 dataset.
"""
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import os
import numpy as np
import pandas as pd
np.random.seed(123)
import tensorflow as tf
tf.set_random_seed(123)
import deepchem as dc
from datasets import load_tox21
import timeit

# Load Tox21 dataset
tox21_tasks, tox21_datasets, transformers = load_tox21(
        featurizer='GraphConv', split='random')
train_dataset, valid_dataset, test_dataset = tox21_datasets

# Fit models
metric = dc.metrics.Metric(
    dc.metrics.roc_auc_score, np.mean, mode="classification")

# Number of features on conv-mols
n_feat = 75
# Batch size of models
batch_size = 50
graph_model = dc.nn.SequentialGraph(n_feat)
graph_model.add(dc.nn.GraphConv(64, n_feat, activation='relu'))
graph_model.add(dc.nn.BatchNormalization(epsilon=1e-5, mode=1))
graph_model.add(dc.nn.GraphPool())
graph_model.add(dc.nn.GraphConv(64, 64, activation='relu'))
graph_model.add(dc.nn.BatchNormalization(epsilon=1e-5, mode=1))
graph_model.add(dc.nn.GraphPool())
# Gather Projection
graph_model.add(dc.nn.Dense(128, 64, activation='relu'))
graph_model.add(dc.nn.BatchNormalization(epsilon=1e-5, mode=1))
graph_model.add(dc.nn.GraphGather(batch_size, activation="tanh"))

model = dc.models.MultitaskGraphClassifier(
    graph_model,
    len(tox21_tasks),
    n_feat,
    batch_size=batch_size,
    learning_rate=0.0005,
    optimizer_type="adam",
    beta1=.9,
    beta2=.999)

start = timeit.default_timer()

# Fit trained model
model.fit(train_dataset, nb_epoch=10)

train_time = timeit.default_timer() - start

start = timeit.default_timer()

print("Evaluating model")
train_score, train_scores = model.evaluate(train_dataset, [metric], transformers, per_task_metrics=True)
valid_score, valid_scores = model.evaluate(valid_dataset, [metric], transformers, per_task_metrics=True)

eval_time = timeit.default_timer() - start

print("Train scores")
print(train_score)

print("Validation scores")
print(valid_score)

if not os.path.exists('log/tox21'): os.makedirs('log/tox21')
out = open('log/tox21/graph_conv.log', 'w')
out.write('Train scores: %s\n' % train_score)
out.write('Validation scores: %s\n' % valid_score)
out.write('Train time: %.1fm\n' % (train_time/60.))
out.write('Eval time: %.1fm\n' % (eval_time/60.))
out.close()

scores = [
        train_scores['mean-roc_auc_score'],
        valid_scores['mean-roc_auc_score'],
        ]
scores = pd.DataFrame(scores).T
scores.columns = ['train','valid']
scores.to_pickle('log/tox21/graph_conv.pkl')
Deep Learning for Virtual Screening
===================================

This template script can be used for benchmarking. 

Dependency
----------

- Keras 1.0.1  
  https://github.com/fchollet/keras  
  commit b1e47f7741cf526cb3381c4944f20582f368ba27

- intel Theano (0.80rc fork or later for work with Keras 1.0.1)

- intel Numpy (for intel Theano)

- pandas 0.15 (can be older version)
- scikit-learn 0.17 (can be older version)

Files
-----

- mlp.py  
Template script for parameter search.

- cpi.npz  
Sample data for predicting compound protein interactions.  
Download from https://my.syncplicity.com/share/vvks9oqxas1xneg/cpi

Usage
-----

    $ python
    >>> import numpy as np
    >>> np.load('cpi.npz')['data']
    array([[ 0.20235342,  0.13306834,  0.23337506, ...,  0.2016128 ,
             0.2054604 ,  1.        ],
           [ 0.15328281,  0.18236028,  0.15194339, ...,  0.08339998,
             0.11678988,  1.        ],
           [ 0.30227754,  0.05331679,  0.3800444 , ...,  0.04803333,
             0.04840195,  1.        ],
           ...,
           [ 0.3487972 ,  0.21659626,  0.3485468 , ...,  0.15965709,
             0.18344697,  0.        ],
           [ 0.20419115,  0.22017394,  0.20193382, ...,  0.07087177,
             0.06966367,  0.        ],
           [ 0.22705786,  0.16934164,  0.26198766, ...,  0.24239591,
             0.18216231,  0.        ]], dtype=float32)
    >>> CTRL-D

    $ python mlp.py cpi.npz
    Using Theano backend.
    Using gpu device 0: GeForce GTX TITAN X (CNMeM is disabled, CuDNN 4007)
    Data loading ...
    (248195, 1975)
    Train on 198556 samples, validate on 49639 samples
    Epoch 1/200
    198556/198556 [==============================] - 7s - loss: 0.8823 - val_loss: 0.9930
    Epoch 2/200
    198556/198556 [==============================] - 7s - loss: 0.6571 - val_loss: 1.2764
    Epoch 3/200
    198556/198556 [==============================] - 7s - loss: 0.6530 - val_loss: 1.0886
    Epoch 4/200
    198556/198556 [==============================] - 7s - loss: 0.6465 - val_loss: 1.0086
    Epoch 5/200
    198556/198556 [==============================] - 7s - loss: 0.6248 - val_loss: 1.2736
    Epoch 6/200
    198556/198556 [==============================] - 7s - loss: 0.5901 - val_loss: 0.7559
    Epoch 7/200
    198556/198556 [==============================] - 7s - loss: 0.5530 - val_loss: 0.8211
    Epoch 8/200
    198556/198556 [==============================] - 7s - loss: 0.5265 - val_loss: 1.1215
    Epoch 9/200
    198556/198556 [==============================] - 7s - loss: 0.4995 - val_loss: 0.7711
    Epoch 10/200
    198556/198556 [==============================] - 7s - loss: 0.4769 - val_loss: 0.7989
    Epoch 11/200
    198556/198556 [==============================] - 7s - loss: 0.4558 - val_loss: 0.7724
    Epoch 12/200
    198556/198556 [==============================] - 7s - loss: 0.4356 - val_loss: 1.1684
    Epoch 13/200
    198556/198556 [==============================] - 7s - loss: 0.4241 - val_loss: 0.8708
    Epoch 14/200
    198556/198556 [==============================] - 7s - loss: 0.4107 - val_loss: 0.7042
    Epoch 15/200
    198556/198556 [==============================] - 7s - loss: 0.3972 - val_loss: 0.8641
    Epoch 16/200
    198556/198556 [==============================] - 7s - loss: 0.3919 - val_loss: 0.8194
    Epoch 17/200
    198556/198556 [==============================] - 7s - loss: 0.3766 - val_loss: 0.5204
    Epoch 18/200
    198556/198556 [==============================] - 7s - loss: 0.3703 - val_loss: 0.8763
    Epoch 19/200
    198556/198556 [==============================] - 7s - loss: 0.3624 - val_loss: 0.5900
    Epoch 20/200
    198556/198556 [==============================] - 7s - loss: 0.3566 - val_loss: 0.6643
    Epoch 21/200
    198556/198556 [==============================] - 7s - loss: 0.3482 - val_loss: 0.5689
    Epoch 22/200
    198556/198556 [==============================] - 7s - loss: 0.3388 - val_loss: 0.5307
    Epoch 23/200
    198556/198556 [==============================] - 7s - loss: 0.3338 - val_loss: 0.6787
    Epoch 24/200
    198556/198556 [==============================] - 7s - loss: 0.3247 - val_loss: 0.6811
    Epoch 25/200
    198556/198556 [==============================] - 7s - loss: 0.3232 - val_loss: 0.9129
    Epoch 26/200
    198556/198556 [==============================] - 7s - loss: 0.3120 - val_loss: 0.6996
    Epoch 27/200
    198556/198556 [==============================] - 7s - loss: 0.3077 - val_loss: 0.6252
    Epoch 28/200
    198556/198556 [==============================] - 7s - loss: 0.3003 - val_loss: 0.6162
    Log file saved as result/cpi.npz_3000_1000_adam_sigmoid_200.log
    ran for 214.2s  

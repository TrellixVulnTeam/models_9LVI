from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import urllib

import numpy as np

import tensorflow as tf
from tensorflow.contrib import predictor

from memory_profiler import profile


def get_predictions(saved_model_path):
    predict_fn = predictor.from_saved_model(
        saved_model_path,
        signature_def_key='probabilities'
    )

    from official.resnet.cifar10_main import input_fn
    next_element = input_fn(
        False,
        data_dir='/tmp/cifar10_data',
        batch_size=128
    )[0]

    with tf.Session() as sess:
        next_element = sess.run(next_element)
        predictions = predict_fn({
            'input': next_element
        })
        return predictions['output'][0]

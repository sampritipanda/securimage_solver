from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import os.path
from datetime import datetime
from PIL import Image
import numpy as np

import tensorflow as tf
from tensorflow.python.platform import gfile
import captcha_model as captcha
from trim import trim

import config

IMAGE_WIDTH = config.IMAGE_WIDTH
IMAGE_HEIGHT = config.IMAGE_HEIGHT

CHAR_SETS = config.CHAR_SETS
CLASSES_NUM = config.CLASSES_NUM
CHARS_NUM = config.CHARS_NUM

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def one_hot_to_texts(recog_result):
    texts = []
    for i in xrange(recog_result.shape[0]):
        index = recog_result[i]
        texts.append(''.join([CHAR_SETS[i] for i in index]))
    return texts


def input_data(image_file):
    images = np.zeros([1, IMAGE_HEIGHT*IMAGE_WIDTH], dtype='float32')

    image = Image.open(image_file)
    image_ = trim(image)
    image.close()
    image = image_
    image_gray = image.convert('L')
    image_resize = image_gray.resize(size=(IMAGE_WIDTH,IMAGE_HEIGHT))
    input_img = np.array(image_resize, dtype='float32')
    input_img = np.multiply(input_img.flatten(), 1./255) - 0.5
    images[0,:] = input_img

    return images

def predict(image_file):
    with tf.Graph().as_default(), tf.device('/cpu:0'):
        input_images = input_data(image_file)
        images = tf.constant(input_images)
        logits = captcha.inference(images, keep_prob=1)
        result = captcha.output(logits)
        saver = tf.train.Saver()
        sess = tf.Session()
        saver.restore(sess, tf.train.latest_checkpoint('./captcha_train'))
        recog_result = sess.run(result)
        sess.close()
        text = one_hot_to_texts(recog_result)
        return text[0]

def main():
    path = sys.argv[1]
    print(predict(path))

if __name__ == '__main__':
    main()

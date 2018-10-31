from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
from os import path, environ
from datetime import datetime
from PIL import Image
import numpy as np

import tensorflow as tf
from tensorflow.python.platform import gfile
from securimage_solver.captcha_model import *
from securimage_solver.trim import trim

import securimage_solver.config as config

class CaptchaApi():
    def __init__(self):
        self.IMAGE_WIDTH = config.IMAGE_WIDTH
        self.IMAGE_HEIGHT = config.IMAGE_HEIGHT

        self.CHAR_SETS = config.CHAR_SETS
        self.CLASSES_NUM = config.CLASSES_NUM
        self.CHARS_NUM = config.CHARS_NUM
        self.checkpoint_path = path.join(path.dirname(__file__), 'captcha_train')

        environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    def one_hot_to_texts(self, recog_result):
        texts = []
        for i in range(recog_result.shape[0]):
            index = recog_result[i]
            texts.append(''.join([self.CHAR_SETS[i] for i in index]))
        return texts


    def input_data(self, image_file):
        images = np.zeros([1, self.IMAGE_HEIGHT*self.IMAGE_WIDTH], dtype='float32')

        image = Image.open(image_file)
        image_ = trim(image)
        image.close()
        image = image_
        image_gray = image.convert('L')
        image_resize = image_gray.resize(size=(self.IMAGE_WIDTH,self.IMAGE_HEIGHT))
        input_img = np.array(image_resize, dtype='float32')
        input_img = np.multiply(input_img.flatten(), 1./255) - 0.5
        images[0,:] = input_img

        return images

    def predict(self, image_file):
        with tf.Graph().as_default(), tf.device('/cpu:0'):
            input_images = self.input_data(image_file)
            images = tf.constant(input_images)
            logits = inference(images, keep_prob=1)
            result = output(logits)
            saver = tf.train.Saver()
            sess = tf.Session()
            saver.restore(sess, tf.train.latest_checkpoint(self.checkpoint_path))
            recog_result = sess.run(result)
            sess.close()
            text = self.one_hot_to_texts(recog_result)
            return text[0]

if __name__ == '__main__':
    capi = CaptchaApi()
    print(capi.predict("images/7NwHCn_141c1458-b5e4-439f-be01-8a8b30c6cbd8.png"))
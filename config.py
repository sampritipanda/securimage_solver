# about captcha image
IMAGE_HEIGHT = 48
IMAGE_WIDTH = 176
CHAR_SETS = 'ABCDEFGHKLMNPRSTUVWYZabcdefghklmnprstuvwyz23456789'
CLASSES_NUM = len(CHAR_SETS)
CHARS_NUM = 6
# for train
RECORD_DIR = './data'
TRAIN_FILE = 'train.tfrecords'
VALID_FILE = 'valid.tfrecords'


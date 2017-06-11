from decoder_wrapper import *

def generate(vec_of_words):
    return get_predict(vec_of_words)

print(generate('the influence of our words'.split()))

import pickle, gensim
from gensim.models import Word2Vec

job_path = 'w2v_jobs'
data_path = 'data/'
wiki_file = job_path + '/wiki.out'
smo_file = job_path + '/trainning.out'
test_file = data_path + 'questions-words.txt'
#questions = open(test_file, 'r').readlines()

def model_to_vectors(filename):
    model = pickle.load( open(filename, 'rb'))
    word_vectors = model.mv
    with open(job_path + 'word_vectors.out', 'wb') as f:
        f.write(pickle.dumps(word_vectors))
def cal_accuracy(filename):
    model = pickle.load( open(filename, 'rb'))
    accuracy = model.accuracy(test_file)
    
    sum_correct = len(accuracy[-1]['correct'])
    print(sum_correct)
    sum_incorrect = len(accuracy[-1]['incorrect'])
    total = sum_correct + sum_incorrect
    percentage = lambda a: a / total * 100
    print(filename + ': Total sentences: {}, Correct: {:.2f}%, Incorrect: {:.2f}%'.format(total, percentage(sum_correct), percentage(sum_incorrect)))

def load_vectors():
    word_vectors = pickle.load(open(job_path + 'word_vectors.out', 'rb'))


if __name__ == "__main__":
    cal_accuracy(wiki_file)
    cal_accuracy(smo_file)
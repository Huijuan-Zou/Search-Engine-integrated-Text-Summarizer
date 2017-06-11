# README #
This project contains work from Zeleng Zhuang and Huijuan Zou.

This is a final project for the course Search Engine Architecture

### How do I get set up? ###

If you want to see how our model works, try the following url:
```
http://linserv2.cims.nyu.edu:34233/?q=This+is+sample+text
```
Attention: This may take a while for the web page to load, please wait with patience.

You can replace the text after 'q=' and please separate it by '+'
ex:
```
http://linserv2.cims.nyu.edu:34233/?q=Yen+drops+as+European+and+Japanese+stocks+start+week+higher.+*+U.S.+data+fails+to+provide+clarity+on+Fed+rate-hike+timing.+*+Speculators+cut+U.S.+dollar+longs+to+lowest+in+over+a+year+-CFTC
```

If you want to set it up, please revise the `BASE MODEL`, and run
```
python server.py
```
given you has installed all the required library and an appropriate python version(It works with python3 but it didn't work with python 3.6. Please use python 3.5)

As the training data is very large, it is not possible for us to provide the training data, but you can find it here:
```
http://research.signalmedia.co/newsir16/signal-dataset.html.
```
But we do provide our trained model as checkpoints files.

### How it works ###
For detail of the implementation, please refer to our paper here:
`https://bitbucket.org/ZelengZhuang/search-engine-architecture-final-project/src/340051975247488b5d1dc53420909e749ec7540a/paper.pdf?at=master&fileviewer=file-view-default
`

### Reference ###
We use GloVe which can be found here:
`https://nlp.stanford.edu/projects/glove/`

We use tornado as our backend server. For training we use Tensorflow and Keras. Also, we use popular data science such like nltk and numpy, etc

For word2vec part:
python reformatter_json.py data/train.jsonl --job_path w2v_jobs --num_partitions 5
(or python reformatter_xml.py data/info_ret.xml --job_path w2v_jobs --num_partitions 5)
python -m gradient
python -m init_model --app apps.word2vec --job_path w2v_jobs
python -m update_model --app apps.word2vec --job_path w2v_jobs --iterations 50

run accuracy file:
python test_accuracy.py

run model file at w2v_jobs/0.out to use the model
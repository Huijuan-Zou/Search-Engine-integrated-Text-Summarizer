
part of the code is based are on from Professor Doherty’s class.
check: http://cs.nyu.edu/courses/spring17/CSCI-GA.3033-006/syllabus.html

instruction:
cd word2vec
python reformatter_json.py data/train.jsonl --job_path w2v_jobs --num_partitions 5
(or python reformatter_xml.py data/info_ret.xml --job_path w2v_jobs --num_partitions 5)
python -m gradient
python -m init_model --app apps.word2vec --job_path w2v_jobs
python -m update_model --app apps.word2vec --job_path w2v_jobs --iterations 50

run accuracy file:
python test_accuracy.py

run model file at w2v_jobs/0.out to use the model




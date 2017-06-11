from argparse import ArgumentParser
import os, importlib, pickle

def main():
    parser = ArgumentParser()
    parser.add_argument("--app", dest = "apps",required=True)
    parser.add_argument("--job_path", dest = "job_path", required=True)
    args = parser.parse_args()
    global files, cur_model, app, iterations, compute_gradient, gradients
    app = args.apps
    job_path = args.job_path
    
    files = []
    for f in os.listdir(job_path):
        if f.endswith('.in'):
            files.append(job_path + "/" + f)

    word2vec = importlib.import_module(app)
    init_model = getattr(word2vec, 'init_model')
    cur_model = init_model(files)
    
    outFile = str(job_path) + "/init.out"
    with open(outFile, 'wb') as f:
        f.write(pickle.dumps(cur_model))
if __name__ == "__main__":
    main()
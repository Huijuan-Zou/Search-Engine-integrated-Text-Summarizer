#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#reformatter for json file
import argparse, string, json

UGLY_TEXT_MAP = dict([(ord(char), ' ') for char in string.punctuation + "“”‘’–—"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("--num_partitions", type=int, required=True)
    parser.add_argument("--job_path", required=True)
    args = parser.parse_args()
    
    num_lines = 0
    headlines = None
    with open(args.filename, 'r') as myFile:
        for line in myFile:
            num_lines += 1
          
    chunk_size = num_lines // args.num_partitions + 1
    output = None
    
    with open(args.filename, 'r') as myFile:
        docId = 0
        for line in myFile:
            cur_news = json.loads(line)
            if docId % chunk_size == 0:
                output = open(args.job_path + "/" + str(int(docId / chunk_size)) + ".in", "w")
            docId += 1
            text = cur_news['content']
            text = text.translate(UGLY_TEXT_MAP).replace('\n', ' ').lower().split()
            text = ' '.join(text)
            output.write("%s\n" % text.encode())
    output.close()
        
    
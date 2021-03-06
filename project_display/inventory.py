import hashlib, getpass

NUM_INDEX_SHARDS = 3
NUM_DOC_SHARDS = 3
MAX_PORT = 49152
MIN_PORT = 10000
BASE_PORT = int(hashlib.md5(getpass.getuser().encode()).hexdigest()[:8], 16) % \
(MAX_PORT - MIN_PORT) + MIN_PORT + 138
#BASE_PORT = 23124

servers = {}
servers['web'] = ["127.0.0.1:%d" % (BASE_PORT)]
servers['index'] = ["127.0.0.1:%d" % (port)
  for port in range(BASE_PORT + 1,
                    BASE_PORT + 1 + NUM_INDEX_SHARDS)]
servers['doc'] = ["127.0.0.1:%d" % (port)
  for port in range(BASE_PORT + 1 + NUM_INDEX_SHARDS,
                    BASE_PORT + 1 + NUM_INDEX_SHARDS + NUM_DOC_SHARDS)]

DF_STORE = "idf_jobs/0.out"
DOCS_STORE = "docs_jobs/%d.out"
POSTINGS_STORE = "invindex_jobs/%d.out"
GEN_STORE = "title_to_generated_content.p"
WEBAPP_PATH = "webapp/"



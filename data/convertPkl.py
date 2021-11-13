import sys
ori = "./data/flame_static_embedding_68.pkl"
dest = "./data/flame_static_embedding_68_new.pkl"

content = ''
outsize = 0
with open(ori,'rb') as infile:
    content=infile.read()
with open(dest,'wb') as outfile:
    for line in content.splitlines():
        outsize+=len(line)+1
        outfile.write(line+str.encode('\n'))

#!/usr/bin/env python
import sys


def make_chunk(infile, outfile, max_lines):
    count = 0
    for line in infile:
        if line:
            outfile.write(line)
            count += 1
        if count >= max_lines:
            outfile.close()
            return False
    return True

num_chunks = int(sys.argv[1])
count = 0
with open('/usr/share/wordlists/rockyou.txt','r') as infile:
    for line in infile:
        count += 1

print('Total lines in rockyou.txt is: %i' % count)
chunk_size = count / num_chunks
print('Entries per chunk will be: %i' % chunk_size)
count = 0
with open('/usr/share/wordlists/rockyou.txt','r') as infile:
        try:
            done = False
            current_chunk = 0
            while not done:
                outfile_fn = '/tmp/chunk%i.txt' % current_chunk
                outfile = open(outfile_fn, 'w')
                done = make_chunk(infile, outfile, chunk_size)
                current_chunk += 1
        except Exception as e:
            print(e)
            sys.exit(1)

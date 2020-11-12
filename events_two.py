# import sys

# src_path = sys.argv[1] if len(sys.argv) > 1 else '.'

import os 
#dir_path = os.path.dirname(os.path.realpath(__file__))

path2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'FTP1')
# print (src_path)
print (path2)
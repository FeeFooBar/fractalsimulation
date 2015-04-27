import re
import sys

infile = open(sys.argv[1],'r').read()

pat = re.compile(r'number_spheres\n\d*\n')

match = re.search(pat,infile)
replacement = re.sub(pat,'number_spheres\n'+sys.argv[2]+'\n',infile)


output = open(sys.argv[1],'w')
output.write(replacement)

output.close()

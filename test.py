import os
os.mkdir('2')
with open(os.path.join('2', '2.txt'), 'a') as f:
	f.write('1111')

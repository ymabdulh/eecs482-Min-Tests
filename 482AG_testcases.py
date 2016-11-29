import itertools

test_list = [] # contains tuples of (testcase_filename, str bugs_found)

def get_filelist(test_list, allbugs):
	for i in range(2, len(allbugs)):
		for comb in itertools.combinations(test_list, i):
			s = set().copy()
			iter_filenames = []
			for tup in comb:
				s.update(tup[1])
				iter_filenames.append(tup[0])
			
			if len(s)+1 == len(allbugs):
				return iter_filenames

	return False

# read in files
with open("testcase_results.txt") as f:
	allbugs = next(f)
	for line in f:
		test_list.append(tuple(line.split()))

s = set()
for i in test_list:
	s.update(i[1])

res = get_filelist(test_list, allbugs)

print
if res:
	print 'finding ' + str(len(allbugs)-1) + ' bugs'
	print 'number of files to include: ' + str(len(res))
	print '-----------------------------'
	for line in res:
		print line
else:
	print 'an error has occured'
print

import os

def get_files(suffix, path, files = []):
	if os.path.isfile(path) and path.endswith(suffix):
		return files.append(path)
	if os.path.isdir(path):
		listdir = os.listdir(path)
		for item in listdir:
			new_path = os.path.join(path, item).replace("\\", "/")
			if os.path.isfile(new_path) and new_path.endswith(suffix):
				files.append(new_path)
			else:
				files = get_files(suffix, new_path, files)
	return files

def find_files(suffix, path):
	if not path:
		return "Path is empty"

	file_paths = get_files(suffix, path, [])
	
	if len(file_paths) == 0:
		return "Files not found with suffix {}".format(suffix)
	return file_paths
    

# Test cases

print (f'**** TestCase 1 ****\n')
# First case for suffix ".c"
required_files = find_files(".c", "./testdir")
print (required_files)
# should print four files namely:
# ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

print (f'\n**** TestCase 2 ****\n')
# Second case for suffix ".h" and "testdir\subdir1"
required_files = find_files(".h", "./testdir/subdir1")
print (required_files)
# should print 1 file path
# ['./testdir/subdir1/a.h']

print (f'\n**** TestCase 3 ****\n')
# Third test case
required_files = find_files(".py", "")
print (required_files)
# Prints : Path is empty


print (f'\n**** TestCase 4 ****\n')
# Fourth test case
required_files = find_files(".py", "/testdir")
print (required_files)
# Prints : Files not found with suffix .py
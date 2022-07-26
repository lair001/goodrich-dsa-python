Python’s os module provides a function with signature walk(path) that
is a generator yielding the tuple (dirpath, dirnames, filenames) for each
subdirectory of the directory identified by string path, such that string
dirpath is the full path to the subdirectory, dirnames is a list of the names
of the subdirectories within dirpath, and filenames is a list of the names
of non-directory entries of dirpath. For example, when visiting the cs016
subdirectory of the file system shown in Figure 4.6, the walk would yield
( '/user/rt/courses/cs016' , '[ homeworks , programs ]', '[ grades ]').
Give your own implementation of such a walk function.
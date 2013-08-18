#!/usr/bin/python

import os
import shutil

for dirname, subdirs, filenames in os.walk('.'):
		for subdirname in subdirs:
				if '.svn' == subdirname:
								print (os.path.join(dirname,subdirname))
								shutil.rmtree(os.path.join(dirname,subdirname))
								#for a, b, c in os.walk(os.path.join(dirname,subdirname)):
								#		print os.path.join(a,c)
					#	os.removedirs(os.path.join(dirname,subdirname))

				

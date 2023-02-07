
import os
import shutil
import sys
import getopt
import gui
import tkdiff
try:
	opts, args = getopt.getopt(sys.argv[1:], "hf:s:", ["help","firstFile=", "secondFile="])
except getopt.GetoptError as err:
  print(err)  # will print something like "option -a not recognized"
  sys.exit(0)
firstFileExist = False
secondFileExist = False
for o, a in opts:
  if o in ("-h", "--help"):
    print("arguments:\n	--firstFile <firstName>\n	--secondFile <secondFile>\n	[-h,--help :get help massage.]\n")
    sys.exit(1)
  elif o in ("--firstFile"):
    firstFile=a
    firstFileExist = True
  elif o in ("--secondFile"):
    secondFile=a
    secondFileExist = True
  else:
    print("option "+o+" not recognized")
    sys.exit(2)

if firstFileExist == False or secondFileExist == False:
  print("firstFile and secondFile args is mandatory, check -h or --help")
  sys.exit(3)
d=tkdiff.tkdiffMethod(str(firstFile),str(secondFile))
difference = list(d)
difference = '\n'.join(difference)
print (difference)
d=tkdiff.tkdiffMethod(str(firstFile),str(secondFile))
gui.init(str(firstFile),str(secondFile),d)

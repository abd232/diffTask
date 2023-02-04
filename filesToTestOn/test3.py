import os
import shutil
import sys
import getopt
try:
	opts, args = getopt.getopt(sys.argv[1:], "hf:l", ["help","firstName=", "lastName="])
except getopt.GetoptError as err:
  print(err)  # will print something like "option -a not recognized"
  sys.exit(0)
cap = False
lastName="Abdalrhman"
firstNameExist = False
for o, a in opts:
  if o in ("--cap"):
    cap = True
  elif o in ("-h", "--help"):
    print("arguments:\n	--firstName <firstName>\n	[--lastName <lastName>]\n	[-h,--help :get help massage.]\n	[--cap :prints the names in capital letters]")
    sys.exit(1)
  elif o in ("--firstName"):
    firstName=a
    firstNameExist = True
  elif o in ("--lastName"):
    lastName=a
  else:
    print("option "+o+" not recognized")
    sys.exit(2)

if firstNameExist == False :
  print("first_name arg is mandatory, check -h or --help")
  sys.exit(3)
if cap:
  firstName=firstName.upper()
  lastName=lastName.upper()
parent_dir = str(os.environ.get('HOME'))
directory="tmp"
path = os.path.join(parent_dir,directory)
shutil.rmtree(path, ignore_errors=True)
os.mkdir(path)
parent_dir = path
for x in [1, 2, 3, 4, 5]:
  directory="training_project_"+str(x)
  path = os.path.join(parent_dir,directory)
  os.mkdir(path)
  with open(path + '/module_'+str(x)+'a.txt', 'x') as f:
    f.write('Hello '+firstName+' welcome to file '+str(x)+'.A')
  with open(path + '/module_'+str(x)+'b.txt', 'x') as f:
    f.write('Hello '+lastName+' welcome to file '+str(x)+'.B')

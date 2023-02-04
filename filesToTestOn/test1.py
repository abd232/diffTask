import os
import shutil
firstName = 'Abdallah'
lastName = 'Abdalrhman'
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

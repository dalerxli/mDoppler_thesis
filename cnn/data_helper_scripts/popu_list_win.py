import sys
import glob
import errno
import re

path = '.\SquaredImages\TrainingSTFTOneSecondNoisy90\*.png'
wPath = '.\input_list_train_STFT1SN90.txt'
fW = open(wPath,'w')
files = glob.glob(path)  

print("Searching for train .png format images, through directory: " + path)

# train set
p = re.compile('[WRB]_.+.png')
 
for name in sorted(files): # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
  try:
      strName = p.findall(name).pop()
      #print strName + '\n'
      if strName[0:2] == 'W_':
        fW.write(strName + ' ' + '0' + '\n')
      elif strName[0:2] == 'R_':
        fW.write(strName + ' ' + '1' + '\n')
      elif strName[0:2] == 'B_':
        fW.write(strName + ' ' + '2' + '\n')        
    #with open(name) as f: # No need to specify 'r': this is the default.
    #    sys.stdout.write(f.read())
  except IOError as exc:
    if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
      raise # Propagate other kinds of IOError.
fW.close()


# test set
path = '.\SquaredImages\TrainingSTFTOneSecondNoisy90\Testing\*.png'
wPath = '.\input_list_test_STFT1SN90.txt'
fW = open(wPath,'w')
files = glob.glob(path)  

print("Searching for test .png format images, through directory: " + path)

p = re.compile('[WRB]_.+.png')
 
for name in sorted(files): # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
  try:
      strName = p.findall(name).pop()
      if strName[0:2] == 'W_':
        fW.write(strName + ' ' + '0' + '\n')
      elif strName[0:2] == 'R_':
        fW.write(strName + ' ' + '1' + '\n')
      elif strName[0:2] == 'B_':
        fW.write(strName + ' ' + '2' + '\n')        
    #with open(name) as f: # No need to specify 'r': this is the default.
    #    sys.stdout.write(f.read())
  except IOError as exc:
    if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
      raise # Propagate other kinds of IOError.
fW.close()

print("File 'test.txt' created in directory: \n" + wPath + '.')

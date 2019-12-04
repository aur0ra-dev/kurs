instruction = ['Say hello', 'Say how are you', 'Ask for money',  'Say thank you', 'Say bye']
instructionApproved = []

'''
for instr in instruction: 
    print('Adding instruction', instr)
    instructionApproved.append(instr)

    if instr == 'abort':
        print("Aborting!!!")
        instructionApproved.clear()
        break
# w takim wypadku gdy wystapi abort instrukcja po else nie wykona sie 
else: 
    print('following action will be taken', instructionApproved)
'''

'''
instructionApproved.clear()
i = 0
while i < len(instruction):
     print('Adding instruction', instruction[i])
     instructionApproved.append(instruction[i])

     if instruction[i] == 'abort':
        print("Aborting!!!")
        instructionApproved.clear()
        break
    i+=1
else:
    print('following action will be taken', instructionApproved)   
'''

import urllib.request
import os
 
data_dir = 'c:/temp'
pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]
 
for page in pages:
 
    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)
 
        print("Processing: {}  => {} ...".format(page["url"], file_name))
        urllib.request.urlretrieve (page["url"], path)
        print('...done')
        
    except:
        print('FAILURE processing web page: {}'.format(page["name"]))
        print('Stopping the process!')
        break
 
else:
    print('All pages downloaded successfully!!!')

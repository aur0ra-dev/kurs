import os 

path = r'c:\temp\mydata.txt'



'''
if os.path.isfile(path): 
    print("File %s exist" % path)
else:
    print("Creating a file %s" % path)
    open(path, 'x').close()
    print("File %s created" % path )
'''
#os.remove(path)
# mamy do spelniania dwa warunki python sprawdza je po kolei dlatego oszacował wartosc pierwszej czesci jako false
# następnie przeszedl do kolejnej czesci kodu .close() nic nie zwarca dlatego zwraca none    
# po ponownym wykonaniu programu python zwraca true bo pierwsza wartosc zwraca true 
'''
result = os.path.isfile(path) and  open(path, 'x').close()
# w momencie kiedy python inerpretuje wyrazenia logiczne interpretuje od lewej do prawej 
# jezeli pierwsze zwraca true to zwraca true 
print(result)
'''

def funkcja(path): 
    with open(path) as f:
        siemano = f.read()
        policz = len(siemano.split())
    return policz

funkcja(path)

if os.path.isfile(path): 
    print("File %s exist" % path)

os.path.isfile(path) and print("There are {} words in  file {}".format(funkcja(path), path))



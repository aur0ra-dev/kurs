listOfErros = [101,102,103]  
#jezeli wartosc zmienna jest napisem zawsze jest interpretowany jako TRUE. dlatego nie uzywamy ich w przypadku wartosci bool
#int rowniez zwracaja wartosc true oprocz 0 - zwraca FALSE
#Kontenery rowniez zwracaja wartos TRUE, kiedy są puste zwracaja FALSE 
#Gdy odwołujemy się do jej elementow to moze zwaracac FALSE 
print('Variable isOk: ', listOfErros, type(listOfErros))
if len(listOfErros) > 0:  
    print('TRUE')


'''
options = ['load data', 'export data', 'analyze & predict']



def DisplayOptions(options):
    print("1 - ", options[0])
    print("2 - ", options[1])
    print("3 - ", options[2])
    choice = input('Podaj wartosc z listy options: ')
    return str(choice)

choice = 'x'

while choice:
    choice = DisplayOptions(options)
    if choice:
        try:
            choice_num = int(choice)-1
            if choice_num >= 0 and choice_num < len(options):
                print("wybrałes opcje: ", options[choice_num])
            else:
                print("wybierz wartość z listy")
        except:
            print("Wybrałeś złą watość")
    else:
        print("======END=====")
'''
'''
def DisplayOptions(options):
    for i in range(len(options)):
        print("{} - {}".format(i+1, options[i]))
 
    choice = input('Select option above or press enter to exit: ')
    return choice
    
 
choice='x'
options = ['load data', 'export data', 'analyze & predict']
 
while choice:
 
    choice = DisplayOptions(options)
 
    #executed only if something was entered
    if choice:
        try:
            choice_num = int(choice)-1
            if choice_num >=0 and choice_num < len(options):
                print("you have selected {} - {}".format(choice_num+1, options[choice_num]))
            else:
                print("choose a value from a list or press enter")
        except:
            print("You need to enter a number")
    else:
        print('----- END -----')
'''



tab = ["chuj", "pizdunia", "pizdeczka"]
def siemano(tab):
    for i in range(len(tab)): 
        print("{} - {}".format(i+1, tab[i]))

siemano(tab)

dict = {
        ('A','Clean') : 'Right',
        ('A','Dirty') : 'Suck',
        ('B','Clean') : 'Left',
        ('B', 'Dirty'): 'Suck',
        (('A', 'Clean'), ('A','Clean')): 'Right',
        (('A', 'Clean'), ('A', 'Dirty')): 'Suck',
        (('A', 'Clean'), ('A', 'Clean'),('A', 'Clean')): 'Right',
        (('A', 'Clean'), ('A', 'Clean'), ('A', 'Dirty')): 'Suck'

    }
print("")
print(dict.items())
print("")

for key, value in dict.items():
        print(key,"  ",value)
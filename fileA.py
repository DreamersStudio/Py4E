#handle = open('../code3/mbox.txt')
#print(handle)

xfile = open('../code3/mbox.txt')
#for cheese in xfile:
#    print(cheese)
    
fhand = open('../code3/mbox-short.txt')
count = 0
for line in fhand:
    #count = count + 1
    #print(line)
    line = line.rstrip()
    if line.startswith('From'):
        print(line)
        count = count + 1
print('Line Count:', count)

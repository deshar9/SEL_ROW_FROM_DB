import csv

def main():

    y = open('TEST_CSV.csv', 'r')
    reader = csv.reader(y, delimiter=',')

    for k in reader:
        x = open('Master Config.txt','r')
        print (k[0])
        z = open('{0}.txt'.format(k[0]),'w')
        line = 1
        for i in x:
            if line==9:
                z.write('                 address {0};\n'.format(k[1]))
            elif line==16:
                z.write('                 address {0};\n'.format(k[2]))
            elif line==23:
                z.write('                 address {0};\n'.format(k[3]))
            else:
                z.write(i)
            line+=1
        x.close()
        z.close()

    y.close()

if __name__=="__main__":
    main()

def writefile():

    kaartnummers = open('kaartnummers.txt', 'w')
    kaartnummers.write('325255, Jan Jansen')
    kaartnummers.write('\n''334343, Erik Materus')
    kaartnummers.write('\n''235434, Ali Ahson')
    kaartnummers.write('\n''645345, Eva Versteeg')
    kaartnummers.write('\n''534545, Jan de Wilde')
    kaartnummers.write('\n''345355, Henk de Vries')

def uitvoer(file):
    file = open(file, 'r')
    lines = file.readlines()
    count = 0;
    for line in lines:
        line = line.rstrip('\n');
        value = line.split(', ');
        count += 1;
        number = value[0]
        name = value[1]
        print(name + ' heeft kaartnummer: ' + number);
    print(count);

    file.close()

uitvoer('kaartnummers.txt');
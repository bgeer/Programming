def convert(tc):
    tf = tc * 1.8 + 32;
    return tf

def table(min,max):
    print('Celcius' + '\t'*2 + 'Fahrenheit')
    for i in range(min,max+1,10):
        print(str(i) + '\t'*3 +  str(convert(i)))
    return '----------------'

print(table(-30,40));

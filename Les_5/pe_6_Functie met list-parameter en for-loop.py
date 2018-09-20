gt = [ 4, 5, 3, -81];

def kwadraten_som(grondgetallen):
    positive = []
    som = 0;

    for x in grondgetallen:
        if x >= 0:
            positive.append(x);
    for o in positive:
        z = o**2;
        som = som +z;

    return som


print(kwadraten_som(gt));
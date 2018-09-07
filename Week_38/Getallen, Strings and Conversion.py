cijferICOR = 5.5
cijferPROG = 7.5
cijferCSN = 6.5

gemiddelde = round(((cijferCSN + cijferPROG + cijferCSN)/3), 2)
beloning = (cijferPROG + cijferICOR + cijferCSN) * 10
overzicht = 'Mijn cijfers(gemiddeld een ' + str(gemiddelde) + ' ) leveren een beloning van ' + str(beloning) + ' op!'
print(overzicht);

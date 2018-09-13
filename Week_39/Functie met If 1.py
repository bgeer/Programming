def lang_genoeg(len):
    if len >= 120:
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'Sorry, je bent te klein!'

lengte = int(input('Hoe lang ben je? '));
print(lang_genoeg(lengte));
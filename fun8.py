def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


# ile miniumum argumentow trzeba podac
allparams(1, 2)
allparams(1, 2, 3)
allparams(1, 2, c=3)
# allparams(b=1, a=2, c=3)
# TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# / - oddziela argumenty pozycyjne od nazwanych
# a i b mogą byc tylko po kolejności
allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, 9)
# args (4, 4, 5, 6, 7, 8, 9)
allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, 9)
allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, 100, 106, 10987)
# args (4, 4, 5, 6, 7, 8, 100, 106, 10987)
allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, 9, d=129)  # c, d 3 129
allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, 9, d=129, klucz='wart')  # c, d 3 129
allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, 9, d=129, klucz='wart')  # c, d 3 129
# kwargs {'klucz': 'wart'}
allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, 9, d=129, klucz='wart', a=8)
# kwargs {'klucz': 'wart', 'a': 8}
# args i kwargs moga byc raz w argumentach

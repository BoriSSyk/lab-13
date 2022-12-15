class ROCK():

    def __init__(self, a='none', b=0.0, c='none', d='none'):
        self.name = a
        self.high = b
        self.continent = c
        self.countrie = d

    def set_name(self, aa):
        self.name = str(aa)

    def set_high(self, bb):
        self.high = float(bb)

    def set_continent(self, cc):
        self.continent = str(cc)

    def set_countrie(self, dd):
        self.countrie = str(dd)


r = ROCK()

mountains = [['Еверест', (8848, 86), 'Китай', 'Азія'], [
    'Кіліманджаро', 5881, 'Танзанія', 'Африка']]

print(mountains)

x = input('Введіть дію:')
while x != 'stop':
    x = input('Введіть дію:')
    if x == "1":

        spisok = []

        r.set_name = input('Введіть назву:')
        r.set_high = input('Висота:')
        r.set_countrie = input('Країна:')
        r.set_continent = input('Континент:')

        spisok.append(r.set_name)
        spisok.append(r.set_high)
        spisok.append(r.set_countrie)
        spisok.append(r.set_continent)

        mountains.append(spisok)

        print(mountains)

    elif x == '2':
        mountains.sort()

        print(mountains)

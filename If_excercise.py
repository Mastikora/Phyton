'''
Sklep odzieżowy uruchamiał promocję tylko jeżeli ilość lajków była większa lub równa 500
a ilość udostępnień co najmniej 100.
Kiedy oba warunki były spełnione sprawa była prosta - rozpoczynała się obniżka cen.
Kiedy jednak brakowało lajków lub udostępnień, to wypadałoby dać znać czego brak.

Spełnione - świetnie, rozpoczynamy promocj
jeśli brakuje lajków wyświetl informację o braku lakjów
w przeciwnym razie (musi brakować udostępnień - to logiczne!) -braku udostępnień
'''

maxlajk = 500
maxshare = 100

lajk = 400000
share = 20

if lajk < maxlajk :
    print('Za mało lajków')
elif share < maxshare:
    print('Za mało udostepień')
else:
    print('Obniżka cen')

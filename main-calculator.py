import important

print('witaj w kalkulatorze, wybierz opcję')
print('policzyć można pola, obwody, objętości, rożnice i sumę objętości, pola i obwody pewnych figur')
print('aby wyjść wpisz koniec')
print('opcja a: pole kuli')
print('opcja b: objętość kuli')
print('opcja c: pole całkowite ostrosłupa')
print('opcja d: objętość ostrosłupa')
print('opcja e: pole kostki')
print('opcja f: objętość kostki')
print('opcja g: obwód kwadratu')
print('opcja h: obwód koła')
print('opcja i: pole równoległoboku')
print('opcja j: pole stożka')
print('opcja k: objętość stożka')
print('opcja l: obwód trójkąta')
print('opcja m: pole walca')
print('opcja n: objętość walca')
print('opcja o: obwód prostokąta')
print('opcja p: suma objętości kuli i objętości kostki')
print('opcja q: różnica pola kostki i pola stożka')
print('opcja r: różnica obwodu koła i obwodu trójkąta')


liczenie = input('co chcesz policzyc? wpisz literę = ').lower()
 
if liczenie == 'a':
    r = float(input('r = '))
    print(calculatorhomework.p_kuli(r))
elif liczenie == 'b':
   r = float(input('r = '))
   print(calculatorhomework.v_kuli(r))
elif liczenie == 'c':
    pp = float(input('pp = '))
    pb = float(input('pc = '))
    print(calculatorhomework.pc_ostrosłupa(pp,pb))
elif liczenie == 'd':
    pp = float(input('pp = '))
    H = float(input('H = '))
    print(calculatorhomework.pc_ostrosłupa(pp,H))
elif liczenie == 'e':
    a = float(input('a = '))
    print(calculatorhomework.p_kostki(a))
elif liczenie == 'f':
    a = float(input('a = '))
    print(calculatorhomework.v_kostki(a))
elif liczenie == 'g':
    a = float(input('a = '))
    print(calculatorhomework.obw_kwadratu(a))
elif liczenie == 'h':
    r = float(input('r = '))
    print(calculatorhomework.obw_koła(r))
elif liczenie == 'i':
    a = float(input('a = '))
    h = float(input('h = '))
    print(calculatorhomework.p_równoległoboku(a,h))
elif liczenie == 'j':
    r = float(input('r = '))
    h = float(input('h = '))
    print(calculatorhomework.p_stożka(r,h))
elif liczenie == 'k':
    r = float(input('r = '))
    s = float(input('s = '))
    print(calculatorhomework.v_stożka(r,s))
elif liczenie == 'l':
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    print(calculatorhomework.obw_trójkąta(a,b,c))
elif liczenie == 'm':
    r = float(input('r = '))
    h = float(input('h = '))
    print(calculatorhomework.p_walca(r,h))
elif liczenie == 'n':
    r = float(input('r = '))
    h = float(input('h = '))
    print(calculatorhomework.v_walca(r,h))
elif liczenie == 'o':
    a = float(input('a = '))
    b = float(input('b = '))
    print(calculatorhomework.obw_prostokąta(a,b))
elif liczenie == 'p':
    r = float(input('r = '))
    a = float(input('a = '))
    print(calculatorhomework.suma_v_kuli_z_v_kostki())
elif liczenie == 'q':
    a = float(input('a = '))
    r = float(input('r = '))
    h = float(input('h = '))
    print(calculatorhomework.różnica_p_kostki_z_p_stożka(a,r,h))
elif liczenie == 'r':
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    r = float(input('r = '))
    print(calculatorhomework.różnica_obw_koła_z_obw_trójkąta(a,b,c,r))
elif liczenie == 'koniec':
    exit()
else:
    print('nie można wykonać operacji')

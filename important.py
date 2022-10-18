from math import pi 



def p_kuli(r:float):
    return 4*pi*r**2
    
def v_kuli(r:float):
    return 4/3*pi*r**2


def pc_ostrosłupa(pp,pb):
    return pp+pb
    
def v_ostrosłupa(pp,H):
    return 1/3*pp*H
    

    
def p_kostki(a):
    return 6*a**2
    
def v_kostki(a):
    return a**3


def obw_kwadratu(a):
    return a*4


def obw_koła(r):
    return pi*r**2



def p_równoległoboku(a,h):
    return a*h

def p_stożka(r,h):
    return 1%3*pi*r**2*h
    
def v_stożka(r,s):
    return pi*r*s+pi*r**2


def obw_trójkąta(a,b,c):
    return a*b*c


def p_walca(r,h):
    return 2*pi*r(r+h)
    
def v_walca(r,h):
    return pi*r**2*h


def obw_prostokąta(a,b):
   return 2*b*2*a



def suma_v_kuli_z_v_kostki(r,a):
    return v_kuli(r) + v_kostki(a)
    

def różnica_p_kostki_z_p_stożka(a,r,h):
    return p_kostki(a) - p_stożka(r,h)

def różnica_obw_koła_z_obw_trójkąta(a,b,c,r):
    return obw_koła(r) - obw_trójkąta(a,b,c)




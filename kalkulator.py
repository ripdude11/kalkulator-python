#!/usr/bin/env python3

def dodaj(a, b): return a+b
def odejmij(a, b): return a-b
def pomnoz(a, b): return a*b
def podziel(a, b):
	if b == 0: return "Syntax error"
	return a/b

a=float(input("Pierwsza liczba: "))
op=input("Operacja (+-*/): ")
b=float(input("Druga liczba: "))

if op == "+": print(dodaj(a, b))
elif op == "-": print(odejmij(a, b))
elif op == "*": print(pomnoz(a, b))
elif op == "/": print(podziel(a, b))

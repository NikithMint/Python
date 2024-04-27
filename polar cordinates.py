from cmath import phase
a=complex(input())
print(abs(complex(a.real,a.imag)))
print(phase(complex(a.real,a.imag)))
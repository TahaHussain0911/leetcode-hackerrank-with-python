import cmath

z=complex(input())

def polar_coordinates(z):
    r=abs(z)
    theta=cmath.phase(z)
    print(r)
    print(theta)

polar_coordinates(z)
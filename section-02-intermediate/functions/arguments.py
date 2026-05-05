"""  
Args named and args not named in python functions
Args named have name with signal of equal
Args not named receive only the args (value) 
"""

def soma(x: float, y: float, z: float) -> None:
    # Definition
    print(f'{x=} + y={y} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3) # Arg not named
soma(1, y=2, z=5) # Arg named

print(1, 2, 3, sep='-')
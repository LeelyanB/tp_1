
b=int(input("choisir un nombre: " ))
p=int(input("choisir un nombre: " ))

prod=0
while b!=0:
    if b%2==1:
        prod+=p
    b//=2
    p+=p
print(prod)

    
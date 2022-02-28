l = str(input("nombre"))


l = l.split(" ")
list(l)
b = [ int(i) for i in l]
print(b)
y = lambda d : d%2
Even = [ int(i) for i  in b if y(int(i)) == 0]
print(Even)


app = open("in.txt", "r")
info = app.read()

out = open("out.txt", "w")
out.write("200")
out.close()

ex = []
a  = []
b  = []
c  = []

for i in info: 
    if i != " ":      
        a.append(i)            
    if i == " ":
        break

for i in info: 
    ex.append(i)

for i in range(len(a)):         
    ex.remove(a[i])  

ex.remove(" ") 

for i in ex: 
    if i != " ":      
        b.append(i)
    else:
        break 

for i in range(len(b)):         
    ex.remove(b[i])

ex.remove(" ") 
c = ex 

a = "".join(a)            
b = "".join(b)                  
c = "".join(c)  

a = int(a)
b = int(b)
c = int(c)

data = [a, b, c]

r    = (a + b + c) / 3

print(a)
print(b)
print(c)
print(data)

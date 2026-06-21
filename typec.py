#int to str float complex
a=12
b=str(a)
print(b)
print(type(b))
a=12
b=float(b)
print(b)
print(type(b))
a=12
b=complex(a)
print(b)
print(type(b))
#str to int float complex
a="10"
b=int(a)
print(b)
print(type(b))
a="10.0"
b=float(b)
print(b)
print(type(b))
a="10+3j"
b=complex(a)
print(b)
print(type(b))
# float to complex int str
a=2.0
b=int(a)
print(b)
print(type(b))
a=2.0
b=str(a)
print(b)
print(type(b))
a=2.0
b=complex(a)
print(b)
print(type(b))
#complex to str int float
a=2+3j
b=int(a)
print(b)
print(type(b))
a=2+3j
b=str(a)
print(b)
print(type(b))
a=2+3j
b=float(a)
print(b)
print(type(b))
#Traceback (most recent call last):
# File "c:\Users\chint\OneDrive\Desktop\96r\typec.py", line 42, in <module>
#   b=int(a)
#ypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

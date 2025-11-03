from ctypes import c_int,addressof
a=5
b=2
b<<=a
print(b)

x=24
y=20
l=[10,20,30,40,50]
# if x not in l:
#     print(x," not present")
# else:
#     print(x," is present")
# if y in l:
#     print(y," is present")
# else:
#     print(y,"not present")

# m=x if x<y else y
# print(m)

# print(addressof(c_int(x)))
# print(hex(id(x)))

d={1,2,3}
d1={
    1:"Indra",
    2:"Suresh",
    3:"Subham"
}
print(type(d))
d1[4]="sourav"
print(d1)
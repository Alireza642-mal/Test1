a=int(input("a ra vared konid:"))
b=int(input("b ra vared konid:"))

op=input("Enter op(+ ,- , * , /):")

if op=="+":
    r=a+b
if op=="-":
    r=a-b
if op=="*":
    r=a*b
if op=="/":
    if b==0:
        b=int(input("b ra vared konid:"))
    r=a/b
print(r)



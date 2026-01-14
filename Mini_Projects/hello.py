print("HELLO WORLD!")
def is_even(a):
    if a%2==0:
        return True
    else:
        return False
name="Haseeb"
age=25
person ={
    "name":"HASEEB"
}
print(name)
print(is_even(4))
skill=["python","automation","git"]
for i in range(0,len(skill)):
    print("skill:",skill[i])
if age >=18:
    print("adult")
else:
    print("young")
def test(uname,age):
    print(uname)
    if age >=18:
        print("Major")
    else:
        print("Minor")
        
name=input("Enter Name")
age=int(input("Enter age"))

test(name,age)


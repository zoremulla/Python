skills=["Python","HTML","Leadership","C++"]
cv={}
cv["name"]=input("Please write you're name: ")
cv["age"]=int(input("Please write you're age: "))
cv["exp"]=int(input("Please write how many years of experience you have: "))
cv["Skills"]=[]
print("1.%s"%skills[0])
print("2.%s"%skills[1])
print("3.%s"%skills[2])
print("4.%s"%skills[3])
skillchoice=int(input("please choose a skill from the list: "))
cv["Skills"].append(skills[int(skillchoice)-1])
skillchoice2=int(input("Please choose another: "))
cv["Skills"].append(skills[int(skillchoice2)-1])
if cv["age"] <=28 and cv["age"] >=21 and cv["Skills"][0] == skills[0] or cv["Skills"][1] == skills[0]:
    print("You are accepted")
else:
    print("Sorry, you are not accepted")
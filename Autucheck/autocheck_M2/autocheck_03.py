work_experience = int(input("Enter your full work experience in years: "))

if 1 < work_experience <= 5:
    developer_type = "Middle"

elif work_experience <= 1:
    developer_type = "Junior"

elif 5 < work_experience <= 10:
    developer_type = "Senior"

else:
    developer_type = "Monster"


print(developer_type)

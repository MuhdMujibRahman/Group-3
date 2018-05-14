#file = open('data.txt','r')
#print(file.read())
file = open('data.txt','a')
print("Enter the data accordingly\n")
name=input('Name: ')
address=input('Address: ')
email=input('Email: ')
dateOfBirth=input('Date of birth: ')
sal=input('Salary: ')

dict = "Name,",name,",Address,",address,",Email,",email,",D.O.B,",dateOfBirth,",Salary,",sal
#dict={'Name': name, 'Address': address, 'Email': email, 'D.O.B.': dateOfBirth, 'Salary': sal}
print(dict)
file.write('\n')
file.write(str(dict))


file.close()

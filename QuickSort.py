def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

#===================================================MAIN PROGRAM=========================================
file = open('data.txt')
file2 = open('newSortedData.txt', 'a')
lines = file.read().splitlines()

name = []
address = []
email = []
dob = []
salary = []

j = 0
for line in lines:
    name.append('')
    address.append('')
    email.append('')
    dob.append('')
    salary.append('')
    j+=1

i = 0
for line in lines:
    name[i] = line.split(',')[0]
    address[i] = line.split(',')[1]
    email[i] = line.split(',')[2]
    dob[i] = line.split(',')[3]
    salary[i] = line.split(',')[4]
    i+=1

n = i
newArray = []
print("How do you want to sort the data?. Based on:")
print("1: Name \n2: City \n3: Date of Birth \n4: Salary\n")
choice = int(input("Your choice: "))

print("Unsorted:", name, address, email, dob, salary)

if choice == 1:
    newArray = name
    quickSort(newArray, 0, n-1)
    file2.write("THIS IS THE SORTED DATA BASED ON NAME\n")
    for line in lines:
        for k in range(n):
            if line.split(',')[0] == newArray[k]:
                name[k] = line.split(',')[0]
                address[k] = line.split(',')[1]
                email[k] = line.split(',')[2]
                dob[k] = line.split(',')[3]
                salary[k] = line.split(',')[4]
    for l in range(n):
        file2.write(name[l] + "," + address[l] + "," + email[l] + "," + dob[l] + "," + salary[l] + "\n")

elif choice == 2:
    newArray = address
    file2.write("THIS IS THE SORTED DATA BASED ON CITY IN ADDRESS\n")
    quickSort(newArray, 0, n-1)
    for line in lines:
        for k in range(n):
            if line.split(',')[1] == newArray[k]:
                name[k] = line.split(',')[0]
                address[k] = line.split(',')[1]
                email[k] = line.split(',')[2]
                dob[k] = line.split(',')[3]
                salary[k] = line.split(',')[4]
    for l in range(n):
        file2.write(name[l] + "," + address[l] + "," + email[l] + "," + dob[l] + "," + salary[l] + "\n")
elif choice == 3:
    newArray = dob
    file2.write("THIS IS THE SORTED DATA BASED ON DATE OF BIRTH\n")
    quickSort(newArray, 0, n-1)
    for line in lines:
        for k in range(n):
            if line.split(',')[3] == newArray[k]:
                name[k] = line.split(',')[0]
                address[k] = line.split(',')[1]
                email[k] = line.split(',')[2]
                dob[k] = line.split(',')[3]
                salary[k] = line.split(',')[4]
    for l in range(n):
        file2.write(name[l] + "," + address[l] + "," + email[l] + "," + dob[l] + "," + salary[l] + "\n")
elif choice == 4:
    newArray = salary
    file2.write("THIS IS THE SORTED DATA BASED ON CITY IN SALARY\n")
    quickSort(newArray, 0, n-1)
    for line in lines:
        for k in range(n):
            if line.split(',')[4] == newArray[k]:
                name[k] = line.split(',')[0]
                address[k] = line.split(',')[1]
                email[k] = line.split(',')[2]
                dob[k] = line.split(',')[3]
                salary[k] = line.split(',')[4]
    for l in range(n):
        file2.write(name[l] + "," + address[l] + "," + email[l] + "," + dob[l] + "," + salary[l] + "\n")

print("Sorted: ", name, address, email, dob, salary)

print("\nDo you want to clear the text file? -> 1: YES    2: NO")
clearFile = int(input("Your choice: "))
if clearFile == 1:
    open('newSortedData.txt', 'w').close()

file2.write('\n')
file.close()
file2.close()

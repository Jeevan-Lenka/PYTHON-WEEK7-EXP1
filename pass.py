def display_numbers(numbers):
    print(numbers)
    for i in numbers :
        print(i)
lst=list(map(int,input("enter numbers:").split()))
display_numbers(lst)

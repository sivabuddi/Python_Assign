def num2word(number):

  num=int(number)

  for i in number:

    if i=='1':
        print("one",end=" ")
    elif i=='2':
        print("two",end=" ")
    elif i=='3':
        print("three",end=" ")
    elif i=='4':
        print("four",end=" ")
    else:
        print("five",end=" ")

  num=num/10

num2word('12345')

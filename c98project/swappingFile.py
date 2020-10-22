def swapfiledata():
    fileName =  input("Enter the file name:- ")

    data_a = "This is file 1."
    data_b = "This is file 2."

    file1 =  open("sample1.txt", 'w')
    file1.write(data_b)
    file1.close()

    file2 = open("sample2.txt", 'w')
    file2.write(data_a)
    file2.close()


swapfiledata()

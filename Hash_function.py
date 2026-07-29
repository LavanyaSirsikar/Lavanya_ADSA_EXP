while(True):
    def Hashidx(sum,table):
        Hash_index = sum % table
        print("Hash index is :",Hash_index)

    key1=input("Enetr your name:")
    table1=int(input("Enetr table size:"))
    sum=0
    for i in key1:
        ascii_value = ord(i)
        sum = sum+ascii_value
    print(sum)
    Hashidx(sum,table1)


    key=int(input("Enetr your roll no:"))
    table=int(input("Enetr table size:"))

    Hashidx(key,table)
    a=input("Do you want to continue(y/n):")
    if a=='n' or a=='N':
        break    

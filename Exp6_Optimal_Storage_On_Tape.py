def optimal_storage_tape():
   
    n = int(input("Enter the number of files (n): "))

    
    length = []
    print(f"Enter the lengths of {n} files:")
    for _ in range(n):
        length.append(int(input()))
    length.sort()

    total = 0
    retrieval = 0

    for i in range(n):
        retrieval += length[i]
        total += retrieval

    average = total / n if n > 0 else 0

    print("Optimal order:", length)
    print("Total Retrieval Time:", total)
    print("Average Retrieval Time:", average)

optimal_storage_tape()

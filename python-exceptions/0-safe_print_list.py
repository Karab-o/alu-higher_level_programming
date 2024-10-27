def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass  # If x exceeds the list length, we simply stop printing.
    
    print()  # Move to the next line after printing.
    return count


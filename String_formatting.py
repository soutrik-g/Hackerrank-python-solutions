def print_formatted(number):
    space_length = len(bin(number))-1
    for i in range(1,number+1):
        print(f"{i:>{space_length-1}}{oct(i)[2:]:>{space_length}}{hex(i).upper()[2:]:>{space_length}}{bin(i)[2:]:>{space_length}}")

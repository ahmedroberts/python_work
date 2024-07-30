hat_file = open(input())

for line in hat_file:
    # Each line read from the file ends with a newline.
    print(line, end="")  # end="" prints each line without adding another newline.
print()

hat_file.close()
version_one = "bottles "
version_two = "bottles "
wall_line = "of beer on the wall\n"
second_line = "of beer\nTake one down, pass it around\n"
for number_of_bottles in range(99, 0, -1):
    if number_of_bottles == 2:
        version_two = "bottle "
    if number_of_bottles == 1:
        version_one = "bottle "
    print(str(number_of_bottles), ' ' + version_one + wall_line,
          str(number_of_bottles), ' ' + version_one + second_line,
          str(number_of_bottles - 1), ' ' + version_two + wall_line, sep='')

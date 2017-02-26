def remove_repetitive_get_largest(number):
    number = str(number)
    curMax = -1
    for i in range(1, len(number)):
        if number[i] == number[i - 1]:
            removed_ith = int(number[:i] + number[i + 1:])
            # if the current removed digit is less
            # than the digit to right, simply return with ith digit removed,
            # it's already the max
            if i + 1 < len(number) and number[i] < number[i + 1]:
                return removed_ith
            else:
                curMax = max(removed_ith, curMax)
    return curMax


print remove_repetitive_get_largest(11233445)
# prints 1233445
print remove_repetitive_get_largest(133233445)


# prints 13323445


def get_files(str_rep):
    file_structure = []
    res = []
    for line in str_rep.strip().split("\n"):
        lvl = 0
        while line[lvl] == " ":
            lvl += 1
        if lvl == len(file_structure):
            file_structure.append(line.lstrip(" "))
        else:
            file_structure[lvl] = line.lstrip(" ")
        res.append("/".join(file_structure[:lvl + 1]))
    return res


str_rep = \
    """
dir
dir1
 dir11
  dir111
dir12
 file.jpg
dir2
 dir21
 file2.jpg
dir3"""
# str_rep is now 
# 'dir dir1  dir11   dir111 dir12   file.jpg dir2  file2.jpg dir3'
print get_files(str_rep)
# prints ['dir/dir12/file.jpg', 'dir/dir2/file2.jpg']

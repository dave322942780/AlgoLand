def remove_repetitive_get_largest(number):
    number = str(number)
    i = len(number) - 2
    curMax = -1
    while (i >= 0):
        if number[i + 1] == number[i]:
            removed_ith = int(number[:i] + number[i + 1:])
            # if the current removed element is less
            # than the digit to right, simply return, it's already the max
            if i - 1 >= 0 and number[i] < number[i - 1]:
                return removed_ith
            else:
                curMax = max(removed_ith, curMax)
        i-=1
    return curMax

print remove_repetitive_get_largest(11233445)
# prints 1233445
print remove_repetitive_get_largest(133233445)
# prints 13323445

import re
def get_files(str_rep, extension):
    prev_level = -1
    cur_path = []
    res = []
    for line in re.findall(" *[^ ]+", str_rep):
        cur_level = len(re.search("^ *", line).group())
        # stepped in one level
        if prev_level == cur_level - 1:
            cur_path.append(line[cur_level:])
        # stepped out cur directory
        else:
            cur_path = cur_path[:cur_level + 1]
        
        if cur_path[-1].endswith(extension):
            res.append("/".join(cur_path))
            
        prev_level = cur_level
    return res


str_rep = \
'''dir
 dir1
  dir11
   dir111
 dir12
  file.jpg
 dir2
  file2.jpg
 dir3'''
str_rep = str_rep.replace("\n", "")
# str_rep is now 
# 'dir dir1  dir11   dir111 dir12   file.jpg dir2  file2.jpg dir3'
print get_files(str_rep, ".jpg")
# prints ['dir/dir1/file.jpg', 'dir/dir1/file2.jpg']

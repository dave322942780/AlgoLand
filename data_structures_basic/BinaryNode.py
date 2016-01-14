class BinaryNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def parse_tree(root_str_format, data_type=str):
        def _parse_tree(str_format):

            def get_top_lvl(idx):
                lvl = 0
                for i in range(idx, len(str_format)):
                    if str_format[i] == "[":
                        lvl += 1
                    elif str_format[i] == "]":
                        lvl -= 1
                    if lvl == 0:
                        return i + 1
                return None

            left_end = get_top_lvl(1) if str_format[1] == "[" else None
            left = None if left_end is None else _parse_tree(str_format[1:left_end])

            value_start_idx = 1 if left_end is None else left_end
            value_end_idx = -1
            for i in range(value_start_idx, len(str_format)):
                if str_format[i] in "[]":
                    value_end_idx = i
                    break
            value = data_type(str_format[value_start_idx: value_end_idx])
            right_end = get_top_lvl(value_end_idx) if str_format[value_end_idx] == "[" else None
            right = None if right_end is None else _parse_tree(str_format[value_end_idx:right_end])

            return BinaryNode(value, left, right)

        return _parse_tree(root_str_format)

    def create_deep_copy(self):
        left = self.left.create_deep_copy() if self.left else None
        right = self.right.create_deep_copy() if self.right else None
        return BinaryNode(self.value, left, right)

    def __str__(self):
        res = str(self.value) + "\n"
        if self.left or self.right:
            res += "\t(left)" + self.left.__str__().strip("\n").replace("\n", "\n\t") + "\n"
            res += "\t(right)" + self.right.__str__().strip("\n").replace("\n", "\n\t")
        return res

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return self.value == other.value and self.left == other.left and self.right == other.right

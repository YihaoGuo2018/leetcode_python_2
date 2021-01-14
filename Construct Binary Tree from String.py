class Solution:
    def str2tree(self, s):
            # Find (, then find end of left tree. The right tree starts after that.
            begin_of_left = s.find("(")
            if begin_of_left < 0:
                # Either all num or none.
                return TreeNode(int(s)) if s else None
            # Now find the end of the left tree.
            paren_count = 0
            index = begin_of_left
            while index < len(s):
                if s[index] == "(":
                    paren_count +=1
                elif s[index] == ")":
                    paren_count -= 1
                if paren_count == 0:
                    break
                index += 1

            end_of_left = index
            left_indices = begin_of_left+1, end_of_left
            right_indices = end_of_left + 2, -1
            left_tree = self.str2tree(s[left_indices[0]: left_indices[1]])
            right_tree = self.str2tree(s[right_indices[0]: right_indices[1]])
            # Note that the left and right trees are without the () that wraps around them.
            root = TreeNode(int(s[:begin_of_left]))
            root.left = left_tree
            root.right = right_tree
            return root
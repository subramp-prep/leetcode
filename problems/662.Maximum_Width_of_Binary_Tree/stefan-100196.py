def widthOfBinaryTree(self, root):
    width = 0
    level = [(1, root)]
    while level:
        width = max(width, level[-1][0] - level[0][0] + 1)
        level = [kid
                 for number, node in level
                 for kid in enumerate((node.left, node.right), 2 * number)
                 if kid[1]]
    return width

# That's numbering nodes (and nulls) like this:

#                   1
#           2               3
#       4       5       6       7
#     8   9   ...

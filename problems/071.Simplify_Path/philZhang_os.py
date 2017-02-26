class Solution(object):

  def simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """
    import os
    return os.path.abspath(path)

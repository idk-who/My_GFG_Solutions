import numpy as np
class Solution:
    def transpose(self, mat):
        trans = np.array(mat)
        return np.transpose(mat).tolist()
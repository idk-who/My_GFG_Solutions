class Solution:
    def validgroup(self, arr, k):
        n = len(arr)
        
        if n % k:
            return False
        
        if k == 1:
            return True
        
        arr.sort()
        index = 0
        
        while index < n - 1:
            group_count = 1
            current_value = arr[index]
            
            while index < n - 1 and arr[index] == arr[index + 1]:
                group_count += 1
                index += 1
            index += 1
            
            remaining_in_group = k - 1
            
            if index + remaining_in_group * group_count > n:
                return False
            
            while remaining_in_group:
                if index < n and current_value + 1 != arr[index]:
                    return False
                
                next_count = 1
                while index < n - 1 and arr[index] == arr[index + 1]:
                    next_count += 1
                    index += 1
                
                if next_count != group_count:
                    return False
                
                index += 1
                remaining_in_group -= 1
                current_value += 1
            
        return True

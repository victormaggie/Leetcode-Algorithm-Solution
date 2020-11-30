class Solution:
    def circularArrayLoop(self, nums):
        for i in range(len(nums)):
            # move forward use the memorization
            is_forward = nums[i] >= 0
            slow, fast = i, i

            # if slow or fast becomes '-1 this means move backward
            # in this case, we can stop the calculation
            while True:
                slow = self.find_next_index(nums, is_forward, slow)
                fast = self.find_next_index(nums, is_forward, fast)

                # move forward another fast
                if (fast != -1):
                    fast = self.find_next_index(nums, is_forward, fast)
                # cannot find cycles
                if slow == -1 or fast == -1 or slow == fast:
                    break
            if slow != -1 and slow == fast:
                return True
        return False
    
    def find_next_index(self, arr, is_forward, current_index):
        direction = arr[current_index] >= 0

        if is_forward != direction:
            return -1
        
        next_index = (current_index + arr[current_index])  % len(arr)

        # one element cycle
        if next_index == current_index:
            next_index = -1
        return next_index

# time complexity o(N^2)
# space complexity o(N)


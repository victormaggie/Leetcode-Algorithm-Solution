class Solutions(object):
    def trap(self, height):
        if not height: return 0
        left = [0] * len(height)
        right = [0] * len(height)

        # initialization
        left[0] = height[0]
        right[-1] = height[-1]

        for i in range(1, len(height)):
            left[i] = max(left[i-1], right[i])
        for j in range(len(height)-2, -1, -1):
            right = max(right[i+1], height[i])
        
        sum_water = 0
        for i in range(len(height)):
            water_volume = min(left[i], right[i]) - height[i]
            sum_water += water_volume if water_volume > 0 else 0
        return sum_water
        
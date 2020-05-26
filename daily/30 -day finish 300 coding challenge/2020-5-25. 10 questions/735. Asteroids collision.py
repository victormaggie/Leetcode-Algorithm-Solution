class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        ans = []

        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                # the same value, collide together
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                # if len(ans) == 0 or both the same direction or ans[-1] < 0 < new
                ans.append(new)
        return ans
    

# very concise solution
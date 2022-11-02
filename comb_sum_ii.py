
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        candidates.sort()
        
        # candidates = [1,1,2,5,6,7,10], target = 8
        def run(i,temp,total):
            print(temp)
            print(total)
            if total == target:
                print("hellp")
                new_lst = temp[:]
                print(temp)
                if new_lst not in output:
                    output.append(new_lst)
                return
            if i >= len(candidates) or total > target:
                return
            
            
            temp.append(candidates[i])
            run(i+1,temp,total+candidates[i])
            temp.pop()
            
            while i < len(candidates)-1 and candidates[i+1] == candidates[i]:
                i = i+1
            run(i+1,temp,total)

            
            print(i)
            
            
            
                
        run(0,[],0)
        print(output)
        return output


candidates = [10,1,2,7,6,1,5]
   
target = 8
        
obj = Solution()

obj.combinationSum2(candidates,target)        
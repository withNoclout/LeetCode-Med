class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        
        def backtrack(index, path, current_val, prev_operand):
            # Base Case: If we've processed all digits
            if index == len(num):
                if current_val == target:
                    res.append(path)
                return

            for i in range(index, len(num)):
                # Extract the current substring as a multi-digit number
                curr_str = num[index : i + 1]
                
                # Constraint: Disallow leading zeros for multi-digit numbers
                if len(curr_str) > 1 and curr_str[0] == '0':
                    break
                
                curr_num = int(curr_str)

                # Special Case: The first number in the expression (no operator before it)
                if index == 0:
                    backtrack(i + 1, curr_str, curr_num, curr_num)
                else:
                    # Case 1: Addition (+)
                    backtrack(i + 1, path + "+" + curr_str, current_val + curr_num, curr_num)
                    
                    # Case 2: Subtraction (-)
                    backtrack(i + 1, path + "-" + curr_str, current_val - curr_num, -curr_num)
                    
                    # Case 3: Multiplication (*)
                    # To handle precedence: current_val - prev_operand + (prev_operand * curr_num)
                    backtrack(i + 1, path + "*" + curr_str, 
                              (current_val - prev_operand) + (prev_operand * curr_num), 
                              prev_operand * curr_num)

        backtrack(0, "", 0, 0)
        return res

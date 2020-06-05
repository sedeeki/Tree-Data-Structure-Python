
def construct_a_longest_palindrome(numbers_bank):
    queue = []
    stack = []
    dict = {}
    for i in numbers_bank:           # adds values to queue and duplicates to stack 
        if i in dict:
            dict[i] = dict[i] + 1
            if (dict[i]%2 == 0):
                stack.append(i)
            else:
                queue.append(i)
        else:
            queue.append(i)
            dict[i] = 1
            
            
    mid = None
    for i in range(len(queue)):       # gets any mid point which is not a duplicate
        temp = queue.pop(0)
        if (dict[temp]%2 == 1 and mid == None):
            mid = temp
            
    palindrome = []
    for i in range(len(stack)): # appends the duplicates into the palindrome list and queue
        temp = stack.pop()
        palindrome.append(temp)
        queue.append(temp)    
        
    palindrome.append(mid)   # appends mid point onto the palindrome
    
    for i in range(len(queue)):   # appends queue in stack again for reverse order
        stack.append(queue.pop(0))
        
    for i in range(len(stack)):   # appends palindrome with reverse order
        palindrome.append(stack.pop())
    
    return palindrome
    
bank = [3,47,6,6,5,6,15,3,22,1,6,15]
print(construct_a_longest_palindrome(bank))
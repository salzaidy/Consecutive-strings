'''
Created on Nov 27, 2020

@author: Salzaidy
'''

# Check if the array is empty, or if k is bigger the array's length, or k in less than 0
# append the joined string to new array
# return the longest string
def longest_consec(strarr, k):

    longestConsec = []

    if (len(strarr) == 0) or (k > len(strarr)) or (k <= 0):
        return ''
    else:
        for i in range(len(strarr)):
            longestConsec.append(''.join(strarr[i:i+k]))

    
    return max(longestConsec, key = len)
    
    
s = longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 1)
print(s)
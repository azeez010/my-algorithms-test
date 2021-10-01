# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    highest_count = 0
    if N >= 1 and N <= 2147483647:
        counter = 0
        
        binary = str(bin(N)).replace("0b", "")
        for char in binary:
            if char == "0":
                counter += 1
            else:
                if highest_count < counter:
                    highest_count = counter
                
                counter = 0
        
    return highest_count
    # write your code in Python 3.6
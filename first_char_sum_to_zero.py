#TASK 1
#Complete function solution, that should return a string describing first character of the given string:
#'digit' for a digit, 'lower' for a lowercase letter, 'upper' for an uppercase letter and 
#'other' for other characters.

def solution (s):
  c = s[0]
  if c.isupper():
    return print ('upper')
  elif c.islower():
    return print ('lower')
  elif type(int(c)) ==int:
    return print ('digit')
  else:
    return print('other')


#TASK 2
#Find the bug(s) and modify one line of code in the incorrect implementation of a function solution
#that is supposed to return the smallest element of the given non-empty array A which contains at most 1000
#integers within range [-1000...1000]

def solution(A):
  ans = 0
  for i in range (1, len(A)):
    if A[i] <ans:
      ans = A[i]
  return print (ans)


#TASK 3
#Write a function solution that returns an arbitrry integer which is greater than N, not greater than 10**9, and ends with 0. 
#Assume that N is between 1 and 999,999,999

def solution(N):
  for x in range (N, 999999999):
    if str(x).endswith('0') and x > N:
      return print(x)

#TASK 4
#Write a function def solution (N) that given an integer N(1<=N<=100), 
#returns an array containing N unique integers that sum up to 0. The function can return any such array.

def solution(N): 
    for i in range(1, N // 2 + 1): 
          
        # Print 2 symmetric numbers 
        print(i, end = ', ') 
        print(-i, end = ', ') 
          
    # Print a extra 0 if N is odd 
    if N % 2 == 1: 
        print(0, end = '') 
      
N = 11
solution(N) 

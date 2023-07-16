# Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
# function.
# ['python', 'php', 'aba', 'radar', 'level']


l=['python', 'php', 'aba', 'radar', 'level']

ans=list(filter(lambda x:x==x[::-1],l))

print(ans)
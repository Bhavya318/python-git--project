def is palindrome(s):
return s==s[::-1]
s="telugu"
ans=ispalindrome(s)
if ans:
       print ("yes")
else:
       print("no")
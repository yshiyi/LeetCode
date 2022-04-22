"""
Your input will be an ASCII string, and you will output a boolean, which indicates whether the string is valid xml.
We simplify the xml format to only have content or tags.
Content
Text which can contain any ascii characters EXCEPT < and >
Tags
Tags come in two flavors. < and > must only appear as the start and end of a tag, and the tags cannot be empty. 
I.e <> and </> are invalid.
The start-tag and end-tag elements must be correctly nested, with none missing and none overlapping. 
For example, text <a> text</a>, <a>text<b>other text</b></a> are valid, <a>text<b>other text</a></b> is not.
The goal of this question is to simulate an xml validator. 
We will give you sample xml text and you should output wheter the text is valid xml or not.
###Example input/output
Input
	text
Output
	true
Input
	text<a>more text</a>
Output
	true
Input
	text</a>
Output
	false
Input
	<invalid<>text</invalid>
Output
	false
12 test cases total, 3 showed and 9 hidden.
"""

import collections
class Solution(object):
    def validXML(self, text):
        stack = collections.deque()
        i = 0
        while i<len(text):
            if text[i]=="<":
                valid, tag = self.helper(text[i:])
                if not valid:
                    return False
		#tags cannot be empty
                if tag=="" or tag=="/":
                    return False
		#If we find a closing tag </abc>
                if tag[0]=="/":
		    #if stack is empty, that means there was no opening tag, return false
                    if len(stack)==0:
                        return False
		    #if stack top is 'abc' but our closing tag is 'xyz', return False
                    if stack[-1]!=tag[1:]:
                        return False
		    #if there is a match to our closing tag then pop it from stack
                    stack.pop()
                else:
		     #if this is the opening tag then add it to stack
                    stack.append(tag)
		#we increment i to tag length plus 2 to add <> to the legth of i
                i += len(tag)+2
            elif text[i]==">":
		#if there is a random > in text then return false
                return False
            else:
                i += 1
        if len(stack):
	    #if we never found a closing tag to one of our opening tags
            return False
        return True
    
    def helper(self, text):
        tag = ""
        for i in range(1, len(text)):
            if text[i]=="<":
                #text = <<abc>
                return False, -1
            if text[i]==">":
		#Completes the tag <abc>
                return True, tag
            tag += text[i]
        return True, tag


sol = Solution()
text = "<a>text<b>other text</b></b>"
print(sol.validXML(text))


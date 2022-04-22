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

#  Install an external module and use it to perform an operation of your interest. 

import wikipedia

result = wikipedia.page("GeeksforGeeks (website)")
print(result.summary)

#  Install an external module and use it to perform an operation of your interest. 
# first install package of wikipedia
# pip install wikipedia

import wikipedia

result = wikipedia.page("GeeksforGeeks (website)")
print(result.summary)

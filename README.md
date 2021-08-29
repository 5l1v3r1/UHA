# UHA

UHA (Unusable Hashing Algorythm), is a very slow hashing algorythm made over a weekend.
The algorythm takes 11s to hash a 76KB EXE file.

## How Does It Work?
The input gets converted to an array: `'hello' > ['h','e','l','l','o']`
For every element in the array above 
`for i in range(len(array)):` we grab the next 32 symbols 
after the one specified so ['h'] would be 
['ijklmnopqrs ...'] this turns the specified charachter into a 32 byte long string.
After all the charachters have been converted to strings we have someting that looks like this 
['32 chars','32 chars','32 chars']
as all of this is done in hex we get the first hex value 
from the string 1010202130213011404130 > 10
and then we get first value of the second string  
9070890901203210990289328932094 > 90 then we add the 2 values so `90 + 10 = 100`
if the value is greater than 100 we take away 100 so in this instance 
we will do `100 - 100` and we will get `00` then we append it to a
spare string `string += 00` then we repeat it for all the 32 symbols 
so 2 32 byte strings gets turned into 1. We repeat this entire sequence until 
all of the 32 byte values have been turned into 1, then that is returned as our hash.


								['h','e','y']
								      |
							['32 chars','32 chars','32 chars']
								   |
							    ['32 chars','32 chars']
								      |
								 ['32 chars']
                 
## How to use it
1. download the .py file and put into the same directory as your source code
2. import it `import uha`
3. call the function `uha.uHash(string)`

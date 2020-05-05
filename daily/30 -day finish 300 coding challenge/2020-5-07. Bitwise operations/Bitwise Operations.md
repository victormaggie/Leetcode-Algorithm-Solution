# Bitwise operation for the calcualtion

## the general bitwise operators 

* --> logical operators

* & Binary AND 

* x << y returns x left shift by y places 

    In this case, we can simply say that this is (x * 2^y) 

* x >> y returns x right shift by y places

    In this case, this is that (x / 2 ^ y)

* x & y 'Bitwise and' each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise 0


```
    1 & 1 = 1
    1 & 0 = 0
    0 & 0 = 0
```

* x | y 'Bitwise or' OR
* ~ x returns the compliment of x --> NOT !! 
* x ^ y "bitwise exclusive or" --> bit same then 0, bit compliment then 1


## Properties
1. `a ^ b ^ a = b` , this can be used to find single value  `XOR` detect 1, 3, 5 ... single numbers
2. `a ^ a = 0`, cancal out the duplicated one
3. `bin()`,  `chr()` return the return a character whose Unicode code point, `int(, 2)` change the binary bits into number,  `ord()` return integer of the number

## Two-complement Binary
* Given 8 bits, if it is unsigned, it can be represent the value 0 to 255. 
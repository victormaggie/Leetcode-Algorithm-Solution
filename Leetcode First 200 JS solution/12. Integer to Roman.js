var intToRoman = function(num) {
    let hashmap = {
        '1000': 'M',
        '900': 'CM',
        '500': 'D',
        '400': 'CD',
        '100': 'C',
        '90' : 'XC',
        '50' : 'L',
        '40' : 'XL',
        '10' : 'X',
        '9'  : 'IX',
        '5'  : 'V',
        '4'  : 'IV',
        '1' : 'I'  
    }
    
    let res = '';
    
    array = Object.keys(hashmap).reverse()

    for (let key of array) {
        
        let value = hashmap[key];
        res += value.repeat(Math.floor(num / key));
        num %= key;
    }
    return res;
    
};

// solution 1


var intToRoman = function(x) {
    const values = [
        1000,
        900, 500, 400, 100,
        90, 50, 40, 10,
        9, 5, 4, 1
    ]

    const strs = [
        'M',
        'CM', 'D', 'CD', 'C',
        'XC', 'L', 'XL', 'X',
        'IX', 'V', 'IV', 'I'
    ]

    let res = "";
    for (let i = 0; i < 13; i++) {
        while (x >= values[i]) {
            res += str[i];
            x -= values[i];
        }
    }
    return res;
};

// the value here


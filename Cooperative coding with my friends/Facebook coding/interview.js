function foo(input) {
    // implement the logic below
    var newString = "";
    for (var i = input.length-1; i >= 0; i--){
        newString += input[i];
    }
    return newString;
  }
  
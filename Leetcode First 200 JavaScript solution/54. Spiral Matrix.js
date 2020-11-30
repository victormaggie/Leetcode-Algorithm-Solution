var spiralOrder = function(matrix) {
    
    if (matrix.length == 0 || matrix[0].length == 0) return []
    let left = 0, upper = 0, right = matrix[0].length-1, down = matrix.length-1;
    
    let res = [];
    
    let direction = 0
    
    while (left <= right && upper <= down) {
        if (direction == 0) {
            for (let i = left; i <= right; i++) res.push(matrix[upper][i]);
            upper++;  
            direction = 1
        }

        else if (direction == 1) {
            for (let i = upper; i <= down; i++) res.push(matrix[i][right]);
            right--;   
            direction = 2
        }
        
        else if (direction == 2) {
            for (let i = right; i >= left; i--) res.push(matrix[down][i]);
            down--;   
            direction = 3
        }
        
        else if (direction == 3) {
            for (let i = down; i >= upper; i--) res.push(matrix[i][left]);
            left++;  
            direction = 0
        }
    }
    
    return res;
    
};

// spiral matrix 
// be aware that this is n x m matrix here!
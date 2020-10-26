var isValidSudoku = function(board) {


    for (let j = 0; j < 9; j++){
        let col = new Set();
        for (let i = 0; i < 9; i++) {
            const value = board[i][j];
            if (col.has(value)) {
                return false;   
            }
            if (value !== '.'){
                col.add(value);   
            }
        }         
    }
    
    for (let i = 0; i < 9; i++){
        let row = new Set();
        for (let j = 0; j < 9; j++) {
            const value = board[i][j];
            if (row.has(value)) {
                return false;   
            }
            if (value !== '.'){
                row.add(value);  
            }
        }         
    }
    
    for (let i = 0; i < 9; i += 3){
        for (let j = 0; j < 9; j += 3){
            let matrix = new Set();
            for (let m = i; m < i+3; m++){
                for (let n = j; n < j+3; n++){
                    const value = board[m][n];
                    if (matrix !== 'undefined' && matrix.has(value)) return false;
                    if (value !== '.') matrix.add(value);
                }
            }
        }
    }
    
    return true;
};

// valid sudoku


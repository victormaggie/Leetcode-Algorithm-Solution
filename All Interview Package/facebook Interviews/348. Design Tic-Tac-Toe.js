var TicTacToe = function(n){
    this.row = new Array(n).fill(0);
    this.col = new Array(n).fill(0);
    this.diagnoal = new Array(2).fill(0);
    this.size = n;
};


TicTacToe.prototype.move = function(row, col, player) {
    var update = player === 1 ? 1 : -1;
    this.row[row] += update;
    this.col[col] += update;
    if (row === col) this.diagnoal[0] += update;
    if (Math.abs(this.row[row]) === this.size || Math.abs(this.col[col]) === this.size || Math.abs(this.diagnoal[0]) === this.size || Math.abs(this.diagnoal[1]) === this.size) {
        return player;
    }
    return 0;
};

// time complexity o(n)
// space complexity o(n)




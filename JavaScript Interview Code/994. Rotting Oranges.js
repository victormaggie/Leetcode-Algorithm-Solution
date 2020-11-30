var orangesRotting = function(grid) {
    // first step find the rotten oranges

    if (grid == null || grid[0] == null) return 0;

    let rotten = [];
    const dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    const row = grid.length;
    const col = grid[0].length;
    let fresh = 0;

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (grid[i][j] != 0) fresh += 1;
            if (grid[i][j] === 2) {
                rotten.push([i, j]);
                grid[i][j] = '.';
            }
        }
    }
    if (numRotten == 0 && totalNum != 0) return -1;
    if (numRotten == 0) return 0;

    let time = 0
    while (rotten.length && fresh) {
        let max_len = rotten.length;
        time += 1;
        for (let i = 0; i < max_len; i++) {
            [y, x] = rotten.shift();
            grid[y][x] = '.';
            for (const [dy, dx] of dirs) {
                new_y = dy + y;
                new_x = dx + x;
                if (new_y >= 0 && new_y < row && new_x >= 0 && new_x < col && grid[new_y][new_x] == 1) {
                    grid[new_y][new_x] = '.';
                    rotten.push([new_y, new_x]);
                    fresh--;
                } 
            }
        }
    }
    return (fresh == 0) ? time: -1;
};

// time complexity o(N)
// space complexity o(n)



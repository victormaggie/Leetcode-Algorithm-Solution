var getPermutation = function(n, k) {
    
    let ans = []
    let path = '';
    visited = Array(n+1).fill(false)
    dfs(n, k, path, visited)
    return ans[k-1];
    
    function dfs(n, k, path) {
        
        if (path.length == n){
            ans.push(path);
            return
        }

        for (let i = 1; i < n+1; i++) {
            if (!visited[i]){
                path += i;
                visited[i] = true;
                dfs(n, k, path);
                path = path.slice(0, path.length-1)
                visited[i] = false;
            }
        }
    }
};

// Permutation with the all out put!

var getPermutation = function(n, k) {

    var res = "";

    var st = Array.from({length : n},()=>false);

    for(var i = 0 ; i < n ; i ++ )
    {
        var fac = 1;

        for(var j = 1 ; j < n - i ; j ++ ) fac *= j;

        for(var j = 0 ; j < n ; j ++ )
        {
            if(st[j]) continue;
            if(k <= fac)
            {
                res += j + 1;
                st[j] = true;
                break;
            }
            k -= fac;
        }
    }

    return res;
};


// next permutation


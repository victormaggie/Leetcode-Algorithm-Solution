
var depthSum = function(nestedList){
    if (nestedList === null || nestedList.length === 0) return 0;
    let sum = 0;
    function dfs(list, depth){
        for (let i = 0; i < list.length; i++){
            if (list[i].isInteger()){
                sum += list[i].getInteger() * depth;
            } else{
                dfs(list[i].getList(), depth+1);
            }
        }
    }
    dfs(nestedList, 1);
    return sum;
}

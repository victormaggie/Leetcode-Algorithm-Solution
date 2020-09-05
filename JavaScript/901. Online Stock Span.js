var StockSpanner = function() {
    this.stack = [];
};

StockSpanner.prototype.next = function(price) {

    let span = 1;
    while (this.stack.length > 0 && this.stack.slice(-1)[0][1]) {
        span += this.stack.slice(-1)[0][0];
        this.stack.pop();
    
    this.stack.push[[span, price]];
    return span;
    }
};


class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let stack = [];    
        for (let token of tokens) {
            if (token === '+') {
                stack.push(stack.pop() + stack.pop());
            } else if (token === '-') {
                let b = stack.pop(); // segundo valor
                let a = stack.pop(); // primeiro valor
                stack.push(a - b);
            } else if (token === '*') {
                stack.push(stack.pop() * stack.pop());
            } else if (token === '/') {
                let b = stack.pop();
                let a = stack.pop();
                // Math.trunc trunca em direção ao zero (ex: 1.8 vira 1, -1.8 vira -1)
                stack.push(Math.trunc(a / b));
            } else {
                stack.push(Number(token));
            }
        }
        return stack.pop();
    }
}

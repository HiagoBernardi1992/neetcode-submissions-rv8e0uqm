class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let hold = [];
        let response = 0;
        for(let i = 0; i < tokens.length; i++) {
            switch(tokens[i]) {
                case '+':
                    response = hold[0] + hold[1];
                    hold.pop();
                    hold.pop();
                    hold.push(response);
                    break;
                case '-':
                    response = hold[0] - hold[1];
                    hold.pop();
                    hold.pop();
                    hold.push(response);
                    break;
                case '*':
                    response = hold[0] * hold[1];
                    hold.pop();
                    hold.pop();
                    hold.push(response);
                    break;
                case '/':
                    response = hold[0] / hold[1];
                    hold.pop();
                    hold.pop();
                    hold.push(response);
                    break;
                default:
                    hold.push(Number(tokens[i]));
                    break;
            }
        }
        return response;
    }
}

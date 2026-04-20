class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let initialBrackets = [];
        for(let bracket of s) {
            if(bracket == '('
                || bracket == '{'
                || bracket == '[') initialBrackets.push(bracket);
            else {
                if((bracket == ')' && initialBrackets[initialBrackets.length - 1] != '(')
                    || (bracket == ']' && initialBrackets[initialBrackets.length - 1] != '[')
                    || (bracket == '}' && initialBrackets[initialBrackets.length - 1] != '{')) {
                        return false;
                    } else {
                        initialBrackets.pop();
                    }
            }
        }
        return initialBrackets.length == 0;
    }
}

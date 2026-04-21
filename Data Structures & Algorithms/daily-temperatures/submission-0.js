class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        const n = temperatures.length;
        const output = new Array(n).fill(0);
        const stackIndexes = []; 

        for (let i = 0; i < n; i++) {
            const currentTemp = temperatures[i];
            
            while (stackIndexes.length > 0 
                    && temperatures[stackIndexes[stackIndexes.length - 1]] < currentTemp) {
                const prevIndex = stackIndexes.pop(); 
                output[prevIndex] = i - prevIndex; 
            }

            stackIndexes.push(i);
        }

        return output;
    }
}

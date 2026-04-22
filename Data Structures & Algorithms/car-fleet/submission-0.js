class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        let cars = position.map((p, i) => [p, speed[i]]);
        cars.sort((a, b) => b[0] - a[0]);

        let stack = [];

        for (let [pos, vel] of cars) {
            let timeToTarget = (target - pos) / vel;
            if(stack.length == 0 || timeToTarget > stack[stack.length - 1]) stack.push(timeToTarget);
            
        }
        return stack.length;
    }
}

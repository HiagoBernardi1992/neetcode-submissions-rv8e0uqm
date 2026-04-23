class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let start = 1;
        let end = Math.max(...piles);
        let res = end;
        while(start <= end) {
            let k = Math.floor(start + (end - start) / 2);
            let hoursSpent = 0;

            for (let pile of piles) {
                hoursSpent += Math.ceil(pile / k);
            }

            if (hoursSpent <= h) {
                res = k;
                end = k - 1;
            } else {
                start = k + 1;
            }
        }

        return res;
    }
}

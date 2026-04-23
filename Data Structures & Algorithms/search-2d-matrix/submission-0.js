class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        let startMatrix = 0;
        let endMatrix = matrix.length - 1;

        while (startMatrix <= endMatrix) {
            let middleMatrix = this.calcMiddle(startMatrix, endMatrix);
            let row = matrix[middleMatrix];
            let lastIndexLine = row.length - 1;

            if (target >= row[0] && target <= row[lastIndexLine]) {                
                let startLine = 0;
                let endLine = lastIndexLine;
                while (startLine <= endLine) {
                    let middleLine = this.calcMiddle(startLine, endLine);
                    if (row[middleLine] === target) return true;

                    if (row[middleLine] < target) startLine = middleLine + 1;
                    else endLine = middleLine - 1;
                }
                return false; 
            }

            if (target > row[lastIndexLine]) startMatrix = middleMatrix + 1;
            else endMatrix = middleMatrix - 1;
        }
        return false;
    }

    calcMiddle(start, end) {
        return Math.floor(start + (end - start) / 2);
    }
}

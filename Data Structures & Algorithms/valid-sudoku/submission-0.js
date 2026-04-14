class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) { 
        let lines = Array.from({ length: 9 }, () => new Set());       
        let columns = Array.from({ length : 9} , () => new Set());
        let blocks = Array.from({ length: 9 }, () => new Set());

        for(let r = 0; r < 9; r++) {
            for(let c = 0; c < 9; c++) {
                const value = board[r][c];

                if(value === '.') continue;

                const boxIndex = Math.floor(r / 3) * 3 + Math.floor(c / 3);

                if(lines[r].has(value) 
                    || columns[c].has(value)
                    || blocks[boxIndex].has(value)) return false;
                    
                lines[r].add(value);
                columns[c].add(value);
                blocks[boxIndex].add(value);
            }
        }
        
        return true;
    }
}

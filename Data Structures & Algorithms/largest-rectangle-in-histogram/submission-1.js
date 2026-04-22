class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    largestRectangleArea(heights) {
        let maxArea = 0;
        let stack = []; // Guardará os índices
        // Adicionamos um 0 no final para limpar a pilha no fim do loop
        heights.push(0); 

        for (let i = 0; i < heights.length; i++) {
            // Enquanto a barra atual for MENOR que a do topo da pilha
            while (stack.length > 0 && heights[stack[stack.length - 1]] > heights[i]) {
                let h = heights[stack.pop()]; // A altura da barra que vamos processar
                
                // Se a pilha estiver vazia, a largura é a distância até i
                // Se não, a largura é a distância entre o i e o novo topo da pilha
                let width = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;
                
                maxArea = Math.max(maxArea, h * width);
            }
            stack.push(i);
        }

        // Importante: restaurar o array caso ele seja usado em outro lugar (opcional)
        heights.pop(); 
        return maxArea;
    }
}

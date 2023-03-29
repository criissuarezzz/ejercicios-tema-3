class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]
    
    def __getitem__(self, idx):
        return self.data[idx]
    
    def __str__(self):
        return '\n'.join([' '.join([str(val) for val in row]) for row in self.data])
    
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Las matrices no son compatibles para la multiplicación.")
        result = Matrix(self.rows, other.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                dot_product = sum([self[i][k] * other[k][j] for k in range(self.cols)])
                result[i][j] = dot_product
        return result
    
    def swap_rows(self, i, j):
        self[i], self[j] = self[j], self[i]
    
    def add_row(self, i, j, scale=1):
        for k in range(self.cols):
            self[i][k] += scale * self[j][k]
    
    def eliminate(self):
        num_swaps = 0
        for j in range(self.cols):
            pivot_row = max(range(j, self.rows), key=lambda i: abs(self[i][j]))
            if pivot_row != j:
                self.swap_rows(j, pivot_row)
                num_swaps += 1
            for i in range(j+1, self.rows):
                scale = -self[i][j] / self[j][j]
                self.add_row(i, j, scale)
        return num_swaps
    
    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("La matriz debe ser cuadrada para calcular el determinante.")
        temp_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                temp_matrix[i][j] = self[i][j]
        num_swaps = temp_matrix.eliminate()
        det = 1
        for i in range(temp_matrix.rows):
            det *= temp_matrix[i][i]
        return det * (-1) ** num_swaps

# Crear una matriz de 3x3
m = Matrix(3, 3)
m[0] = [1, 2, 3]
m[1] = [4, 5, 6]
m[2] = [7, 8, 9]

# Calcular el determinante
det = m.determinant()
print(det)  # Output: 0

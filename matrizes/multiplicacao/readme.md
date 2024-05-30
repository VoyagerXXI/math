# Multiplicação de  Matrizes

  Matrizes são estruturas matemáticas organizadas em forma de tabelas. Cada elemento de uma matriz é identificado pela posição que ocupa, determinada pelo número da linha e da coluna em que se encontra.

  + Multiplicar matrizes com o mesmo numero de linhas
  
    ```math
      A =
      \begin{bmatrix} 
        1 & 1 & 1 \\
        2 & 2 & 2 \\
        3 & 3 & 3
      \end{bmatrix}
      \times
      B =
      \begin{bmatrix} 
        4 & 4 & 4 \\
        5 & 5 & 5 \\
        6 & 6 & 6
      \end{bmatrix}
    ```
    Multiplique cada elemento da linha i de **A** pelos elementos correspondentes da coluna j de **B**.

    ```math
      A \times B
      =
      \begin{bmatrix} 
        (1 ⋅ 4)+(1 ⋅ 5)+(1 ⋅ 6) & (1 ⋅ 4)+(1 ⋅ 5)+(1 ⋅ 6) & (1 ⋅ 4)+(1 ⋅ 5)+(1 ⋅ 6) \\
        (2 ⋅ 4)+(2 ⋅ 5)+(2 ⋅ 6) & (2 ⋅ 4)+(2 ⋅ 5)+(2 ⋅ 6) & (2 ⋅ 4)+(2 ⋅ 5)+(2 ⋅ 6) \\
        (3 ⋅ 4)+(3 ⋅ 5)+(3 ⋅ 6) & (3 ⋅ 4)+(3 ⋅ 5)+(3 ⋅ 6) & (3 ⋅ 4)+(3 ⋅ 5)+(3 ⋅ 6)
      \end{bmatrix}
      =
      \begin{bmatrix} 
        15 & 15 & 15 \\
        30 & 30 & 30 \\
        45 & 45 & 45
      \end{bmatrix}
    ```
  + Multiplicar matrizes com o mesmo numeros diferentes de colunas

  ```math
      A =
      \begin{bmatrix} 
        1 & 1 \\
        2 & 2 \\
        3 & 3 
      \end{bmatrix}
      \times
      B =
      \begin{bmatrix} 
        4 & 4 & 4 \\
        5 & 5 & 5 
      \end{bmatrix}
  ```
  O número de colunas de A(2) é igual ao número de linhas de B (2), tornando a multiplicação A×B possível.

  ```math
      A \times B 
      =
      \begin{bmatrix} 
        (1 ⋅ 4)+(1 ⋅ 5) & (1 ⋅ 4)+(1 ⋅ 5) & (1 ⋅ 4)+(1 ⋅ 5) \\
        (2 ⋅ 4)+(2 ⋅ 5) & (2 ⋅ 4)+(2 ⋅ 5) & (2 ⋅ 4)+(2 ⋅ 5) \\
        (3 ⋅ 4)+(3 ⋅ 5) & (3 ⋅ 4)+(3 ⋅ 5) & (3 ⋅ 4)+(3 ⋅ 5)
      \end{bmatrix}
      =
      \begin{bmatrix} 
         9 &  9 &  9 \\
        18 & 18 & 18 \\
        27 & 27 & 27
      \end{bmatrix}
  ```

  + Extra 

  ```math
      A =
      \begin{bmatrix} 
        2 & 8 & 3\\
        5 & 4 & 1
      \end{bmatrix}
      \times
      B =
      \begin{bmatrix} 
        4 & 1 \\
        6 & 3 \\
        2 & 4
      \end{bmatrix}
  ```
  ```math
      A \times B 
      =
      \begin{bmatrix} 
        (2 ⋅ 4) + (8 ⋅ 6) + (3 ⋅ 2) & (2 ⋅ 1) + (8 ⋅ 3) + (3 ⋅ 4)\\
        (5 ⋅ 4) + (4 ⋅ 6) + (1 ⋅ 2) & (5 ⋅ 1) + (4 ⋅ 3) + (1 ⋅ 4)
      \end{bmatrix}
      =
      \begin{bmatrix} 
        62 & 38 \\
        46 & 21
      \end{bmatrix}
  ```

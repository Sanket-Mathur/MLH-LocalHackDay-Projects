# Build a Sudoku Solver

A sudoku solver is a program that can solve a sudoku puzzle. 

The sudoku puzzle is a 9x9 grid of numbers, with each number from 1 to 9. The puzzle is solved by placing the right number in each cell in of grid.

The solution currently is set to not print the puzzle at each step but it can be changed passing a parameter to the solve function, however, it highly effects the time of execution.

## Instructions to execute the script
- Have python (python3) and python-pip installed in the machine
- Execute the script
  ```
  python main.py # enter the input yourself
  # OR
  cat sample.txt | python main.py # save the input in the text file
  ```

## Sample Input
```
5 3 _ _ 7 _ _ _ _
6 _ _ 1 9 5 _ _ _
_ 9 8 _ _ _ _ 6 _
8 _ _ _ 6 _ _ _ 3
4 _ _ 8 _ 3 _ _ 1
7 _ _ _ 2 _ _ _ 6
_ 6 _ _ _ _ 2 8 _
_ _ _ 4 1 9 _ _ 5
_ _ _ _ 8 _ _ 7 9
```

## Sample Output
```
5 3 4 6 7 8 9 1 2 
6 7 2 1 9 5 3 4 8 
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```
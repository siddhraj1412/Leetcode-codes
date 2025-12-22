---

# Intuition 
A valid Sudoku requires that each number (1–9) appears only once in every row, column, and 3×3 sub-grid.  
To efficiently detect duplicates while scanning the board, we can track seen numbers using hash sets.  
If a number appears again in the same row, column, or sub-grid, the board is invalid. 


# Approach
We iterate through each cell of the 9×9 board.  
- If the cell is empty ('.'), we skip it.  
- Otherwise, we check whether the number already exists in:
  - the current row
  - the current column
  - the corresponding 3×3 sub-grid  

We use three defaultdicts of sets:
- `rows[r]` stores numbers seen in row `r`
- `cols[c]` stores numbers seen in column `c`
- `squares[(r//3, c//3)]` stores numbers seen in the 3×3 sub-grid  

If a duplicate is found in any of these, we return False immediately.  
If the entire board is processed without conflicts, the Sudoku is valid.  

# Complexity

* Time complexity: $$O(1)$$
The board size is fixed at 9×9, so the total operations are constant 

* Space complexity: $$O(1)$$
At most 81 values are stored across rows, columns, and squares

# Code

```python3 []
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=collections.defaultdict(set)
        rows=collections.defaultdict(set)
        squares=collections.defaultdict(set) # here key is r//3,c//3

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue # cause it's empty and we dont have any use of it
                if (board[r][c] in rows[r] or # used to check if its in same row
                    board[r][c] in cols[c] or # used to check if its in same column 
                    board[r][c] in squares[(r//3,c//3)]# to check if its in the same square
                    ):
                    return False
                # if it isnt repeated then just add it in our set hashmap
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True # cause we cant decide any repetation
 
```

---



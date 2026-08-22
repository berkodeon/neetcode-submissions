class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Handle with one set and string manupilation [medium]
        seen = set()
        EMPTY_CELL = "."

        for r in range(9):
            for c in range(9):
                curr_cell = board[r][c]
                if curr_cell == EMPTY_CELL:
                    continue
                
                box_id = ((r//3) *3) + c//3
                row_index = f"r-{r}-{curr_cell}"
                column_index = f"c-{c}-{curr_cell}"
                box_index = f"b-{box_id}-{curr_cell}"

                if row_index in seen or column_index in seen or box_index in seen:
                    return False
                
                seen.add(row_index)
                seen.add(column_index)
                seen.add(box_index)
        return True



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Handle with one set and string manupilation [medium]
        EMPTY_CELL = "."
        seen_at_rows = [0]*9
        seen_at_columns = [0]*9
        seen_at_boxes = [0]*9

        for r in range(9):
            for c in range(9):
                raw_curr_cell = board[r][c]
                if raw_curr_cell == EMPTY_CELL:
                    continue
                curr_cell = int(raw_curr_cell) - 1
                box_id = ((r//3) *3) + c//3
                if (1 << curr_cell) & seen_at_rows[r] or (1 << curr_cell) & seen_at_columns[c] or (1 << curr_cell) & seen_at_boxes[box_id]:
                    return False
                
                seen_at_rows[r] |= (1 << curr_cell)
                seen_at_columns[c] |= (1 << curr_cell)
                seen_at_boxes[box_id] |= (1 << curr_cell)
        return True



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Normal 3 hashmap solution! [easy]
        EMPTY_CELL = "."
        seen_at_rows = defaultdict(set)
        seen_at_columns = defaultdict(set)
        seen_at_boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr_cell = board[r][c]
                if curr_cell == EMPTY_CELL:
                    continue
                
                box_id = ((r//3) *3) + c//3
                if curr_cell in seen_at_rows[r] or curr_cell in seen_at_columns[c] or curr_cell in seen_at_boxes[box_id]:
                    return False
                
                seen_at_rows[r].add(curr_cell)
                seen_at_columns[c].add(curr_cell)
                seen_at_boxes[box_id].add(curr_cell)
        return True



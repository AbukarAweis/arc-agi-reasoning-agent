import copy
import numpy as np

from collections import deque, Counter

class Utilities:
    def __init__ (self):
        self.colors = {0: 'black', 1: 'blue', 2: 'red', 3: 'green', 4: 'yellow',
                        5: 'gray', 6: 'magenta', 7: 'orange', 8: 'cyan', 9: 'brown'}

        self.background_color = 0

        self.TRANSFORMATION_PROPERTIES = {

            ################## MILESTONE B TRANSFORMATIONS ##################
            'rotate': {
                'priority': 10,
                'grid_size': 'preserved',
                'color_set': 'preserved',
                'background_color': 'unknown',
                'background_count': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'mirror': {
                'priority': 10,
                'grid_size': 'preserved',
                'color_set': 'preserved',
                'background_color': 'unknown',
                'background_count': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'color_swap': {
                'priority': 10,
                'grid_size': 'preserved',
                'color_set': 'unknown',
                'background_color': 'unknown',
                'background_count': 'unknown',
                'object_count': 'preserved',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'color_black': {
                'priority': 5,
                'grid_size': 'preserved',
                'color_set': 'unknown',
                'background_color': 'unknown',
                'background_count': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'color_new': {
                'priority': 5,
                'grid_size': 'preserved',
                'color_set': 'changed',
                'background_color': 'unknown',
                'background_count': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'align': {
                'priority': 8,
                'grid_size': 'preserved',
                'color_set': 'preserved',
                'background_color': 'unknown',
                'background_count': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'crop_zeros': {
                'priority': 7,
                'grid_size': 'changed',
                'color_set': 'unknown',
                'background_count': 'unknown',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'hollow_out': {
                'priority': 6,
                'grid_size': 'preserved',
                'color_set': 'unknown',
                'background_color': 'unknown',
                'background_count': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'expand': {
                'priority': 5,
                'grid_size': 'unknown',
                'color_set': 'unknown',
                'background_color': 'unknown',
                'background_count': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'draw_cross': {
                'priority': 4,
                'grid_size': 'preserved',
                'color_set': 'unknown',
                'background_color': 'unknown',
                'background_count': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'draw_spiral': {
                'priority': 4,
                'grid_size': 'preserved',
                'color_set': 'unknown',
                'background_color': 'unknown',
                'background_count': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'logical': {
                'priority': 3,
                'grid_size': 'changed',
                'color_set': 'unknown',
                'background_color': 'unknown',
                'background_count': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            ################## MILESTONE C TRANSFORMATIONS ##################
            'connect': {
                'priority': 8,
                'grid_size': 'preserved',
                'color_set': 'unknown',
                'background_color': 'unknown',
                'background_count': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'changed',
                'object_color': 'unknown',
            },

            'draw_laser': {
                'priority': 8,
                'grid_size': 'preserved',
                'color_set': 'unknown',
                'background_color': 'unknown',
                'background_count': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'crop_bounds': {
                'priority': 6,
                'grid_size': 'changed',
                'color_set': 'unknown',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'draw_tails': {
                'priority': 8,
                'grid_size': 'preserved',
                'color_set': 'preserved',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'color_in_out': {
                'priority': 6,
                'grid_size': 'preserved',
                'color_set': 'changed',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'organize': {
                'priority': 6,
                'grid_size': 'changed',
                'color_set': 'preserved',
                'background_count': 'preserved',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'tile': {
                'priority': 6,
                'grid_size': 'changed',
                'color_set': 'preserved',
                'background_count': 'unknown',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'col_to_row': {
                'priority': 5,
                'grid_size': 'preserved',
                'color_set': 'preserved',
                'background_count': 'unknown',
                'background_color': 'unknown',
                'object_count': 'preserved',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'color_cycles': {
                'priority': 6,
                'grid_size': 'preserved',
                'color_set': 'changed',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'steps': {
                'priority': 7,
                'grid_size': 'changed',
                'color_set': 'preserved',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'combine': {
                'priority': 3,
                'grid_size': 'changed',
                'color_set': 'preserved',
                'background_count': 'unknown',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'move_once': {
                'priority': 7,
                'grid_size': 'preserved',
                'color_set': 'preserved',
                'background_count': 'unknown',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'take_out_brackets': {
                'priority': 5,
                'grid_size': 'preserved',
                'color_set': 'preserved',
                'background_count': 'unknown',
                'background_color': 'unknown',
                'object_count': 'preserved',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'fence': {
                'priority': 3,
                'grid_size': 'preserved',
                'color_set': 'changed',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'unknonw',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            ################## MILESTONE D TRANSFORMATIONS ##################
            'fill_majority': {
                'priority': 4,
                'grid_size': 'preserved',
                'color_set': 'changed',
                'background_count': 'unknown',
                'background_color': 'unknown',
                'object_count': 'preserved',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'draw_edges': {
                'priority': 5,
                'grid_size': 'preserved',
                'color_set': 'changed',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'changed',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'tetris': {
                'priority': 3,
                'grid_size': 'preserved',
                'color_set': 'preserved',
                'background_count': 'unknown',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'colored_steps': {
                'priority': 4,
                'grid_size': 'changed',
                'color_set': 'changed',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'tile_divider': {
                'priority': 2,
                'grid_size': 'preserved',
                'color_set': 'preserved',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'mirror_center': {
                'priority': 2,
                'grid_size': 'preserved',
                'color_set': 'preserved',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'draw_path': {
                'priority': 3,
                'grid_size': 'preserved',
                'color_set': 'changed',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'changed',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'fill_shape': {
                'priority': 2,
                'grid_size': 'changed',
                'color_set': 'unknown',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'changed',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'draw_colored_path': {
                'priority': 9,
                'grid_size': 'preserved',
                'color_set': 'changed',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'changed',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },


            'color_cycles_in_out': {
                'priority': 4,
                'grid_size': 'preserved',
                'color_set': 'changed',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'changed',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'in_cycle_count': {
                'priority': 6,
                'grid_size': 'changed',
                'color_set': 'changed',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'swap_color_palette': {
                'priority': 4,
                'grid_size': 'changed',
                'color_set': 'changed',
                'background_count': 'changed',
                'background_color': 'changed',
                'object_count': 'changed',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'draw_tent': {
                'priority': 5,
                'grid_size': 'changed',
                'color_set': 'changed',
                'background_count': 'changed',
                'background_color': 'changed',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

            'tile_extra': {
                'priority': 8,
                'grid_size': 'changed',
                'color_set': 'preserved',
                'background_count': 'changed',
                'background_color': 'unknown',
                'object_count': 'unknown',
                'object_adjacent': 'unknown',
                'object_color': 'unknown',
            },

        }

    '#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #'
    'HELPER FUNCTIONS'
    '#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #'

    def _in_bounds(self, grid, row, col):
        return 0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]

    def _find_background_color(self, grid):
        return self.background_color

    def _find_non_background_color(self, grid):
        if grid is None or grid.size == 0:
            return 0

        unique, counts = np.unique(grid, return_counts=True)

        non_zero = unique != self.background_color
        unique = unique[non_zero]
        counts = counts[non_zero]

        if counts.size == 0:
            return 0

        return unique[np.argmax(counts)]

    def _find_neighbor_positions(self, grid, row, col, only=''):
        neighbor_positions = []
        (up, down, right, left,
         up_right, up_left, down_right, down_left) = None, None, None, None, None, None, None, None

        if self._in_bounds(grid, row - 1, col): up =   (row - 1, col)
        if self._in_bounds(grid, row + 1, col): down =  (row + 1, col)
        if self._in_bounds(grid, row, col + 1): right = (row, col + 1)
        if self._in_bounds(grid, row, col - 1): left =  (row, col - 1)
        if self._in_bounds(grid, row - 1, col + 1): up_right =  (row - 1, col + 1)
        if self._in_bounds(grid, row - 1, col - 1): up_left =   (row - 1, col - 1)
        if self._in_bounds(grid, row + 1, col + 1): down_right = (row + 1, col + 1)
        if self._in_bounds(grid, row + 1, col - 1): down_left =  (row + 1, col - 1)

        if only == 'cardinal':
            if up is not None: neighbor_positions.append(up)
            if down is not None: neighbor_positions.append(down)
            if right is not None: neighbor_positions.append(right)
            if left is not None: neighbor_positions.append(left)
        elif only == 'diagonal':
            if up_right is not None: neighbor_positions.append(up_right)
            if up_left is not None: neighbor_positions.append(up_left)
            if down_right is not None: neighbor_positions.append(down_right)
            if down_left is not None: neighbor_positions.append(down_left)
        else:
            if up is not None: neighbor_positions.append(up)
            if down is not None: neighbor_positions.append(down)
            if right is not None: neighbor_positions.append(right)
            if left is not None: neighbor_positions.append(left)
            if up_right is not None: neighbor_positions.append(up_right)
            if up_left is not None: neighbor_positions.append(up_left)
            if down_right is not None: neighbor_positions.append(down_right)
            if down_left is not None: neighbor_positions.append(down_left)

        return neighbor_positions

    def _does_neighbor_exists(self, grid, row, col, direction):
        if direction == 'up': return self._in_bounds(grid, row - 1, col)
        if direction == 'down': return self._in_bounds(grid, row + 1, col)
        if direction == 'right': return self._in_bounds(grid, row, col + 1)
        if direction == 'left': return self._in_bounds(grid, row, col - 1)
        if direction == 'up right': return self._in_bounds(grid, row - 1, col + 1)
        if direction == 'up left': return self._in_bounds(grid, row - 1, col - 1)
        if direction == 'down right': return self._in_bounds(grid, row + 1, col + 1)
        if direction == 'down left': return self._in_bounds(grid, row + 1, col - 1)
        return False

    def _move(self, cur_cell, direction):
        if direction == 'up': return (cur_cell[0] - 1, cur_cell[1])
        elif direction == 'down': return (cur_cell[0] + 1, cur_cell[1])
        elif direction == 'right': return (cur_cell[0], cur_cell[1] + 1)
        elif direction == 'left': return (cur_cell[0], cur_cell[1] - 1)
        elif direction == 'up right': return (cur_cell[0] - 1, cur_cell[1] + 1)
        elif direction == 'up left': return (cur_cell[0] - 1, cur_cell[1] - 1)
        elif direction == 'down right': return (cur_cell[0] + 1, cur_cell[1] + 1)
        elif direction == 'down left': return (cur_cell[0] + 1, cur_cell[1] - 1)

    def _move_object(self, grid, obj_cells, direction):
        new_obj_cells = []
        if direction == 'up':
            for cell in obj_cells:
                new_cell = (cell[0] - 1, cell[1])
                if self._in_bounds(grid, new_cell[0], new_cell[1]):
                    new_obj_cells.append((cell[0] - 1, cell[1]))

        elif direction == 'down':
            for cell in obj_cells:
                new_cell = (cell[0] + 1, cell[1])
                if self._in_bounds(grid, new_cell[0], new_cell[1]):
                    new_obj_cells.append((cell[0] + 1, cell[1]))

        elif direction == 'right':
            for cell in obj_cells:
                new_cell = (cell[0], cell[1] + 1)
                if self._in_bounds(grid, new_cell[0], new_cell[1]):
                    new_obj_cells.append((cell[0], cell[1] + 1))

        elif direction == 'left':
            for cell in obj_cells:
                new_cell = (cell[0], cell[1] - 1)
                if self._in_bounds(grid, new_cell[0], new_cell[1]):
                    new_obj_cells.append((cell[0], cell[1] - 1))

        return new_obj_cells

    def _rotate_object(self, grid, obj_cells):
        rotated_object = []

        rows = [r for r, _ in obj_cells]
        cols = [c for _, c in obj_cells]

        min_r, min_c = min(rows), min(cols)

        for cell in obj_cells:
            row = cell[0]
            col = cell[1]

            # shift to origin
            r = row - min_r
            c = col - min_c

            # rotate
            new_r = c
            new_c = r

            # shift back
            new_cell = (new_r + min_r, new_c + min_c)

            if not self._in_bounds(grid, new_cell[0], new_cell[1]):
                return obj_cells

            rotated_object.append(new_cell)

        return rotated_object

    def _line_object_to_gap(self, grid, obj_cells, gap_cols):
        lined_object = []

        old_cols = sorted(set(c for _, c in obj_cells))

        for cell in obj_cells:
            row = cell[0]
            col = cell[1]

            idx = old_cols.index(col)
            new_col = gap_cols[idx]

            new_cell = (row, new_col)

            if not self._in_bounds(grid, new_cell[0], new_cell[1]):
                return obj_cells

            lined_object.append(new_cell)

        return lined_object

    def _break(self, grid, labels):
        pieces = []

        if labels is None or not isinstance(labels, np.ndarray) or labels.ndim != 2:
            return grid, pieces
        if labels.size == 0 or labels.shape[0] == 0 or labels.shape[1] == 0:
            return grid, pieces

        #checking for cols and rows that have the same value in each index
        col_mask = (labels[0, :] != self.background_color) & np.all(labels == labels[0:1, :], axis=0)
        row_mask = (labels[:, 0] != self.background_color) & np.all(labels == labels[:, 0:1], axis=1)

        candidates = None
        stop = None
        axis = None

        if np.any(col_mask):
            stop = grid.shape[1] + 1
            candidates = np.sort(np.where(col_mask)[0])
            axis = 1

        elif np.any(row_mask):
            stop = grid.shape[0] + 1
            candidates = np.sort(np.where(row_mask)[0])
            axis = 0

        if candidates is None:
            return pieces

        #for every candidate row/col, find another row/col that has all the same color
        #compare the left side of the candidate and the right side of the candidate
        #if they are, they're a divider
        dividers = []
        start = 0
        for c in candidates:
            if axis == 0:
                curr = grid[c, :]
            elif axis == 1:
                curr = grid[:, c]

            curr_idx = c

            next_idx = None

            if axis == 0:
                for i in range(grid.shape[0]):
                    if np.array_equal(grid[i, :], curr) and i != curr_idx:
                        next_idx = i
                        break

            elif axis == 1:
                for i in range(grid.shape[1]):
                    if np.array_equal(grid[:, i], curr) and i != curr_idx:
                        next_idx = i
                        break

            if axis == 0:
                left = grid[start:curr_idx, :]
                right = grid[curr_idx+1:next_idx, :]

            if axis == 1:
                left = grid[:, start:curr_idx]
                right = grid[:, curr_idx+1:next_idx]

            if left.shape == right.shape:
                start = curr_idx + 1
                dividers.append(int(c))

        #finding pieces based on where the dividers are
        start = 0
        for d in dividers:
            end = d
            while end < stop:
                if axis == 0:
                    pieces.append(grid[start:end, :])
                elif axis == 1:
                    pieces.append(grid[:, start:end])

                start = end + 1
                end += d + 1

        pieces = [p for p in pieces if p.size != 0]

        if len(pieces) == 0:
            return []

        if len(pieces) < 2:
            return pieces

        ref_shape = pieces[0].shape

        for p in pieces:
            if p.shape != ref_shape:
                return None

        return pieces

    def _cut_in_half(self, grid, orientation):
        pieces = []
        if orientation == 'horizontal':
            mid = grid.shape[0] // 2
            pieces.append(grid[:mid, :])
            pieces.append(grid[mid:, :])
        elif orientation == 'vertical':
            mid = grid.shape[1] // 2
            pieces.append(grid[:, :mid])
            pieces.append(grid[:, mid:])

        ref_shape = pieces[0].shape

        for p in pieces:
            if p.shape != ref_shape:
                return None

        return pieces

    def _cut_by_dividers(self, grid, row_divs, col_divs):
        row_splits = np.split(grid, row_divs, axis=0)
        pieces = [np.split(r, col_divs, axis=1) for r in row_splits]
        return pieces

    def _expand_with_dividers(self, subgrid, divider_color, i, j, rows, cols):
        is_top = (i == 0)
        is_left = (j == 0)

        expanded = self.transform_tile(subgrid, params={})

        height, width = expanded.shape
        mid_row = height // 2
        mid_col = width // 2

        expanded = np.insert(expanded, mid_row, divider_color, axis=0)
        expanded = np.insert(expanded, mid_col, divider_color, axis=1)

        if not is_top:
            expanded = np.insert(expanded, 0, divider_color, axis=0)

        if not is_left:
            expanded = np.insert(expanded, 0, divider_color, axis=1)

        return expanded

    # CODE CITATION: written based on pseudocode found at https://en.wikipedia.org/wiki/Connected-component_labeling
    def label_objects(self, grid, background_color=0):
        label = 1
        label_arr = np.zeros_like(grid)
        status_arr = np.full(grid.shape, 'F')

        queue_1, queue_2 = deque(), deque()

        row, col = grid.shape[0], grid.shape[1]

        for i in range(row):
            for j in range(col):
                if status_arr[i][j] == 'F':
                    if grid[i][j] != background_color:
                        cur_color = grid[i][j]
                        label_arr[i][j] = label
                        status_arr[i][j] = 'T'

                        neighbors = self._find_neighbor_positions(grid, i, j)
                        for neighbor_position in neighbors:
                            n_i, n_j = neighbor_position[0], neighbor_position[1]

                            neighbor_color = grid[n_i][n_j]
                            neighbor_status = status_arr[n_i][n_j]

                            if neighbor_status != 'T' and neighbor_color == cur_color:
                                if neighbor_color != background_color:
                                    queue_1.append(neighbor_position)
                                    label_arr[n_i][n_j] = label
                                    status_arr[n_i][n_j] = 'T'
                                else:
                                    status_arr[i][j] = 'T'

                        while len(queue_1) > 0:
                            cell = queue_1.popleft()
                            pi, pj = cell[0], cell[1]
                            cell_color = grid[pi][pj]

                            cell_neighbors = self._find_neighbor_positions(grid, pi, pj)

                            for cell_neighbor_position in cell_neighbors:
                                pn_i, pn_j = cell_neighbor_position[0], cell_neighbor_position[1]

                                next_neighbor_color = grid[pn_i][pn_j]
                                next_neighbor_status = status_arr[pn_i][pn_j]

                                if next_neighbor_status != 'T' and next_neighbor_color == cell_color:
                                    if next_neighbor_color != background_color:
                                        queue_2.append(cell_neighbor_position)
                                        label_arr[pn_i][pn_j] = label
                                        status_arr[pn_i][pn_j] = 'T'
                                    else:
                                        status_arr[i][j] = 'T'

                            queue_1.extend(queue_2)
                            queue_2.clear()
                        label += 1
                else:
                    status_arr[i][j] = 'T'

        return label_arr
    # END CODE CITATION FOR: https://en.wikipedia.org/wiki/Connected-component_labeling

    def _find_object_cells(self, label, object_labels):
        #returns all cells that make up an object
        object_positions = []

        labels, counts = np.unique(object_labels, return_counts=True)
        count_by_label = dict(zip(labels, counts))

        for i in range(object_labels.shape[0]):
            for j in range(object_labels.shape[1]):
                if label == self.background_color:
                    continue

                if object_labels[i][j] != label:
                    continue

                object_positions.append((i, j))

                if count_by_label[label] == 1:
                    return object_positions

        return object_positions

    def _find_mirrored_object_cells(self, grid, obj_cells, line, orientation):
        mirrored_obj_cells = []

        for cell in obj_cells:
            new_cell = self._find_mirrored_pos(grid, cell, line, orientation)

            if new_cell is not None:
                mirrored_obj_cells.append(new_cell)

        return mirrored_obj_cells

    def _find_object_perimeter(self, label, object_labels):
        # returns all cells that are at the perimeter of the object
        object_perimeter = []

        for i in range(object_labels.shape[0]):
            for j in range(object_labels.shape[1]):
                if label == self.background_color:
                    continue

                if object_labels[i][j] != label:
                    continue

                neighbors = self._find_neighbor_positions(object_labels, i, j)

                for neighbor in neighbors:
                    neighbor_label = object_labels[neighbor[0]][neighbor[1]]

                    if neighbor_label != label:
                        if (i, j) not in object_perimeter:
                            object_perimeter.append((i, j))
                        break

        return object_perimeter

    def _find_cycle_centers(self, grid, cycle_perimeters):
        cycle_centers = {}

        directions = ['up', 'down', 'left', 'right']

        # using BFS to find the centers of each cycle
        for cycle_color, perimeter in cycle_perimeters.items():
            temp_grid = np.zeros(shape=grid.shape, dtype=int)
            center = []

            Q = deque()
            Q.append((0, 0))

            visited_cells = set()

            while len(Q) > 0:
                cell = Q.popleft()
                if self._in_bounds(grid, cell[0], cell[1]):
                    for dir in directions:
                        new_cell = self._move(cell, dir)

                        if new_cell not in visited_cells and new_cell not in perimeter:
                            if self._in_bounds(grid, new_cell[0], new_cell[1]):
                                temp_grid[new_cell] = cycle_color
                                visited_cells.add(new_cell)
                                Q.append(new_cell)

            rows, cols = temp_grid.shape[0], temp_grid.shape[1]

            for i in range(rows):
                for j in range(cols):
                    if temp_grid[i][j] == self.background_color and (i, j) not in perimeter:
                        center.append((i, j))

            cycle_centers.update({cycle_color: center})

        return cycle_centers

    def _find_object_adjacent(self, label, object_labels):
        # returns all cells that are adjacent to the object (including inside if hollow)
        object_adjacent = []

        for i in range(object_labels.shape[0]):
            for j in range(object_labels.shape[1]):
                if label == self.background_color:
                    continue

                if object_labels[i][j] != label:
                    continue

                neighbors = self._find_neighbor_positions(object_labels, i, j)

                for neighbor in neighbors:
                    neighbor_label = object_labels[neighbor[0]][neighbor[1]]

                    if neighbor_label != label:
                        if neighbor not in object_adjacent:
                            object_adjacent.append((neighbor[0], neighbor[1]))

        return object_adjacent

    def _find_in_out_colors(self, grid_in, grid_out):
        temp_grid = np.zeros_like(grid_out)

        in_color, out_color = -1, -1

        rows, cols = grid_out.shape[0], grid_out.shape[1]

        labels = self.label_objects(grid_in)

        num_objects = np.max(labels)

        perimeter = None

        for o in range(num_objects):
            label = o + 1
            perimeter = self._find_object_perimeter(label, labels)

        if perimeter == None:
            return in_color, out_color

        for cell in perimeter:
            temp_grid[cell] = grid_out[cell]


        up_left = (0, 0)
        down_left = (rows - 1, 0)
        up_right = (0, cols - 1)
        down_right = (rows - 1, cols - 1)

        corners = [up_left, down_left, up_right, down_right]
        directions = ['up', 'down', 'left', 'right']

        visited_cells = set()

        for corner in corners:
            Q = deque()
            Q.append(corner)

            while len(Q) > 0:
                cell = Q.popleft()
                if self._in_bounds(grid_out, cell[0], cell[1]):
                    for dir in directions:
                        new_cell = self._move(cell, dir)

                        if new_cell not in visited_cells and new_cell not in perimeter:
                            if self._in_bounds(grid_out, new_cell[0], new_cell[1]):
                                temp_grid[new_cell] = -1
                                out_color = grid_out[new_cell]
                                visited_cells.add(new_cell)
                                Q.append(new_cell)

        for i in range(rows):
            for j in range(cols):
                cell_color = temp_grid[i][j]

                if cell_color == self.background_color:
                    in_color = grid_out[i][j]

        return in_color, out_color

    def _find_new_color(self, grid_in, grid_out):
        in_colors, counts = np.unique(grid_in, return_counts=True)
        out_colors, counts = np.unique(grid_out, return_counts=True)

        new_candidates = out_colors[~np.isin(out_colors, in_colors)]
        if new_candidates.size == 0:
            return None

        new_color = new_candidates[0]

        return new_color

    def _find_removed_color(self, grid_in, grid_out):
        in_colors, counts = np.unique(grid_in, return_counts=True)
        out_colors, counts = np.unique(grid_out, return_counts=True)

        new_candidates = in_colors[~np.isin(in_colors, out_colors)]
        if new_candidates.size == 0:
            return None

        new_color = new_candidates[0]

        return new_color

    def _find_preserved_colors(self, grid_in, grid_out):
        in_colors, counts = np.unique(grid_in, return_counts=True)
        out_colors, counts = np.unique(grid_out, return_counts=True)

        preserved_colors = in_colors[np.isin(in_colors, out_colors)]
        preserved_colors = preserved_colors[preserved_colors != self.background_color]

        if preserved_colors.size == 0:
            return None

        return preserved_colors.tolist()

    def _find_mover_anchor(self, grid_in, grid_out):
        mover = None
        anchor = None

        rows, cols = grid_in.shape[0], grid_in.shape[1]

        for i in range(rows):
            for j in range(cols):
                cell_color = grid_in[i][j]

                if cell_color == self.background_color:
                    continue

                if grid_out[i][j] != cell_color:
                    mover = grid_in[i][j]

                if grid_out[i][j] == cell_color:
                    anchor = grid_in[i][j]

        return mover, anchor

    def _find_brackets(self, grid, params):
        info = {}

        temp = self.transform_crop_zeros(grid, params=params)

        up = temp[0]
        down = temp[-1]
        right = temp[:, -1]
        left = temp[:, 0]

        orientation = None
        color = None

        if (np.all(up == up[0]) and up[0] != 0) and (np.all(down == down[0]) and down[0] != 0):
            orientation = 'horizontal'
            color = np.max(up) if np.max(up) != -1 else None
        elif (np.all(left == left[0]) and left[0] != 0) and (np.all(right == right[0]) and right[0] != 0):
            orientation = 'vertical'
            color = np.max(left) if np.max(left) != -1 else None

        if orientation is None or color is None:
            return info

        first_idx = None
        second_idx = None

        if orientation == 'vertical':
            for col in grid:
                if any(col):
                    first_idx = np.where(col != 0)[0][0]
                    second_idx = np.where(col != 0)[0]
                    second_idx = second_idx[-1] if len(second_idx) > 0 else None
                    break

        elif orientation == 'horizontal':
            for row in grid:
                if any(row):
                    first_idx = np.where(row != 0)[0][0]
                    second_idx = np.where(row != 0)[0]
                    second_idx = second_idx[-1] + 1 if len(second_idx) > 0 else None
                    break

        if orientation == 'vertical':
            width = np.count_nonzero(temp[0]) // 2
            length = np.count_nonzero(temp[:, 0])

        elif orientation == 'horizontal':
            width = np.count_nonzero(temp[:, 0]) // 2
            length = np.count_nonzero(temp[0])

        num_cells = width + length

        if first_idx is None or second_idx is None:
            return grid

        info.update({'orientation': orientation,
                     'color': int(color),
                     'first_idx': int(first_idx),
                     'second_idx': int(second_idx),
                     'width': int(width),
                     'length': int(length),
                     'num_cells': int(num_cells)})

        return info

    def _find_mirrored_pos(self, grid, cell, line, orientation):
        if orientation == 'vertical':
            mirror_pos = (cell[0], 2 * line - cell[1])

        else:
            mirror_pos = (2 * line - cell[0], cell[1])

        if self._in_bounds(grid, mirror_pos[0], mirror_pos[1]):
            return mirror_pos

        return None

    def _calc_shape(self, object_cells):
        min_row = np.array(object_cells)[:, 0].min()
        min_col = np.array(object_cells)[:, 1].min()

        #normalize each cell position to get the shape
        shape = []
        for cell in object_cells:
            shape.append((int(cell[0] - min_row), int(cell[1] - min_col)))

        return shape

    def _get_color(self, grid, object_cells):

        color = None
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i][j] == self.background_color:
                    continue

                for c in object_cells:
                    color = grid[c[0]][c[1]]

        return (int(color), self.colors[color])

    def _extract_object_info(self, grid):
        object_labels = self.label_objects(grid)

        object_features = []

        labels, _ = np.unique(object_labels, return_counts=True)

        for label in labels:
            temp = {}
            if label == self.background_color: continue

            temp.update({'cells': self._find_object_cells(label, object_labels)})
            temp.update({'perimeter': self._find_object_perimeter(label, object_labels)})
            temp.update({'adjacent': self._find_object_adjacent(label, object_labels)})

            area = len(temp['cells']) if len(temp['cells']) is not None else None
            temp.update({'area': area})

            temp.update({'shape': self._calc_shape(temp['cells'])})
            temp.update({'color': self._get_color(grid, temp['cells'])})

            object_features.append(temp)

        return object_features, object_labels

    def _find_spiral_info(self, grid):
        info = {
            'rotation': None,
            'start_corner': None,
            'directions': None,
        }

        up = grid[0]
        down = grid[-1]
        right = grid[:, -1]
        left = grid[:, 0]

        rows, cols = grid.shape[0], grid.shape[1]

        borders = [up, down, right, left]
        border = None

        for b in borders:
            mask = (b == self.background_color)
            if np.any(mask) and np.any(~mask):
                border = b
                break

        if border is None:
            return None

        gap = np.where(border == 0)[0][0]
        gap_end = gap
        while gap_end + 1 < len(border) and border[gap_end + 1] == 0:
            gap_end += 1

        gap_len = gap_end - gap + 1

        left_of_gap = border[:gap]
        right_of_gap = border[gap + 1:]

        info['gap_len'] = int(gap_len)

        #checking rotation based on which borders have gaps and how the gaps split the border
        if np.array_equal(border, up) or np.array_equal(border, right):
            info['rotation'] = 'cw' if len(left_of_gap) > len(right_of_gap) else 'ccw'
        elif np.array_equal(border, down) or np.array_equal(border, left):
            info['rotation'] = 'cw' if len(left_of_gap) < len(right_of_gap) else 'ccw'

        #setting which corner to start drawing from and direction to draw in based on the rotation
        if info['rotation'] == 'cw':
            if np.array_equal(border, down):
                info['start_corner'] = (rows - 1, 0)
                info['directions'] = ['up', 'right', 'down', 'left']

            elif np.array_equal(border, up):
                info['start_corner'] = (0, cols - 1)
                info['directions'] = ['down', 'left', 'up', 'right']

            elif np.array_equal(border, right):
                info['start_corner'] = (rows - 1, cols - 1)
                info['directions'] = ['left', 'up', 'right', 'down']

            elif np.array_equal(border, left):
                info['start_corner'] = (0, 0)
                info['directions'] = ['right', 'down', 'left', 'up']

        elif info['rotation'] == 'ccw':
            if np.array_equal(border, down):
                info['start_corner'] = (rows - 1, cols - 1)
                info['directions'] = ['up', 'left', 'down', 'right']

            elif np.array_equal(border, up):
                info['start_corner'] = (0, 0)
                info['directions'] = ['down', 'right', 'up', 'left']

            elif np.array_equal(border, right):
                info['start_corner'] = (0, cols - 1)
                info['directions'] = ['left', 'down', 'right', 'up']

            elif np.array_equal(border, left):
                info['start_corner'] = (rows - 1, 0)
                info['directions'] = ['right', 'up', 'left', 'down']

        return info

    def _detect_cycles(self, grid, only_cardinal=False):
        cycle_perimeters = {}

        labels = self.label_objects(grid, background_color=self.background_color)
        num_objects = np.max(labels)

        # detecting 4-connectivity/8-connectivity cycles for each object
        for o in range(num_objects):
            label = o + 1
            perimeter = self._find_object_perimeter(label, labels)
            if not perimeter:
                continue

            Q = deque([perimeter[0]])
            visited_cells = {perimeter[0]}
            edges = set()
            p = set(perimeter)

            while Q:
                cell = Q.popleft()

                if only_cardinal:
                    neighbors = self._find_neighbor_positions(grid, cell[0], cell[1], only='cardinal')
                else:
                    neighbors = self._find_neighbor_positions(grid, cell[0], cell[1])

                for neighbor in neighbors:
                    if neighbor in p:
                        edge = (min(cell, neighbor), max(cell, neighbor))
                        edges.add(edge)

                        if neighbor not in visited_cells:
                            visited_cells.add(neighbor)
                            Q.append(neighbor)

            # cycle detected
            if len(edges) >= len(perimeter):
                for cell in perimeter:
                    if grid[cell] not in cycle_perimeters:
                        cycle_perimeters.update({int(grid[cell]): perimeter})

        return cycle_perimeters

    def _is_cycle(self, grid, obj_cells, only_cardinal=False):
        if not obj_cells:
            return False

        obj_set = set(obj_cells)
        start = obj_cells[0]

        Q = deque([start])
        visited = {start}
        edges = set()

        while Q:
            cell = Q.popleft()

            if only_cardinal:
                neighbors = self._find_neighbor_positions(grid, cell[0], cell[1], only='cardinal')
            else:
                neighbors = self._find_neighbor_positions(grid, cell[0], cell[1])

            for neighbor in neighbors:
                if neighbor in obj_set:
                    edge = (min(cell, neighbor), max(cell, neighbor))
                    edges.add(edge)

                    if neighbor not in visited:
                        visited.add(neighbor)
                        Q.append(neighbor)

        return len(edges) >= len(obj_cells)

    def _on_same_axis(self, start, end):
        return (start[0] == end[0]) or (start[1] == end[1])

    def _find_cardinal_draw_dir(self, start, end):
        if start == end:
            return None

        if start[0] != end[0] and start[1] != end[1]:
            return None

        if start[0] < end[0]:
            return 'down'
        if start[0] > end[0]:
            return 'up'
        if start[1] < end[1]:
            return 'right'
        if start[1] > end[1]:
            return 'left'

    def _find_gaps(self, grid, border_name, border_color):
        g = grid if border_name in ['up', 'down'] else grid.T

        for idx, line in enumerate(g):
            if border_color in line and np.any(line == self.background_color):

                zeros = np.where(line == self.background_color)[0]

                if len(zeros) == 0:
                    continue

                cols = []
                temp = [int(zeros[0])]

                for i in range(1, len(zeros)):
                    if zeros[i] == zeros[i - 1] + 1:
                        temp.append(int(zeros[i]))
                    else:
                        cols.append(temp)
                        temp = [int(zeros[i])]

                cols.append(temp)

                return {'gap_line': idx, 'gap_cols': cols}

        return {}

    def _assign_objects_to_gaps(self, obj_info, border_gap_info):
        obj_info = sorted(obj_info.items(), key=lambda x: x[1]['size'], reverse=True)

        # for each object build a list of candidate gaps that it can fit into
        candidates = {}

        combined = [len(sub) for sub in border_gap_info['gap_cols']]
        flat_border_gap_info = {border_gap_info['gap_line']: combined}

        for obj_color, info in obj_info:
            obj_height = info['height']
            obj_width = info['width']

            candidates[obj_color] = []

            for line_idx, gaps in flat_border_gap_info.items():
                for gap_idx, gap_width in enumerate(gaps):

                    # width match (no rotation)
                    if obj_width == gap_width:
                        candidates[obj_color].append({
                            'line': line_idx,
                            'gap': gap_idx,
                            'rotated': False
                        })

                    # height match (rotation)
                    elif obj_height == gap_width:
                        candidates[obj_color].append({
                            'line': line_idx,
                            'gap': gap_idx,
                            'rotated': True
                        })

        # assign the objects to the appropriate candidate gap
        used_gaps = set()
        used_objects = set()
        ordered_objects = sorted(candidates.keys(), key=lambda x: len(candidates[x]))

        for obj_color in ordered_objects:
            for option in candidates[obj_color]:
                key = (option['line'], option['gap'])

                if key in used_gaps:
                    continue

                obj_info_dict = dict(obj_info)[obj_color]
                obj_info_dict['gap'] = option['gap']
                obj_info_dict['line'] = option['line']
                obj_info_dict['rotated'] = option['rotated']

                used_gaps.add(key)
                used_objects.add(obj_color)
                break

        return obj_info

    def _check_which_half_obj_is_in(self, grid, obj_color, cycle_rows, cycle_orientation):
        if cycle_orientation == 'vertical':
            first_half = cycle_rows[:len(cycle_rows) // 2]
            second_half = cycle_rows[len(cycle_rows) // 2:]

            def _in_half(half):
                return any(grid[cell] == obj_color for row in half for cell in row)

            return _in_half(first_half), _in_half(second_half)
        else:
            all_cells = [cell for row in cycle_rows for cell in row]

            mid = (min(c[1] for c in all_cells) + max(c[1] for c in all_cells)) // 2

            in_left = any(grid[c] == obj_color and c[1] < mid for c in all_cells)
            in_right = any(grid[c] == obj_color and c[1] > mid for c in all_cells)

            return in_left, in_right

    def _create_lines_obj_cells(self, obj_cells, orientation='horizontal'):
        lines = []

        line_counts = {}

        # choose axis
        if orientation == 'horizontal':
            primary = 0  # x
            secondary = 1  # y
            obj_cells = sorted(obj_cells, key=lambda c: (c[0], c[1]))
        else:
            primary = 1  # y
            secondary = 0  # x
            obj_cells = sorted(obj_cells, key=lambda c: (c[1], c[0]))

        # count cells per line
        for cell in obj_cells:
            key = cell[primary]
            if key not in line_counts:
                line_counts[key] = 0

        for cell in obj_cells:
            key = cell[primary]
            line_counts[key] += 1

        curr = -1
        temp = []

        for cell in obj_cells:
            key = cell[primary]

            if key > curr:
                curr = key

            if key == curr:
                temp.append(cell)

            if len(temp) == line_counts[key]:
                lines.append(temp)
                temp = []

        # normalizing lines (filling gaps)
        new_lines = []

        for line in lines:
            first = line[0]
            last = line[-1]

            start = first[secondary]
            end = last[secondary] + 1

            filled = []
            while start < end:
                if orientation == 'horizontal':
                    filled.append((first[0], start))
                else:
                    filled.append((start, first[1]))
                start += 1

            new_lines.append(filled)

        return new_lines

    def _find_direction_to_move_in(self, first_cell, second_cell):
        x1, y1 = first_cell
        x2, y2 = second_cell

        move_dir = []

        if x1 < x2:
            move_dir.append('down')
        elif x1 > x2:
            move_dir.append('up')

        if y1 < y2:
            move_dir.append('right')
        elif y1 > y2:
            move_dir.append('left')

        return ' '.join(move_dir)

    def _find_tent_start(self, grid_in, orientation):
        start = np.where(grid_in != self.background_color)

        if start[0].size == 0:
            return None

        if orientation == 'horizontal':
            return (int(start[0][0]), int(start[1][0]))
        else:
            return (int(start[1][0]), int(start[0][0]))

    def _get_tent_info(self, grid_out, start, old_color, new_color):
        info = {}

        # find the direction the start of the tent should be extended
        neighbors = self._find_neighbor_positions(grid_out, start[0], start[1], only='diagonal')

        temp_dirs = []
        for neighbor in neighbors:
            temp_dirs.append(self._find_direction_to_move_in(start, neighbor))

        info[int(old_color)] = temp_dirs

        # calculate spacing and the direction the new color in the tent should be drawn in
        spacing = 0
        new_start = None

        for d in info[int(old_color)]:
            brush = start

            while self._does_neighbor_exists(grid_out, brush[0], brush[1], d):
                brush = self._move(brush, d)

                other_dirs = [x for x in info[int(old_color)] if x != d]

                for od in other_dirs:
                    check_cell = self._move(brush, od)

                    if self._in_bounds(grid_out, check_cell[0], check_cell[1]):
                        if grid_out[check_cell] == new_color:
                            if new_start is None:
                                new_start = self._move(brush, od)
                                info.update({int(new_color): od})

                            spacing += 1

        # need to test to get dynamic spacing working correctly
        # info.update({'spacing': spacing})
        info.update({'spacing': 2})
        return info

    '#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #'
    'ANALYZER'
    '#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #'

    def _is_grid_changed(self, grid_in, grid_out):
        if grid_in.shape[0] == grid_out.shape[0] and grid_in.shape[1] == grid_out.shape[1]:
            return 'preserved'
        else:
            return 'changed'

    def _is_color_set_changed(self, grid_in, grid_out):
        in_colors = np.unique(grid_in)
        out_colors = np.unique(grid_out)

        if np.array_equal(in_colors, out_colors):
            return 'preserved'
        else:
            return 'changed'

    def _is_background_color_changed(self, grid_in, grid_out):
        in_colors, _ = np.unique(grid_in, return_counts=True)
        out_colors, _ = np.unique(grid_out, return_counts=True)

        if self.background_color in in_colors:
            bg = self.background_color
        else:
            bg = self._find_background_color(grid_in)

        if bg in in_colors and bg in out_colors:
            return 'preserved'
        else:
            return 'changed'

    def _is_background_count_changed(self, grid_in, grid_out):
        in_count = np.sum(grid_in == self.background_color)
        out_count = np.sum(grid_out == self.background_color)
        return 'preserved' if in_count == out_count else 'changed'

    def _is_object_count_changed(self, object_labels_in, object_labels_out):
        if object_labels_in is None or object_labels_out is None:
            return 'unknown'

        if object_labels_in.size == 0 or object_labels_out.size == 0:
            return 'preserved' if object_labels_in.size == object_labels_out.size else 'changed'

        return 'preserved' if np.max(object_labels_in) == np.max(object_labels_out) else 'changed'

    def _is_object_adjacent_changed(self, object_features_in, object_features_out):
        if len(object_features_in) != len(object_features_out):
            return 'changed'

        used_out = set()

        for i in range(len(object_features_in)):
            matched = False

            for o in range(len(object_features_out)):
                if o in used_out:
                    continue

                if object_features_in[i]['color'] != object_features_out[o]['color']:
                    continue

                if object_features_in[i]['area'] != object_features_out[o]['area']:
                    continue

                obi = np.array(object_features_in[i]['adjacent'])
                obo = np.array(object_features_out[o]['adjacent'])

                matched = True
                used_out.add(o)

                if not np.array_equal(obi, obo):
                    return 'changed'

                break

            if not matched:
                return 'changed'

        return 'preserved'

    def _is_object_perimeter_changed(self, object_features_in, object_features_out):
        if len(object_features_in) != len(object_features_out):
            return 'changed'

        used_out = set()

        for i in range(len(object_features_in)):
            matched = False
            perimeter_shape_in = self._calc_shape(object_features_in[i]['perimeter'])

            for o in range(len(object_features_out)):
                if o in used_out:
                    continue

                if object_features_in[i]['color'] != object_features_out[o]['color']:
                    continue

                perimeter_shape_out = self._calc_shape(object_features_out[o]['perimeter'])

                if perimeter_shape_in != perimeter_shape_out:
                    continue

                matched = True
                used_out.add(o)

                break

            if not matched:
                return 'changed'

        return 'preserved'

    def _is_object_color_changed(self, object_features_in, object_features_out):
        in_colors = Counter(obj['color'] for obj in object_features_in)
        out_colors = Counter(obj['color'] for obj in object_features_out)
        return 'preserved' if in_colors == out_colors else 'changed'

    def _get_possible_transforms(self, observations):
        transforms = []

        for transformation, props in self.TRANSFORMATION_PROPERTIES.items():
            score = 0
            priority = props.get('priority', 0)

            for prop, expected in props.items():
                if prop == 'priority':
                    continue

                observed = observations.get(prop, 'unknown')

                if expected == 'unknown' or observed == 'unknown':
                    continue

                if expected == observed:
                    score += 1

            transforms.append((transformation, score, priority))

        #sort by highest score first, then by priority
        transforms.sort(key=lambda x: (x[1], x[2]), reverse=True)

        ordered = [t[0] for t in transforms]

        return ordered

    def analyze(self, grid_in, grid_out):
        observations = {
            'grid_size': 'unknown',
            'color_set': 'unknown',
            'background_color': 'unknown',
            'background_count': 'unknown',
            'object_count': 'unknown',
            'object_adjacent': 'unknown',
            'object_perimeter': 'unknown',
            'object_color': 'unknown',
        }

        object_features_in, object_labels_in = self._extract_object_info(grid_in)
        object_features_out, object_labels_out = self._extract_object_info(grid_out)

        observations['grid_size'] = self._is_grid_changed(grid_in, grid_out)
        observations['color_set'] = self._is_color_set_changed(grid_in, grid_out)
        observations['background_color'] = self._is_background_color_changed(grid_in, grid_out)
        observations['background_count'] = self._is_background_count_changed(grid_in, grid_out)
        observations['object_count'] = self._is_object_count_changed(object_labels_in, object_labels_out)
        observations['object_adjacent'] = self._is_object_adjacent_changed(object_features_in, object_features_out)
        observations['object_perimeter'] = self._is_object_perimeter_changed(object_features_in, object_features_out)
        observations['object_color'] = self._is_object_color_changed(object_features_in, object_features_out)

        possible_transforms = self._get_possible_transforms(observations)
        return possible_transforms

    '#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #'
    '''MILESTONE B TRANSFORMATIONS'''
    '#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #'

    def transform_crop_zeros(self, grid, params=None):
        if params is None:
            params = {}
        transformed_grid = copy.deepcopy(grid)

        if not np.any(grid):
            return transformed_grid

        rows = np.any(grid != 0, axis=1)
        cols = np.any(grid != 0, axis=0)

        return grid[np.ix_(rows, cols)]

    def transform_rotate(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)
        transformed_grid = np.rot90(transformed_grid, params['degrees'] / 90)
        return transformed_grid

    def transform_mirror(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)
        axis = 0 if params['orientation'] == 'horizontal' else 1
        mirrored_grid = np.flip(transformed_grid, axis)
        mask = (transformed_grid == self.background_color)
        transformed_grid[mask] = mirrored_grid[mask]
        return transformed_grid

    def transform_color_swap(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)
        unique, counts = np.unique(transformed_grid, return_counts=True)

        unique = unique[unique != self.background_color]
        if unique.size < 2:
            return transformed_grid

        first_color = int(unique[0])
        second_color = int(unique[1])

        temp = -1
        transformed_grid[grid == second_color] = temp
        transformed_grid[grid == first_color] = second_color
        transformed_grid[transformed_grid == temp] = first_color

        return transformed_grid

    def transform_color_black(self, grid, params=None):
        transformed_grid = np.zeros(shape=grid.shape, dtype=int)

        train_in = params['train_in']
        train_out = params['train_out']

        remove_color = self._find_removed_color(train_in, train_out)

        unique, counts = np.unique_counts(grid)

        candidates = unique[(unique != remove_color) & (unique != self.background_color)]
        if candidates.size == 0:
            return transformed_grid

        keep_color = int(candidates[0])

        rows, cols = grid.shape[0], grid.shape[1]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == remove_color:
                    transformed_grid[i][j] = keep_color

        return transformed_grid

    def transform_color_new(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)

        in_colors, counts = np.unique(grid, return_counts=True)
        out_colors, counts = np.unique(params['train_out'], return_counts=True)

        new_color = self._find_new_color(grid, params['train_out'])
        if not new_color:
            return transformed_grid

        rows, cols = grid.shape[0], grid.shape[1]

        #recolor all of the cells that have a different color in the output
        for i in range(rows):
            for j in range(cols):
                if not np.isin(transformed_grid[i][j], out_colors):
                    transformed_grid[i][j] = new_color

        return transformed_grid

    def transform_draw_cross(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)

        if np.max(grid) == 0: return transformed_grid

        cross_color = np.max(grid) if np.max(grid) != 0 else np.min(grid)

        rows, cols = grid.shape[0], grid.shape[1]

        center = None
        for i in range(rows):
            for j in range(cols):
                if transformed_grid[i][j] != 0: center = (i, j)
        brush = center

        directions = ['up right', 'up left', 'down right', 'down left']

        for dir in directions:
            while self._does_neighbor_exists(transformed_grid, brush[0], brush[1], dir):
                transformed_grid[brush] = cross_color
                brush = self._move(brush, dir)
            transformed_grid[brush] = cross_color
            brush = center

        return transformed_grid

    def transform_draw_spiral(self, grid, params=None):
        transformed_grid = np.zeros(shape=grid.shape, dtype=int)

        train_out = params['train_out']
        spiral_color = params['output_color']

        info = self._find_spiral_info(train_out)
        if info is None:
            return transformed_grid

        rows, cols = grid.shape[0], grid.shape[1]

        directions = info['directions']
        brush = info['start_corner']
        bounds = {'up': 0, 'down': rows - 1, 'left': 0, 'right': cols - 1}

        #start from brush position and erase everything within bounds in a spiral motion
        while bounds['up'] <= bounds['down'] and bounds['left'] <= bounds['right']:
            for dir in directions:
                while self._does_neighbor_exists(transformed_grid, brush[0], brush[1], dir):
                    next_brush = self._move(brush, dir)

                    #break if the cell that is the 2nd cell to be painted is already painted or it runs into a gap
                    if self._does_neighbor_exists(transformed_grid, next_brush[0], next_brush[1], dir):
                        next_next_brush = self._move(next_brush, dir)

                        if transformed_grid[next_next_brush] == spiral_color:
                            transformed_grid[brush] = spiral_color
                            break

                    if not self._in_bounds(transformed_grid, brush[0], brush[1]):
                        return transformed_grid

                    if self._in_bounds(transformed_grid, brush[0], brush[1]):
                        transformed_grid[brush] = spiral_color
                        brush = self._move(brush, dir)

                if dir == 'right': bounds['up'] += 1
                if dir == 'down':  bounds['right'] -= 1
                if dir == 'left':  bounds['down'] -= 1
                if dir == 'up':   bounds['left'] += 1

        if info['gap_len'] > 1:
            brush = info['start_corner']

            for i in range(info['gap_len']):
                if self._in_bounds(transformed_grid, brush[0], brush[1]):
                    transformed_grid[brush] = self.background_color
                    brush = self._move(brush, info['directions'][0])

        return transformed_grid

    def transform_hollow_out(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)

        labels = self.label_objects(grid)

        num_objects = np.max(labels)
        rows, cols = grid.shape[0], grid.shape[1]

        #for each object set color of every label that is surrounded by 8 of the same label  0 (background)
        for o in range(num_objects):
            label = o + 1
            for i in range(rows):
                for j in range(cols):
                    if labels[i][j] == label:
                        neighbors = self._find_neighbor_positions(labels, i, j)
                        count_same_object = 0

                        for neighbor in neighbors:
                            object = labels[neighbor[0]][neighbor[1]]

                            if object == label:
                                count_same_object += 1

                            if count_same_object == 8: transformed_grid[i][j] = 0

        return transformed_grid

    def transform_expand(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)
        output_color = params['output_color']

        labels = self.label_objects(grid)

        rows, cols = labels.shape
        num_objects = np.max(labels)

        for o in range(num_objects):
            label = o + 1
            for i in range(rows):
                for j in range(cols):
                    if labels[i][j] == label:
                        neighbors = self._find_neighbor_positions(labels, i, j)
                        for ni, nj in neighbors:
                            if 0 <= i < transformed_grid.shape[0] and 0 <= j < transformed_grid.shape[1]:
                                transformed_grid[i][j] = output_color
                            if 0 <= ni < transformed_grid.shape[0] and 0 <= nj < transformed_grid.shape[1]:
                                transformed_grid[ni][nj] = output_color

        return transformed_grid

    def transform_align(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)

        rows, cols = grid.shape[0], grid.shape[1]

        up = grid[0]
        down = grid[-1]
        right = grid[:, -1]
        left = grid[:, 0]

        up_color = np.max(up)
        down_color = np.max(down)
        right_color = np.max(right)
        left_color = np.max(left)

        colors = [up_color, down_color, right_color, left_color]

        bounds = {'up': 0, 'down': rows - 1, 'left': 0, 'right': cols - 1}

        directions = {'up': up_color, 'down': down_color, 'left': left_color, 'right': right_color}

        for i in range(rows):
            for j in range(cols):
                cell_color = transformed_grid[i][j]
                if cell_color == self.background_color:
                    continue

                if cell_color not in colors:
                    transformed_grid[i][j] = self.background_color

                #for each direction, move non-boundary cells towards their corresponding color boundary
                if (bounds['up'] < i < bounds['down']) and (bounds['left'] < j < bounds['right']):
                    for dir, color in directions.items():
                        if cell_color == color:
                            start = (i, j)
                            next_cell = start
                            while self._does_neighbor_exists(transformed_grid, next_cell[0], next_cell[1], dir):
                                candidate = self._move(next_cell, dir)
                                if transformed_grid[candidate] == color:
                                    break
                                next_cell = candidate
                            transformed_grid[next_cell] = color
                            if next_cell != start:
                                transformed_grid[start] = self.background_color

        return transformed_grid

    def transform_logical(self, grid, params=None):
        output_color = params['output_color']
        transformed_grid = copy.deepcopy(grid)

        labels = self.label_objects(grid)

        pieces = self._break(transformed_grid, labels)

        if pieces is None or len(pieces) < 2:
            if params['logical'] == 'XOR':
                pieces = self._cut_in_half(transformed_grid, params['orientation'])

        if pieces is None or len(pieces) < 2:
            return grid

        if params['logical'] == 'AND':
            transformed_grid = np.logical_and(pieces[0] != 0, pieces[1] != 0)
        elif params['logical'] == 'OR':
            transformed_grid = np.logical_or(pieces[0] != 0, pieces[1] != 0)
        elif params['logical'] == 'NOT':
            transformed_grid = (pieces[0] == 0) & (pieces[1] == 0)
        elif params['logical'] == 'XOR':
            transformed_grid = np.logical_xor(pieces[0] != 0, pieces[1] != 0)

        transformed_grid = np.where(transformed_grid == True, output_color, 0)
        return transformed_grid

    '#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #'
    '''MILESTONE C TRANSFORMATIONS'''
    '#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #'

    def transform_connect(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)

        if grid.size == 0:
            return transformed_grid

        up = grid[0]
        down = grid[-1]
        right = grid[:, -1]
        left = grid[:, 0]

        if np.any(left) and np.any(right):
            for idx, cell_color in enumerate(left):
                if cell_color == self.background_color:
                    continue

                if cell_color == right[idx]:
                    transformed_grid[idx] = cell_color

        elif np.any(up) and np.any(down):
            for idx, cell_color in enumerate(up):
                if cell_color == self.background_color:
                    continue

                if cell_color == down[idx]:
                    transformed_grid[:, idx] = cell_color

        return transformed_grid

    def transform_draw_laser(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)

        rows, cols = grid.shape[0], grid.shape[1]

        unique, counts = np.unique(grid, return_counts=True)

        laser_color = None
        for idx, _ in enumerate(unique):
            if counts[idx] == 1:
                laser_color = unique[idx]

        if laser_color == None:
            return transformed_grid

        brush = (0, 0)

        directions = ['up', 'down', 'left', 'right']
        opposite = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}

        draw_dir = None
        for i in range(rows):
            for j in range(cols):
                cell_color = grid[i][j]

                if cell_color == self.background_color:
                    continue

                if cell_color == laser_color:
                    brush = (i, j)

        for dir in directions:
            temp = self._move(brush, dir)

            if not self._in_bounds(grid, temp[0], temp[1]):
                return transformed_grid

            if grid[temp[0]][temp[1]] == self.background_color:
                draw_dir = opposite[dir]
                break

        if draw_dir is not None:
            while self._does_neighbor_exists(transformed_grid, brush[0], brush[1], draw_dir):
                next_brush = self._move(brush, draw_dir)
                if grid[next_brush[0]][next_brush[1]] == self.background_color:
                    transformed_grid[next_brush] = laser_color

                brush = next_brush

        return transformed_grid

    def transform_draw_tails(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)

        labels = self.label_objects(grid)

        num_objects = np.max(labels)

        train_out = params['train_out']

        if num_objects == 0 or grid.shape != train_out.shape:
            return transformed_grid

        rows, cols = grid.shape[0], grid.shape[1]

        directions = ['up right', 'up left', 'down right', 'down left']
        opposite = {'up right': 'down left', 'up left': 'down right', 'down right': 'up left', 'down left': 'up right'}

        draw_dirs = {}

        #looking for cells that are surrounding by four zeros since these cells make up the tail
        #needs testing for tails that are wider than 1
        for i in range(train_out.shape[0]):
            for j in range(train_out.shape[1]):
                cell_color = int(train_out[i][j])

                if cell_color == self.background_color:
                    continue

                neighbors = self._find_neighbor_positions(train_out, i, j, only='cardinal')

                all_zero = True
                for neighbor in neighbors:
                    if train_out[neighbor[0]][neighbor[1]] != self.background_color:
                        all_zero = False

                if all_zero:
                    brush = (i, j)

                    for dir in directions:
                        next_brush = self._move(brush, dir)

                        if self._in_bounds(train_out, next_brush[0], next_brush[1]):
                            if train_out[next_brush] == cell_color:
                                if cell_color not in draw_dirs:
                                    draw_dirs.update({cell_color: None})

                                draw_dirs[cell_color] = opposite[dir]

        if len(draw_dirs) == 0:
            return transformed_grid

        #start at corner that when moving in the draw direction is the same color. draw until end of grid
        for i in range(rows):
            for j in range(cols):
                cell_color = int(grid[i][j])

                if cell_color == self.background_color:
                    continue

                if cell_color not in draw_dirs:
                    return transformed_grid

                start_corner = None

                brush = (i, j)
                next_brush = self._move(brush, draw_dirs[cell_color])

                if not self._in_bounds(grid, next_brush[0], next_brush[1]):
                    return transformed_grid

                if grid[next_brush] == cell_color:
                    start_corner = brush
                else:
                    continue

                brush = start_corner
                while self._does_neighbor_exists(grid, brush[0], brush[1], draw_dirs[cell_color]):
                    brush = self._move(brush, draw_dirs[cell_color])
                    transformed_grid[brush] = cell_color

        return transformed_grid

    def transform_crop_bounds(self, grid, params=None):
        transformed_grid = np.zeros_like(grid)

        grid = self.transform_color_swap(grid, params={})

        rows, cols = grid.shape[0], grid.shape[1]

        labels = self.label_objects(grid)

        num_objects = np.max(labels)

        obj_cells = []

        for o in range(num_objects):
            label = o + 1
            cells = self._find_object_cells(label, labels)

            if len(cells) == 1:
                obj_cells.append(cells)

        if len(obj_cells) == 0:
            return transformed_grid

        up = min(obj_cells)[0][0]
        down = max(obj_cells)[0][0]

        left = min(obj_cells)[0][1]
        right = max(obj_cells)[0][1]

        for i in range(rows):
            for j in range(cols):
                if up < i < down:
                    if left < j < right:
                        if grid[i][j] != self.background_color:
                            transformed_grid[i][j] = grid[i][j]
                        else:
                            transformed_grid[i][j] = -1

        transformed_grid = self.transform_crop_zeros(transformed_grid, params={})
        transformed_grid[transformed_grid == -1] = 0

        return transformed_grid

    def transform_color_in_out(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)

        train_in = params['train_in']
        train_out = params['train_out']

        if train_in.shape != train_out.shape:
            return transformed_grid

        in_color, out_color = self._find_in_out_colors(train_in, train_out)

        rows, cols = grid.shape[0], grid.shape[1]

        labels = self.label_objects(grid)

        num_objects = np.max(labels)

        perimeter = None

        for o in range(num_objects):
            label = o + 1
            perimeter = self._find_object_perimeter(label, labels)

        if perimeter == None:
            return transformed_grid

        for cell in perimeter:
            transformed_grid[cell] = grid[cell]

        up_left = (0, 0)
        down_left = (rows - 1, 0)
        up_right = (0, cols - 1)
        down_right = (rows - 1, cols - 1)

        corners = [up_left, down_left, up_right, down_right]
        directions = ['up', 'down', 'left', 'right']

        visited_cells = set()

        for corner in corners:
            Q = deque()
            Q.append(corner)

            while len(Q) > 0:
                cell = Q.popleft()
                if self._in_bounds(grid, cell[0], cell[1]):
                    for dir in directions:
                        new_cell = self._move(cell, dir)

                        if new_cell not in visited_cells and new_cell not in perimeter:
                            if self._in_bounds(grid, new_cell[0], new_cell[1]):
                                transformed_grid[new_cell] = out_color
                                visited_cells.add(new_cell)
                                Q.append(new_cell)

        for i in range(rows):
            for j in range(cols):
                cell_color = transformed_grid[i][j]

                if cell_color == self.background_color:
                    transformed_grid[i][j] = in_color

        return transformed_grid

    def transform_organize(self, grid, params=None):
        labels = self.label_objects(grid)

        num_objects = np.max(labels)

        cols = num_objects
        rows = 0

        color_order = []

        for o in range(num_objects):
            label = o + 1

            num_cells = len(self._find_object_cells(label, labels))
            if num_cells > rows:
                rows = num_cells

        transformed_grid = np.zeros(shape=(rows, cols), dtype=int)

        unique, counts = np.unique(grid, return_counts=True)

        if rows == 0:
            return grid

        for idx, val in enumerate(unique):
            color_order.append((int(val), int(counts[idx])))

        color_order.sort(key=lambda x: (x[1]), reverse=True)

        for idx, info in enumerate(color_order):
            color, cells = info

            transformed_grid[0: cells, idx-1] = color

        return transformed_grid

    def transform_tile(self, grid, params=None):
        rows, cols = grid.shape[0], grid.shape[1]

        transformed_grid = np.zeros(shape=(rows * 2, cols * 2), dtype=int)

        for i in range(rows):
            for j in range(cols):
                transformed_grid[i][j] = grid[i][j]

        transformed_grid = self.transform_mirror(transformed_grid, params={'orientation': 'vertical'})
        transformed_grid = self.transform_mirror(transformed_grid, params={'orientation': 'horizontal'})

        return transformed_grid

    def transform_col_to_row(self, grid, params=None):
        transformed_grid = np.zeros(shape=grid.shape, dtype=int)

        train_in = params['train_in']
        train_out = params['train_out']

        in_rows, in_cols = train_in.shape[0], train_in.shape[1]
        out_rows, out_cols = train_out.shape[0], train_out.shape[1]

        if in_rows != in_cols or out_rows != out_cols:
            return transformed_grid

        for idx, row in enumerate(grid):
            transformed_grid[:, idx] = row

        return transformed_grid

    def transform_color_cycles(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)

        bg = self._find_non_background_color(grid)

        labels = self.label_objects(grid, background_color=bg)

        num_objects = np.max(labels)

        new_color = self._find_new_color(grid, params['train_out'])
        if not new_color:
            return transformed_grid

        #detecting 4-connectivity cycles for each object
        for o in range(num_objects):
            label = o + 1
            perimeter = self._find_object_perimeter(label, labels)
            if not perimeter:
                continue

            Q = deque([perimeter[0]])
            visited_cells = {perimeter[0]}
            edges = set()
            p = set(perimeter)

            while Q:
                cell = Q.popleft()
                neighbors = self._find_neighbor_positions(grid, cell[0], cell[1], only='cardinal')

                for neighbor in neighbors:
                    if neighbor in p:
                        edge = (min(cell, neighbor), max(cell, neighbor))
                        edges.add(edge)

                        if neighbor not in visited_cells:
                            visited_cells.add(neighbor)
                            Q.append(neighbor)

            #cycle detected
            if len(edges) >= len(perimeter):
                for cell in perimeter:
                    transformed_grid[cell] = new_color

        return transformed_grid

    def transform_steps(self, grid, params=None):
        rows, cols = grid.shape[0], grid.shape[1]

        transformed_grid = np.zeros(shape=(cols // 2 , cols), dtype=int)

        color = self._find_non_background_color(grid)

        num_to_color = np.count_nonzero(grid)

        for idx, row in enumerate(transformed_grid):
            transformed_grid[idx, 0:num_to_color] = color
            num_to_color += 1

        return transformed_grid

    def transform_combine(self, grid, params=None):
        labels = self.label_objects(grid)

        pieces = self._break(grid, labels)

        if pieces is None or len(pieces) < 2:
            return grid

        rows, cols = pieces[0].shape[0], pieces[0].shape[1]
        transformed_grid = np.zeros(shape=pieces[0].shape, dtype=int)

        for piece in reversed(pieces):
            for i in range(rows):
                for j in range(cols):
                    if piece[i][j] != self.background_color:
                        transformed_grid[i][j] = piece[i][j]

        return transformed_grid

    def transform_move_once(self, grid, params=None):
        transformed_grid = np.zeros(shape=grid.shape, dtype=int)

        train_in = params['train_in']
        train_out = params['train_out']

        if train_in.shape != train_out.shape:
            return transformed_grid

        mover, anchor = self._find_mover_anchor(train_in, train_out)

        if mover is None or anchor is None:
            return transformed_grid

        rows, cols = grid.shape[0], grid.shape[1]

        directions = ['up', 'down', 'left', 'right', 'up right', 'up left', 'down right', 'down left']

        mover_pos = None
        move_dir = None
        found = False
        for i in range(rows):
            for j in range(cols):
                cell_color = grid[i][j]

                if cell_color == self.background_color:
                    continue

                if cell_color == anchor:
                    transformed_grid[i][j] = anchor

                if cell_color == mover:
                    mover_pos = (i, j)
                    brush = mover_pos

                    steps = 0
                    max_steps = grid.shape[0] * grid.shape[1] + 5

                    for d in directions:
                        while self._does_neighbor_exists(grid, brush[0], brush[1], d):
                            brush = self._move(brush, d)
                            steps += 1
                            if steps > max_steps:
                                break

                            if grid[brush] == anchor:
                                move_dir = d
                                found = True
                                break
                        brush = mover_pos

                if found:
                    new_pos = self._move(mover_pos, move_dir)
                    if self._in_bounds(transformed_grid, new_pos[0], new_pos[1]):
                        transformed_grid[new_pos] = mover

        return transformed_grid

    def transform_take_out_brackets(self, grid, params=None):
        transformed_grid = np.zeros(shape=grid.shape, dtype=int)

        brackets_info = self._find_brackets(grid, params=params)

        if len(brackets_info) == 0:
            return grid

        labels = self.label_objects(grid)
        num_objects = np.max(labels)

        non_brackets = []
        brackets = []

        unique, counts = np.unique_counts(grid)
        obj_color = unique[(unique != self.background_color) & (unique != brackets_info['color'])]
        if obj_color.size != 1:
            return grid
        obj_color = int(obj_color[0])

        #finding all bracket and non_bracket cells
        for o in range(num_objects):
            label = o + 1

            perimeter = self._find_object_perimeter(label, labels)

            if perimeter is None:
                return grid

            if len(perimeter) == brackets_info['num_cells']:
                brackets.append(perimeter)

                for cell in perimeter:
                    transformed_grid[cell] = brackets_info['color']
            else:
                non_brackets.append(perimeter)

        first_bracket = brackets[:len(brackets) // 2]
        second_bracket = brackets[len(brackets) // 2:]

        if not first_bracket or not second_bracket:
            return grid

        mirrored_positions = []

        #for each non_bracket object, calculate its distance to each bracket and mirror its cells
        #on the bracket that it's closer to
        for nb in non_brackets:
            for nb_cell in nb:
                x1, y1 = nb_cell

                d1 = min((fx - x1) ** 2 + (fy - y1) ** 2 for (fx, fy) in first_bracket[0])
                d2 = min((sx - x1) ** 2 + (sy - y1) ** 2 for (sx, sy) in second_bracket[0])

                if d1 < d2:
                    mirrored_pos = self._find_mirrored_pos(grid, nb_cell, brackets_info['first_idx'], brackets_info['orientation'])
                    if mirrored_pos is None:
                        return grid
                    mirrored_positions.append(mirrored_pos)
                else:
                    mirrored_pos = self._find_mirrored_pos(grid, nb_cell, brackets_info['second_idx'], brackets_info['orientation'])
                    if mirrored_pos is None:
                        return grid
                    mirrored_positions.append(mirrored_pos)

        for cell in mirrored_positions:

            transformed_grid[cell] = obj_color

        return transformed_grid

    def transform_fence(self, grid, params=None):
        transformed_grid = np.zeros(shape=grid.shape, dtype=int)

        train_in = params['train_in']
        train_out = params['train_out']

        unique, counts = np.unique_counts(grid)
        unique = unique[unique != self.background_color]
        new_color = self._find_new_color(train_in, train_out)

        if new_color is None or len(unique) != 2:
            return grid

        rows, cols = grid.shape[0], grid.shape[1]
        max_steps = rows * cols + 5

        #finding what direction to draw the fence in for each center point
        directions = ['up', 'down', 'left', 'right']
        info = {}

        for i in range(rows):
            for j in range(cols):
                cell_color = grid[i][j]
                opposing_color = unique[unique != cell_color][0]

                if cell_color == self.background_color:
                    continue

                if cell_color not in info:
                    info.update({int(cell_color): {'centers': [], 'draw_dirs': []}})

                info[cell_color]['centers'].append((i, j))

                transformed_grid[i][j] = cell_color
                neighbors = self._find_neighbor_positions(grid, i, j)
                for neighbor in neighbors:
                    transformed_grid[neighbor[0]][neighbor[1]] = opposing_color

        for cell_color, details in info.items():
            for center in details['centers']:
                temp = []
                for d in directions:
                    brush = center
                    for _ in range(max_steps):
                        if not self._does_neighbor_exists(grid, brush[0], brush[1], d):
                            break
                        brush = self._move(brush, d)
                        if grid[brush] != self.background_color:
                            temp.append(d)
                            break
                info[cell_color]['draw_dirs'].append(temp)

        for cell_color, details in info.items():
            opposing_color = unique[unique != cell_color][0]

            for idx, center in enumerate(details['centers']):
                draw_dir = details['draw_dirs'][idx]

                for d in draw_dir:
                    brush = self._move(center, d)
                    brush = self._move(brush, d)

                    if not self._in_bounds(transformed_grid, brush[0], brush[1]):
                        return transformed_grid

                    transformed_grid[brush] = new_color

                    #checking how many steps it takes to get from brush to next colored cell in current direction
                    steps = 0
                    for _ in range(max_steps):
                        if not self._does_neighbor_exists(transformed_grid, brush[0], brush[1], d):
                            break
                        brush = self._move(brush, d)
                        if transformed_grid[brush] == cell_color:
                            break
                        steps += 1

                    even = (steps % 2 == 0)
                    allowed_steps = steps // 2
                    even_count = 0
                    odd_count = 0

                    brush = self._move(center, d)
                    brush = self._move(brush, d)
                    transformed_grid[brush] = new_color

                    for _ in range(max_steps):
                        if not self._does_neighbor_exists(transformed_grid, brush[0], brush[1], d):
                            break
                        brush = self._move(brush, d)
                        if transformed_grid[brush] == opposing_color:
                            break

                        #for even number steps, color every other
                        #for odd number steps, color every other within allowed steps
                        if even:
                            even_count += 1
                            if even_count % 2 == 0:
                                transformed_grid[brush] = new_color
                        else:
                            odd_count += 1
                            if odd_count <= allowed_steps and odd_count % 2 == 0:
                                transformed_grid[brush] = new_color

        return transformed_grid

    '#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #'
    '''MILESTONE D TRANSFORMATIONS'''
    '#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #'

    def transform_fill_majority(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)

        cycle_perimeters = self._detect_cycles(grid)
        cycle_centers = self._find_cycle_centers(grid, cycle_perimeters)
        cycle_majority_color = {}

        # # using BFS to find the centers of each cycle
        for cycle_color, perimeter in cycle_perimeters.items():
            for cell in perimeter:
                transformed_grid[cell] = cycle_color

        # find max color of each center
        for cycle_color, center in cycle_centers.items():
            center_colors = []
            for cell in center:
                if grid[cell] == self.background_color:
                    continue

                center_colors.append(int(grid[cell]))

            unique, counts = np.unique(center_colors, return_counts=True)
            if len(counts) == 0:
                continue
            else:
                majority_color = int(unique[np.argmax(counts)])

            if cycle_color not in cycle_majority_color:
                cycle_majority_color.update({cycle_color: majority_color})

            for cell in center:
                transformed_grid[cell] = majority_color

        # erasing all single cell colors
        rows, cols = transformed_grid.shape

        for i in range(rows):
            for j in range(cols):
                cell = (i, j)

                if transformed_grid[cell] == self.background_color:
                    continue

                neighbors = self._find_neighbor_positions(transformed_grid, i, j)

                same_color_count = 0

                for neighbor in neighbors:
                    if transformed_grid[neighbor] == transformed_grid[cell]:
                        same_color_count += 1

                if same_color_count == 0:
                    transformed_grid[cell] = self.background_color

        return transformed_grid

    def transform_draw_edges(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)

        edge_color = self._find_new_color(params['train_in'], params['train_out'])

        if edge_color is None:
            return transformed_grid

        labels = self.label_objects(grid)

        obj_perimeters = self._detect_cycles(labels)
        obj_centers = self._find_cycle_centers(labels, obj_perimeters)
        obj_centers_flat = [c for c in obj_centers.values() for c in c]

        cache = []

        if not all(len(perimeters) > 0 for perimeters in obj_perimeters.values()) or \
            not all(len(centers) > 0 for centers in obj_centers.values()):
            return transformed_grid

        # drawing a line between 2 center points that are on the same horizontal/vertical line
        for obj_label_1, center_cell_1 in obj_centers.items():
            start = (center_cell_1[0][0], center_cell_1[0][1])
            cache.append(start)

            for obj_label_2, center_cell_2 in obj_centers.items():
                end = (center_cell_2[0][0], center_cell_2[0][1])

                if (start == end) or (not self._on_same_axis(start, end)):
                    continue

                curr = start
                while curr != end:
                    if transformed_grid[curr] == self.background_color:
                        transformed_grid[curr] = edge_color

                    curr = self._move(curr, self._find_cardinal_draw_dir(start, end))

        rows, cols = transformed_grid.shape[0], transformed_grid.shape[1]

        for i in range(rows):
            for j in range(cols):
                if (i, j) in obj_centers_flat:
                    transformed_grid[i][j] = self.background_color

        return transformed_grid

    def transform_tetris(self, grid, params=None):
        borders = {
            'up': grid[0],
            'down': grid[-1],
            'left': grid[:, 0],
            'right': grid[:, -1],
            }

        # find which side of the grid has a same colored border followed by the border line with gaps
        border_color = None
        border_name = None
        border_gap_info = None

        for name, cells in borders.items():
            if cells[0] == self.background_color:
                continue

            if not np.all(cells == cells[0]):
                continue

            color = cells[0]
            gap_info = self._find_gaps(grid, name, color)

            if len(gap_info) > 0:
                border_color = color
                border_name = name
                border_gap_info = gap_info
                break

        if border_name is None:
            return grid

        # find objects by first removing the border
        temp_grid = np.where(grid != border_color, grid, self.background_color)
        transformed_grid = np.where(grid == border_color, grid, self.background_color)

        labels = self.label_objects(temp_grid)
        num_objects = np.max(labels)

        obj_info = {}

        for o in range(num_objects):
            label = o + 1
            obj_cells = self._find_object_cells(label, labels)
            obj_color = int(grid[obj_cells[0]])

            obj_cells_np = np.array(obj_cells)

            rows = obj_cells_np[:, 0]
            cols = obj_cells_np[:, 1]

            height = int(rows.max() - rows.min() + 1)
            width = int(cols.max() - cols.min() + 1)

            if obj_color not in obj_info:
                obj_info[obj_color] = {'cells': obj_cells, 'size': len(obj_cells), 'height': height, 'width': width}

        obj_info = self._assign_objects_to_gaps(obj_info, border_gap_info)

        required = {'cells', 'size', 'height', 'width', 'gap', 'line', 'rotated'}

        if len(obj_info) > 0:
            has_all = all(required.issubset(info) for _, info in obj_info)

            if not has_all:
                return grid

        for obj in obj_info:
            obj_color = obj[0]
            obj_cells = obj[1]['cells']
            obj_size = obj[1]['size']
            obj_height = obj[1]['height']
            obj_width = obj[1]['width']
            obj_gap = obj[1]['gap']
            obj_line = obj[1]['line']
            obj_rotated = obj[1]['rotated']

            if obj_rotated:
                obj_cells = self._rotate_object(transformed_grid, obj_cells)


            # line up objects with their gaps
            obj_cells = self._line_object_to_gap(transformed_grid, obj_cells, border_gap_info['gap_cols'][obj_gap])

            # keep moving objects down until at least one of their cells is in the gap
            temp = copy.deepcopy(transformed_grid)

            if border_name in ['up', 'down']:
                line_vals = temp[obj_line]
            else:
                line_vals = temp[:, obj_line]

            while obj_color not in line_vals:
                obj_cells = self._move_object(temp, obj_cells, border_name)

                for cell in obj_cells:
                    temp[cell] = obj_color

            for cell in obj_cells:
                transformed_grid[cell] = obj_color

        return transformed_grid

    def transform_colored_steps(self, grid, params=None):
        # getting all colors that aren't a divider color or background
        divider_color = None
        for row in grid:
            if np.all(row == row[0]):
                divider_color = np.max(row)

        if divider_color is None:
            return grid

        uniques, counts = np.unique(grid, return_counts=True)
        uniques = uniques[uniques != self.background_color]
        uniques = uniques[uniques != divider_color]

        # temp grid that has no divider and no divider-colored objects
        temp = np.where(grid != divider_color, grid, self.background_color)
        labels = self.label_objects(temp)

        # getting the count for each unique object in temp
        obj_info = {}
        for c in uniques:
            obj_info.update({int(c): 0})

        rows, cols = temp.shape[0], temp.shape[1]

        checked_labels = []
        max_obj_count = 0
        for i in range(rows):
            for j in range(cols):
                cell_color = temp[i][j]
                cell_label = labels[i][j]

                if cell_color == self.background_color:
                    continue

                if cell_label not in checked_labels:
                    checked_labels.append(cell_label)

                    obj_info[int(cell_color)] += 1

                    if obj_info[int(cell_color)] > max_obj_count:
                        max_obj_count = obj_info[int(cell_color)]

        # sort by object count
        obj_info = dict(sorted(obj_info.items(), key=lambda x: x[1]))

        # create transformed grid
        transformed_grid = np.zeros(shape=(len(uniques), max_obj_count), dtype=int)

        for idx, info in enumerate(obj_info.items()):
            color, num_to_color = info[0], info[1]
            transformed_grid[idx, 0: num_to_color] = color

        return transformed_grid

    def transform_tile_divider(self, grid, params=None):
        # get dividers colors and indices
        divider_color = None
        for row in grid:
            if np.all(row == row[0]):
                divider_color = int(row[0])

        if divider_color is None:
            return grid

        row_divs = []
        col_divs = []

        for idx, row in enumerate(grid):
            if np.all(row == row[0]):
                row_divs.append(idx)

        for idx, col in enumerate(grid.T):
            if np.all(col == col[0]):
                col_divs.append(idx)

        # break up the grid into pieces along dividers
        pieces = self._cut_by_dividers(grid, row_divs, col_divs)

        checked_colors = []
        rows = len(pieces)
        cols = len(pieces[0])

        # for each piece, create a subgrid and expand that subgrid
        transformed_map = {}

        for i in range(rows):
            for j in range(cols):
                subgrid = pieces[i][j]

                # don't worry about subgrids that have an object color that's already been checked
                uniques = np.unique(subgrid)
                uniques = uniques[uniques != self.background_color]
                uniques = uniques[uniques != divider_color]

                new_colors = [int(c) for c in uniques if c not in checked_colors]

                if not new_colors:
                    continue

                checked_colors.extend(new_colors)

                # remove dividers if they exist in subgrid
                if np.any(subgrid == divider_color):
                    subgrid = subgrid[~np.all(subgrid == divider_color, axis=1)]
                    subgrid = subgrid[:, ~np.all(subgrid == divider_color, axis=0)]

                if subgrid.size == 0:
                    continue

                # expand subgrid by creating a 2x2 mirrored tile
                expanded_subgrid = self._expand_with_dividers(subgrid, divider_color, i, j, rows, cols)

                # map object color to subgrid
                obj_color = self._find_non_background_color(subgrid)
                if obj_color is None:
                    continue
                transformed_map[int(obj_color)] = {"grid": expanded_subgrid, "index": (i, j)}

        # build transformed_grid
        transformed_grid = copy.deepcopy(grid)

        row_bounds = [0] + row_divs + [grid.shape[0]]
        col_bounds = [0] + col_divs + [grid.shape[1]]

        for color, data in transformed_map.items():
            i, j = data["index"]
            subgrid = data["grid"]

            row_start = row_bounds[i]
            col_start = col_bounds[j]

            new_height, new_width = subgrid.shape

            if row_start + new_height > transformed_grid.shape[0] or col_start + new_width > transformed_grid.shape[1]:
                return grid

            try:
                transformed_grid[row_start:row_start + new_height,
                col_start:col_start + new_width] = subgrid
            except ValueError:
                return grid

        return transformed_grid

    def transform_mirror_center(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)

        labels = self.label_objects(grid)
        num_objs = np.max(labels)

        # print(labels)

        # getting colors for cycle and non cycle
        cycle_labels = []
        cycle_info = {}
        cycle_color = None
        obj_color = None

        # getting information for the cycles and objs
        for o in range(num_objs):
            label = o + 1

            obj_cells = self._find_object_cells(label, labels)
            is_cycle = self._is_cycle(grid, obj_cells, only_cardinal=True)

            obj_grid = np.where(labels == label, grid, self.background_color)
            obj_grid_cropped = self.transform_crop_zeros(obj_grid)

            if is_cycle:
                cycle_color = grid[obj_cells[0]]

                height, width = obj_grid_cropped.shape

                if width > height:
                    orientation = 'horizontal'
                else:
                    orientation = 'vertical'

                cycle_labels.append(label)
                cycle_info.update({label: (orientation, obj_cells)})

            if not is_cycle:
                obj_color = grid[obj_cells[0]]

        if obj_color is None:
            return grid

        # when looping through the grid, if the cell is part of a cycle, get all the rows that cycle
        # belongs to. for each row, create a start and end pointer. while moving pointers towards each
        # other, draw the obj color at the end pointer if the obj color is at the start pointer
        rows, cols = grid.shape

        for i in range(rows):
            for j in range(cols):
                cell = (i, j)
                color = grid[cell]
                label = labels[cell]

                if color == self.background_color:
                    continue

                is_cycle = False
                if label in cycle_labels:
                    is_cycle = True

                if is_cycle:
                    orientation = cycle_info[label][0]
                    cycle_cells = cycle_info[label][1]

                    cycle_lines = self._create_lines_obj_cells(cycle_cells, orientation)

                    # checking which half of the cycle the object is on
                    # in_first_half, in_second_half = self._check_which_half_obj_is_in(grid, obj_color, cycle_lines, orientation)

                    for row in cycle_lines:
                        start = 0
                        end = len(row) - 1

                        while start <= end:
                            if transformed_grid[row[start]] != cycle_color and transformed_grid[
                                row[start]] != self.background_color:
                                transformed_grid[row[end]] = obj_color

                            if transformed_grid[row[end]] != cycle_color and transformed_grid[
                                row[end]] != self.background_color:
                                transformed_grid[row[start]] = obj_color

                            start += 1
                            end -= 1

        return transformed_grid

    def transform_draw_path(self, grid, params=None):
        unique = np.unique(grid)
        non_bg = unique[unique != self.background_color]

        if len(non_bg) != 2:
            return grid

        train_in = params['train_in']
        train_out = params['train_out']

        path_color = self._find_new_color(train_in, train_out)

        transformed_grid = np.where(grid != path_color, grid, self.background_color)

        # getting draw information using training grids
        rows, cols = train_in.shape
        obj_info = {}

        for i in range(rows):
            for j in range(cols):
                cell = (i, j)
                color = train_in[cell]

                if color == self.background_color:
                    continue

                # check if the obj uses diagonal or horizontal lines in the path
                neighbors = self._find_neighbor_positions(train_out, i, j)

                first_neighbor = None

                for neighbor in neighbors:
                    neighbor_color = train_out[neighbor]

                    if neighbor_color != path_color:
                        continue

                    first_neighbor = neighbor
                    break

                if first_neighbor is None:
                    return grid

                # checking if the first neighbor of the start pixel has only cardinal neighbors or diagonal neighbors
                fn_neighbors_horizontal = self._find_neighbor_positions(train_out, first_neighbor[0], first_neighbor[1], only='cardinal')
                fn_neighbors_vertical = self._find_neighbor_positions(train_out, first_neighbor[0], first_neighbor[1])

                h_count = 0
                for fn_h in fn_neighbors_horizontal:
                    if train_out[fn_h] == self.background_color:
                        continue

                    h_count += 1
                    break

                v_count = 0
                for fn_v in fn_neighbors_vertical:
                    if train_out[fn_v] == self.background_color:
                        continue

                    v_count += 1
                    break

                # draw direction is based on number of vertical and horizontal neighbors
                if v_count > 0 and h_count == 0:
                    draw_dir = 'diagonal'
                else:
                    draw_dir = 'cardinal'

                # obj_info.update({int(color): {'pos': cell, 'draw_dir': draw_dir}})
                obj_info.update({int(color): {'draw_dir': draw_dir}})

        if len(obj_info) < 2:
            return grid

        # find position of the pixels in input grid
        rows, cols = grid.shape

        for i in range(rows):
            for j in range(cols):
                cell = (i, j)
                color = grid[cell]

                if color == self.background_color:
                    continue

                obj_info[color].update({'pos': (cell)})

        diagonal_end_pos = None

        for i in range(rows):
            for j in range(cols):
                cell = (i, j)
                color = grid[cell]

                if color == self.background_color:
                    continue

                # draw the first neighbor
                if obj_info[color]['draw_dir'] != 'diagonal':
                    continue

                other_color = next(k for k in obj_info if k != color)
                other_cell = obj_info[other_color]['pos']
                first_draw_dir = self._find_direction_to_move_in(cell, other_cell)

                brush = self._move(cell, first_draw_dir)
                transformed_grid[brush] = path_color

                # draw subsequent neighbors in draw dir without going past other color
                draw_dir = obj_info[color]['draw_dir']

                if draw_dir == 'diagonal':
                    while self._does_neighbor_exists(grid, brush[0], brush[1],
                                                     first_draw_dir) and not self._on_same_axis(brush, other_cell):
                        transformed_grid[brush] = path_color
                        brush = self._move(brush, first_draw_dir)
                    diagonal_end_pos = brush

        if diagonal_end_pos is None:
            return grid

        for i in range(rows):
            for j in range(cols):
                cell = (i, j)
                color = grid[cell]

                if color == self.background_color:
                    continue

                # draw the first neighbor
                if obj_info[color]['draw_dir'] != 'cardinal':
                    continue

                other_color = next(k for k in obj_info if k != color)
                other_cell = obj_info[other_color]['pos']
                first_draw_dir = self._find_direction_to_move_in(cell, other_cell)

                brush = self._move(cell, first_draw_dir)
                transformed_grid[brush] = path_color

                # draw subsequent neighbors in draw dir without going over the diagonal path
                draw_dir = obj_info[color]['draw_dir']

                if draw_dir == 'cardinal':
                    new_dir = self._find_direction_to_move_in(cell, diagonal_end_pos)
                    transformed_grid[brush] = 0

                    while self._does_neighbor_exists(grid, brush[0], brush[1], new_dir) and transformed_grid[
                        brush] != path_color:
                        transformed_grid[brush] = path_color
                        brush = self._move(brush, new_dir)

        return transformed_grid

    def transform_fill_shape(self, grid, params=None):
        labels = self.label_objects(grid)
        pieces = self._break(grid, labels)

        if pieces is None or len(pieces) < 2:
            return grid

        left_piece = pieces[0]
        right_piece = pieces[1]
        transformed_grid = left_piece

        # find the empty cells in the left piece and the shape cells in the right piece
        # combine if they're equal else return left piece
        rows, cols = left_piece.shape

        empty_cells = []
        shape_cells = []
        for i in range(rows):
            for j in range(cols):
                if left_piece[i][j] == self.background_color:
                    empty_cells.append((i, j))

                if right_piece[i][j] != self.background_color:
                    shape_cells.append((i, j))

        if empty_cells == shape_cells:
            transformed_grid = self.transform_combine(grid)

        return transformed_grid

    def transform_draw_colored_path(self, grid, params=None):
        if not np.any(grid == self.background_color):
            return grid

        transformed_grid = copy.deepcopy(grid)

        unique, counts = np.unique(grid, return_counts=True)

        # getting path color and new color
        mask = counts == 2
        if np.sum(mask) != 1:
            return grid

        path_color = unique[mask][0]

        if path_color is None:
            return grid

        new_color = self._find_new_color(params['train_in'], params['train_out'])
        if new_color is None:
            return grid

        # find direction to draw in
        obj_info = []
        rows, cols = grid.shape

        for i in range(rows):
            for j in range(cols):
                cell = (i, j)
                color = grid[cell]

                if color == self.background_color or color != path_color:
                    continue

                obj_info.append(cell)

        if len(obj_info) != 2:
            return grid

        start = obj_info[0]
        end = obj_info[1]
        draw_dir = self._find_direction_to_move_in(start, end)

        if draw_dir is None:
            return grid

        # draw using path_color on background and new_color on non-background color
        brush = self._move(start, draw_dir)

        while brush is not None:
            color = grid[brush]

            if color == path_color:
                break

            if color == self.background_color:
                transformed_grid[brush] = path_color
            else:
                print(new_color)
                transformed_grid[brush] = new_color

            brush = self._move(brush, draw_dir)

        return transformed_grid

    def transform_color_cycles_in_out(self, grid, params=None):
        transformed_grid = copy.deepcopy(grid)

        # using train data to find colors
        train_in = params['train_in']
        train_out = params['train_out']

        if train_in.shape != train_out.shape:
            return grid

        if not self._detect_cycles(grid, only_cardinal=True):
            return grid

        cycle_color = self._find_preserved_colors(train_in, train_out)

        if cycle_color is None:
            return grid

        cycle_color = cycle_color[0]

        in_color, _ = self._find_in_out_colors(train_in, train_out)

        unique, counts = np.unique(train_out, return_counts=True)

        if len(unique) == 0:
            return grid

        mask = (unique != cycle_color) & (unique != self.background_color) & (unique != in_color)
        if not np.any(mask):
            return grid

        out_color = unique[mask][0]

        if in_color == -1:
            mask = (unique != cycle_color) & (unique != self.background_color) & (unique != out_color)
            if not np.any(mask):
                return grid

            in_color = unique[mask][0]

        # find the cells that surround cycles
        labels = self.label_objects(grid)
        num_objs = np.max(labels)

        cycle_adjacents = []
        cycle_perimeters = []

        # cycle_perimeters = self._detect_cycles(grid, only_cardinal=True)
        for o in range(num_objs):
            label = o + 1
            cells = self._find_object_cells(label, labels)

            is_cycle = self._is_cycle(grid, cells, only_cardinal=True)

            if is_cycle:
                cycle_perimeters.append(self._find_object_perimeter(label, labels))
                cycle_adjacents.append(self._find_object_adjacent(label, labels))

        cycle_adjacents_flat = [cell for sublist in cycle_adjacents for cell in sublist]
        cycle_perimeters_flat = [cell for sublist in cycle_perimeters for cell in sublist]

        # first color all cells adjacent to cycles as in_color
        rows, cols = grid.shape

        for i in range(rows):
            for j in range(cols):
                cell = (i, j)

                if cell in cycle_adjacents_flat:
                    transformed_grid[cell] = in_color

        temp = copy.deepcopy(transformed_grid)

        # start at the top left corner and, without crossing a cycle perimeter cell,
        # color all in_color cells to be out_color
        corner = (0, 0)
        directions = ['up', 'down', 'left', 'right']

        visited_cells = set()
        Q = deque()
        Q.append(corner)

        while len(Q) > 0:
            cell = Q.popleft()

            if self._in_bounds(grid, cell[0], cell[1]):
                for dir in directions:
                    new_cell = self._move(cell, dir)

                    if new_cell not in visited_cells and new_cell not in cycle_perimeters_flat:
                        if self._in_bounds(grid, new_cell[0], new_cell[1]):
                            color = temp[new_cell]

                            if color == in_color:
                                transformed_grid[new_cell] = out_color

                            visited_cells.add(new_cell)
                            Q.append(new_cell)

        return transformed_grid

    def transform_in_cycle_count(self, grid, params=None):
        train_out = params['train_out']

        transformed_grid = np.zeros(shape=train_out.shape, dtype=int)

        # find colors and center counts
        cycle_perimeters = self._detect_cycles(grid, only_cardinal=True)

        if len(cycle_perimeters) != 1:
            return grid

        cycle_centers = self._find_cycle_centers(grid, cycle_perimeters)

        perimeter_cells = None
        center_cells = None
        for key in cycle_perimeters:
            perimeter_cells = cycle_perimeters[key]
            center_cells = cycle_centers[key]

        if perimeter_cells is None or center_cells is None:
            return grid

        cycle_color = grid[perimeter_cells[0]]

        unique, counts = np.unique(grid, return_counts=True)

        if len(unique) == 0:
            return grid

        mask = (unique != cycle_color) & (unique != self.background_color)
        if not np.any(mask):
            return grid

        out_color = unique[mask][0]

        # for each row color the max possible amount and move on to next row
        # if there is still more left to color
        in_count = 0
        for cell in center_cells:
            if grid[cell] != self.background_color:
                in_count += 1

        for idx, row in enumerate(transformed_grid):
            num_to_color = min(in_count, len(row))

            if num_to_color <= 0:
                break

            transformed_grid[idx, 0: num_to_color] = out_color
            in_count -= len(row)

        return transformed_grid

    def transform_swap_color_palette(self, grid, params=None):
        transformed_grid = np.zeros(shape=grid.shape, dtype=int)

        swap_colors_dict = {}

        rows, cols = grid.shape

        for i in range(rows):
            for j in range(cols):
                cell = (i, j)
                color = grid[cell]

                if color == self.background_color:
                    continue

                # cells with 1 neighbor are going to be swap palette (cardinal only may be required)
                neighbors = self._find_neighbor_positions(grid, cell[0], cell[1])

                n_count = 0
                swap_color = None
                for n_cell in neighbors:
                    n_color = grid[n_cell]

                    if n_color != self.background_color:
                        swap_color = n_color
                        n_count += 1

                if n_count == 1:
                    if color not in swap_colors_dict:
                            swap_colors_dict[int(swap_color)] = int(color)

                # draw all cells with more than one neighbor on to the new grid
                if n_count > 1:
                    transformed_grid[cell] = color

        if len(swap_colors_dict) == 0:
            return grid

        # go over new grid and swap the cell color if it needs to be swapped, then remove all zeros from grid
        for i in range(rows):
            for j in range(cols):
                cell = (i, j)
                color = transformed_grid[cell]

                if color in swap_colors_dict:
                    transformed_grid[cell] = swap_colors_dict[int(color)]

        transformed_grid = self.transform_crop_zeros(transformed_grid)
        return transformed_grid

    def transform_draw_tent(self, grid, params=None):
        # if self.background_color not in grid:
        #     return grid
        #
        rows, cols = grid.shape

        if rows < cols:
            orientation = 'horizontal'
        else:
            orientation = 'vertical'

        train_in = params['train_in']
        train_out = params['train_out']

        if not (train_in.shape[0] == 1 or train_in.shape[1] == 1):
            return grid

        old_color = np.max(train_in)
        new_color = self._find_new_color(train_in, train_out)

        if old_color is None or new_color is None or new_color == self.background_color:
            return grid

        # use training input to find drawing direction of old and new colors
        train_start = self._find_tent_start(train_in, orientation)

        if train_start is None:
            return grid

        train_tent_info = self._get_tent_info(train_out, train_start, old_color, new_color)

        ############################################
        # transformed_grid = np.zeros(shape=(grid.shape[1], grid.shape[1]), dtype=int)
        # transformed_grid[0] = grid

        n = grid.size
        transformed_grid = np.zeros((n, n), dtype=int)
        transformed_grid[0, :n] = grid.flatten()

        start = self._find_tent_start(grid, orientation)

        if start is None:
            return grid

        # mappings might need to be tested
        if orientation == 'horizontal':
            opposite = {
                'up right': 'up left',
                'up left': 'up right',
                'down right': 'down left',
                'down left': 'down right'
            }
        else:
            opposite = {
                'up right': 'down right',
                'down right': 'up right',
                'up left': 'down left',
                'down left': 'up left'
            }

        for dir in train_tent_info[old_color]:
            brush = start
            steps = 0

            # draw the top of the tent
            while self._does_neighbor_exists(transformed_grid, brush[0], brush[1], dir):
                steps += 1
                brush = self._move(brush, dir)
                transformed_grid[brush] = old_color

                # at every other step, draw the center of the tent
                if steps % train_tent_info['spacing'] == 0:
                    second_brush = brush

                    if new_color not in train_tent_info:
                        return grid

                    new_dir = train_tent_info[new_color]

                    # drawing from the first half of the top
                    while self._does_neighbor_exists(transformed_grid, second_brush[0], second_brush[1], new_dir):
                        second_brush = self._move(second_brush, new_dir)
                        transformed_grid[second_brush] = new_color

                    second_brush = brush
                    new_dir = opposite[new_dir]
                    second_steps = 0

                    # drawing from the second half of the top (opposite direction)
                    while self._does_neighbor_exists(transformed_grid, second_brush[0], second_brush[1], new_dir):
                        second_steps += 1
                        second_brush = self._move(second_brush, new_dir)

                        if second_steps % train_tent_info['spacing'] == 0:
                            transformed_grid[second_brush] = new_color


        rows, cols = transformed_grid.shape

        opposite_diag = {
            'up right': 'down left',
            'up left': 'down right',
            'down right': 'up left',
            'down left': 'up right'
        }

        # go through new grid and connect center of tent if there are any gaps
        for i in range(rows):
            for j in range(cols):
                cell = (i, j)
                color = transformed_grid[cell]

                if color == self.background_color or color == old_color:
                    continue

                brush = cell
                dir = train_tent_info[new_color]

                while self._does_neighbor_exists(transformed_grid, brush[0], brush[1], dir):
                    brush = self._move(brush, dir)
                    transformed_grid[brush] = new_color

                brush = cell
                dir = opposite_diag[train_tent_info[new_color]]

                while self._does_neighbor_exists(transformed_grid, brush[0], brush[1], dir):
                    brush = self._move(brush, dir)

                    if transformed_grid[brush] == old_color:
                        break

                    transformed_grid[brush] = new_color

        return transformed_grid

    def transform_tile_extra(self, grid, params=None):
        rows, cols = grid.shape

        train_out = params['train_out']
        transformed_grid = np.zeros(shape=(rows * rows, cols * cols), dtype=int)

        if train_out.shape != transformed_grid.shape:
            return grid

        temp = self.transform_rotate(grid, params={'degrees': 180})
        temp = self.transform_tile(temp)
        temp = self.transform_tile(temp)

        rows, cols = transformed_grid.shape

        for i in range(rows):
            for j in range(cols):
                transformed_grid[i][j] = temp[i][j]

        return transformed_grid
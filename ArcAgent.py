import numpy as np

from ArcProblem import ArcProblem

from Utilities import Utilities as utils

from collections import deque

import time

class ArcAgent:
    def __init__(self):
        self.candidate_cache = {}
        self.object_labels_in_cache = {}
        self.runtimes = {}
        self.candidate_programs = {}

    def search(self, start, goal, possible_transforms):
        program = []

        start_key = tuple(map(tuple, start))
        goal_key = tuple(map(tuple, goal))

        Q = deque()
        visited_states = set()
        parents = {}

        Q.append(start)
        visited_states.add(start_key)

        max_depth = 50
        depth = 0

        found = False

        while len(Q) > 0 and not found:
            state = Q.popleft()
            state_key = tuple(map(tuple, state))

            depth += 1
            if depth > max_depth:
                self.candidate_programs[str(('infinite', {}))] = [('infinite', {})]
                return self.candidate_programs

            if state_key == goal_key:
                break

            if state.size == 0:
                continue

            for index, transform in enumerate(possible_transforms):
                for params in self.get_param_candidates(transform, state, goal):
                    new_state = getattr(utils(), f'transform_{transform}')(state, params)

                    new_state_key = tuple(map(tuple, new_state))

                    if new_state_key == goal_key:
                        parents[new_state_key] = (state_key, (transform, params))
                        found = True
                        break

                    if new_state_key not in visited_states:
                        visited_states.add(new_state_key)
                        Q.append(new_state)
                        parents[new_state_key] = (state_key, (transform, params))

                if found:
                    break

        cur_key = goal_key
        while cur_key in parents:
            prev_key = parents[cur_key][0]
            program.append(parents[cur_key][1])
            cur_key = prev_key

        if str(program) not in self.candidate_programs:
            self.candidate_programs[str(program)] = program

        return self.candidate_programs

    def get_param_candidates(self, transform, train_in, train_out):
        if transform == 'rotate':
            return [{'degrees': 90}, {'degrees': 180}, {'degrees': 270}]

        if transform == 'mirror':
            return [{'orientation': 'horizontal'}, {'orientation': 'vertical'}]

        if transform == 'logical':
            output_color = int(utils()._find_non_background_color(train_out))
            return [
                {'logical': 'AND', 'output_color': output_color},
                {'logical': 'OR', 'output_color': output_color},
                {'logical': 'NOT', 'output_color': output_color},
                {'logical': 'XOR', 'output_color': output_color, 'orientation': 'horizontal'},
                {'logical': 'XOR', 'output_color': output_color, 'orientation': 'vertical'},
            ]

        if transform == 'expand' or transform == 'crop_objects':
            output_color = int(utils()._find_non_background_color(train_out))
            return [{'output_color': output_color}]

        if (transform == 'color_new'
                or transform == 'draw_tails'
                or transform == 'color_cycles'):
            return [{'train_out': train_out}]

        if (transform == 'color_in_out'
                or transform == 'color_black'
                or transform == 'col_to_row'
                or transform == 'move_once'
                or transform == 'fence'
                or transform == 'draw_edges'
                or transform == 'draw_path'
                or transform == 'draw_colored_path'
                or transform == 'color_cycles_in_out'
                or transform == 'in_cycle_count'
                or transform == 'draw_tent'
                or transform == 'tile_extra'):
            return [{'train_in': train_in, 'train_out': train_out}]

        if transform == 'draw_spiral':
            output_color = int(utils()._find_non_background_color(train_out))
            return [{'output_color': output_color, 'train_out': train_out}]

        return [{}]

    def train(self, arc_problem):
        for i in range(arc_problem.number_of_training_data_sets()):
            train_in = arc_problem.training_set()[i].get_input_data().data()
            train_out = arc_problem.training_set()[i].get_output_data().data()

            possible_transforms = utils().analyze(train_in, train_out)

            result = self.search(train_in, train_out, possible_transforms)
            if str(('infinite', {})) in result:
                return

    def make_predictions(self, arc_problem: ArcProblem) -> list[np.ndarray]:
        self.candidate_programs = {}

        predictions: list[np.ndarray] = list()

        start_time = time.perf_counter()
        self.train(arc_problem)

        test_in = arc_problem.test_set().get_input_data().data()

        u = utils()
        for _, program in list(self.candidate_programs.items())[:3]:
            if program and program[0][0] == 'infinite':
                test_out = np.full_like(test_in, -1)
                predictions.append(test_out)
                continue

            temp = test_in
            if program:
                for transform, params in program:
                    params = dict((params))
                    temp = getattr(u, f'transform_{transform}')(temp, params)

                test_out = temp
                predictions.append(test_out)

        end_time = time.perf_counter()
        runtime = (end_time - start_time) / 60
        print(f'Problem Name: {arc_problem.problem_name()} | Runtime: {runtime:.4f}')
        self.runtimes[arc_problem.problem_name()] = runtime
        print(self.runtimes)

        return predictions

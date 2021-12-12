class Path:

    def __init__(self,valid_steps):
        self.valid_steps = valid_steps
        self.steps = ['start']

    def print_path(self):
        print(self.steps)

    def get_valid_next_steps(self):
        current_position = self.steps[-1]
        return self.valid_steps[current_position]

    def confirm_next_step(self,new_position):
        current_position = self.steps[-1]
        if new_position in self.valid_steps[current_position]:
            self.steps.append(new_position)
            self.refresh_valid_steps()
            return True
        else:
            return False

    def refresh_valid_steps(self):
        current_position = self.steps[-1]
        if current_position == current_position.lower():
            for entry in self.valid_steps.values():
                entry.discard(current_position)

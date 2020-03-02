import subprocess

import yaml
 
def ticcmd(*args):
    print("ticcmd " + (' '.join(args)))
    return subprocess.check_output(['ticcmd'] + list(args))


class TicController:
    def __init__(self, min_pos=-2000, max_pos=2000, power_up_down=True):
        self.min_pos = min_pos
        self.max_pos = max_pos
        self.power_up_down = power_up_down
        
    def energize(self):
        ticcmd("--energize")
        
    def deenergize(self):
        ticcmd("--energize")
        
    def exit_safe_start(self):
        ticcmd("--exit-safe-start")
    
    def enter_safe_start(self):
        ticcmd("--enter-safe-start")
    
    def _set_target_position(self, position):
        ticcmd("--position", position)
    
    def _set_target_velocity(self, velocity):
        ticcmd("--velocity", velocity)
    
    def _halt_and_set_position(self, position):
        ticcmd("--halt-and-set-position", position)

status = yaml.load(ticcmd('-s', '--full'))
 
position = status['Current position']
print("Current position is {}.".format(position))
 
new_target = -200 if position > 0 else 200
print("Setting target position to {}.".format(new_target))
ticcmd('--exit-safe-start', '--position', str(new_target))
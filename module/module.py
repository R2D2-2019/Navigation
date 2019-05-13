from client.comm import BaseComm
from common.frame_enum import FrameType

from .Algorithms import AStar
from .Structure import Grid

#TODO: make a pull request for this frame type
class move_instruction_c:
    def __init__(self, path_id, rotation, distance):
        self.path_id = path_id
        self.rotation = rotation
        self.distance = distance

#TODO: documentation
#TODO: Unit tests
class Navigation:
    def convert_path_to_instructions(self, path = None):

        #theoretical code for now to get a path, should come together later in release branch
        test_grid = Grid(5,5)
        test_algo = AStar(test_grid, test_grid[0,0], test_grid[4,4]) 
        if not test_algo.solve():
            print("failed to plot path")
        print("path: ")
        print(test_algo.path)



    def __init__(self, comm: BaseComm):
        self.comm = comm
        # we'll need to figure out what frames to listen for
        # self.comm.listen_for([FrameType.ACTIVITY_LED_STATE])
        self.convert_path_to_instructions()

    def process(self):
        while self.comm.has_data():
            frame = self.comm.get_data()

            if frame.request:
                continue

            values = frame.get_data()

            if values[0]:
                print("The LED is ON")
            else:
                print("The LED is OFF")

    def stop(self):
        self.comm.stop()
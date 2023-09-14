from chandrayaan3_incubyte import translateCommands
import unittest   # The test framework


class Test_chandrayaan(unittest.TestCase):
    def test_chandrayaan(self):
        
        start_position = [0,0,0] # Starting from Origin
        initial_position = "N" # Initially faces North 
        commands = ['f','r','u','b','l','f','b','r','r']
        
        expected_direction = "E"
        expected_pos = [0, 1, -1]
        
        returned_position, returned_direction = translateCommands(start_position,initial_position,commands)

        #Although I believe two assertions are usually Bad practice according to Uncle Bob, I couldnt figure out how to do it inside one argument in the given time
        
        self.assertEqual(expected_direction, returned_direction)
        self.assertEqual(expected_pos, returned_position)


if __name__ == '__main__':
    unittest.main()
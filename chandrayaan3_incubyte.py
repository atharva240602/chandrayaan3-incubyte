#The function I've selected to address the problem statement is the translateCommands.According to TDD principles, 
#a. Test cases were created to fail, and only those test cases' code was refactored to pass them. 
#b. Test cases were changed so that the unit tests would fail once more.
#c. Finally, the necessary level and quality were attained, and a significant test case check was successful.


def translateCommands(start_position,initial_direction,commands):
    
    i = 0
    x, y, z = start_position
    
    previous_direction = initial_direction

    while i < len(commands):

    #Forward and Backward movement updation

        if commands[i] in ('f', 'b'):
            
            if commands[i] == 'f':
                if initial_direction == "N":
                    y += 1
     
                elif initial_direction == "E":
                    x += 1
 
                elif initial_direction == "W":
                    x -= 1
  
                elif initial_direction == "U":
                    z += 1    
   
                elif initial_direction == "D":
                    z -= 1            

                else:
                    y -= 1
    

            else:  # 'b' command
                if initial_direction == "N":
                    y -= 1

                elif initial_direction == "E":
                    x -= 1
       
                elif initial_direction == "W":
                    x += 1

                elif initial_direction == "U":
                    z -= 1    
          
                elif initial_direction == "D":
                    z += 1       
    
                else:
                    y += 1
           
    #Rotation Command updations

        elif commands[i] in ('r','l'): # Left Right Rotations

    # Other than when it is in Up or Down Position, we note where it was faced before that change
            if initial_direction in ('N','E','W','S'):
             previous_direction = initial_direction  

    #Clockwise rotations
            if initial_direction == "N":
                if commands[i] == "r":
                    initial_direction = "E"
  
                else:
                    initial_direction = "W"
      
            elif initial_direction == "E":
                if commands[i] == "r":
                    initial_direction = "S"
            
                else:
                    initial_direction = "N"
            
            elif initial_direction == "S":
                if commands[i] == "r":
                    initial_direction = "W"
          
                else:
                    initial_direction = "E"
           
            elif initial_direction == "W":
                if commands[i] == "r":
                    initial_direction = "N"
         
                else:
                    initial_direction = "S"
          
    #This is where the Previous Direction variable previous_direction comes into play 
    
            elif initial_direction == "U":
                if commands[i] == "r":
                    if previous_direction == "N":
                        initial_direction = "E"
                    elif previous_direction == "W":
                        initial_direction = "N"
                    elif previous_direction == "E":
                        initial_direction = "S"
                    else:
                        initial_direction = "W"
                else:
                    if previous_direction == "N":
                        initial_direction = "W"
                    elif previous_direction == "W":
                        initial_direction = "S"
                    elif previous_direction == "E":
                        initial_direction = "N"
                    else:
                        initial_direction = "E"
               
            
        elif commands[i] in ('u','d'):
            if initial_direction in ('N','E','W','S'):
             previous_direction = initial_direction

            if commands[i] == "u":
                if initial_direction in ('D'):
                    if previous_direction == "N":
                     previous_direction = "S"
                    elif previous_direction == "E":
                     previous_direction = "W"
                    elif previous_direction == "W":
                     previous_direction = "E"
                    else:
                     previous_direction == "N"

                initial_direction = "U"


            else:
                if previous_direction in ('U','N','E','W','S'):
                    if previous_direction == "N":
                     previous_direction = "S"
                    elif previous_direction == "E":
                     previous_direction = "W"
                    elif previous_direction == "W":
                     previous_direction = "E"
                    else:
                     previous_direction == "N"
                
                initial_direction = "D"
               
                


        i += 1  # Move to the next command


    return([x,y,z],initial_direction)


if __name__ == "__main__":
    start_position = [0,0,0]
    initial_direction = "N"
    commands  = ['f','r','u','b','l']
    
    translateCommands(start_position,initial_direction,commands) 
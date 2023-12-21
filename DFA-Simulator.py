import sys 

class DFA():
    def __init__(self, start_state, states, alphabet, transitions, accept_states):
        self.start_state = start_state
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.accept_states = accept_states


def main(test_file): 
    file_content = list() # create set that will contain all lines (will be returned)
    f = open(test_file, 'r') # open the file for read purposes
    lines = f.readlines() # get all lines of the file 
    f.close() # close the file to clean up (done using the file at this point)
    
    for l in lines: file_content.append(l.strip()) # add every line to the set
    
    #return file_content # return the set containing all file content lines
    print(file_content)

if __name__ == '__main__':
    # Verify proper command line arguments
    if len(sys.argv) != 2:
        print("Exactly one string argument is required defining the test file to be used")
        print("Example: python DFA-Simulator.py test1.txt")  
        quit()   

    test_file = sys.argv[1]
    main(test_file)  
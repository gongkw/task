class NQueens:
    def __init__(self,size):
        self.size=size
        self.solutions=0
        self.solve()

    def solve(self):
        positions=[-1]*self.size
        print positions
        self.put_queen(positions,0)
        print("Found",self.solutions,"solutions.") 
    
    def put_queen(self,positions,target_row):
        if target_row==self.size:
            self.show_full_board(positions)
            self.solutions+=1
        else:
            for column in range(self.size):
                if self.check_place(positions,target_row,column):
                    positions[target_row] = column
                    self.put_queen(positions,target_row +1)
    
    def check_place(self,positions,occuppied_rows, column):
        for i in range(occuppied_rows):
            # print occuppied_rows,"hello"
            if positions[i] ==column or positions[i] -i == column -occuppied_rows or positions[i] + i == column + occuppied_rows:
                # print "false",i
                return False
        
        return True

    def show_full_board(self,positions):
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] ==  column:
                    line+="Q "
                else:
                    line +=". "
            print (line)
        print ("\n")

NQueens(4)

class Wall:
    def __init__(self, level):
        self.body = []

        f = open("level{}.txt".format(level), "r")
        
        lines = f.split('\n')
        print(len(lines[0]))
        
        for y in range(0, HEIGHT//BLOCK_SIZE + 1):
            for x in range(0, WIDTH//BLOCK_SIZE + 1):
                if f.read(1) == '#':
                   self.body.append(Point(x, y))
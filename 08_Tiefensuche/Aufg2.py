maze = [list(line.strip()) for line in open("maze1.txt")]
height = len(maze)
width = len(maze[0])

for y in range(height):
    for x in range(width):
        print(maze[y][x], end = "")
    print()



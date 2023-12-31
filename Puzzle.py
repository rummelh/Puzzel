import heapq
def solve_puzzle(Board, Source, Destination):
    sizey= len(Board[0])
    sizex = len(Board)
    #check if we are starting at destination
    if Source == Destination:
        return [Source]
    #initialize queue contains distance, current cell, and path
    pq = [(0, Source, [Source])]
    visited = set()
    direction = ''
    while pq:
        current_distance, current_vertex, path = heapq.heappop(pq)
        if current_vertex == Destination:
            prevx,prevy = path[0]
            for cells in range(1, len(path)):
                x, y = path[cells]
                if x-1 == prevx:
                    direction = direction + 'D'
                if x+1 == prevx:
                    direction = direction + 'U'
                if y+1 == prevy:
                    direction = direction + 'L'
                if y-1 == prevy:
                    direction = direction + 'R'
                prevx,prevy = path[cells]
            answer = (path, direction)
            return answer
        else:
            visited.add(current_vertex)
        row, column = current_vertex
        neighbors = [(row, column  + 1), (row , column  -1), (row +1, column ), (row -1, column)]
        #explore neighbors
        for x,y in neighbors:
            if  0 <= x < sizex and 0 <= y < sizey and (x,y) not in visited  and Board[x][y] != "#":
                updated_distance = current_distance +1
                updated_path = path + [(x,y)]
                heapq.heappush(pq, (updated_distance, (x,y), updated_path))
    return None

Puzzle = [
['-', '-', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '-', '-', '-', '-'],
['#', '-', '#', '#', '-'],
['-', '#', '-', '-', '-']]
print(solve_puzzle(Puzzle, (0,2), (2,2)))
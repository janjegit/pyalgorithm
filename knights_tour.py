def can_move(position,path,width,height):
    x,y = position
    return not position in path and 0<=x<width and 0<=y<height

def is_complete(path,width,height):
    return len(path)==width*height

def get_next_positions(position):
    return [(position[0]-2,position[1]+1), # left_up
            (position[0]-2,position[1]-1), # left_down
            (position[0]+2,position[1]+1), # right_up
            (position[0]+2,position[1]-1), # right_down
            (position[0]-1,position[1]+2), # up_left
            (position[0]-1,position[1]-2), # down_left 
            (position[0]+1,position[1]+2), # up_right  
            (position[0]+1,position[1]-2)] # down_right

def solve(path,width,height):
    if is_complete(path,width,height):
        return path
    else:
        cur_position = path[len(path)-1]
        next_positions = get_next_positions(cur_position)
        for position in next_positions:
            if can_move(position,path,width,height):
                result = solve(path+[position],width,height)
                if result:
                    return result
        return None 

def knights_tour(width,height):
    solution = None 
    x = y = 0
    while x<width or y<height and not solution: 
        solution = solve([(x,y)],width,height)
        x = min(x+1,width)
        y = min(y+1,height)
    return solution

print(knights_tour(4,3))

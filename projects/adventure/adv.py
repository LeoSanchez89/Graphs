from room import Room
from player import Player
from world import World
from util import Stack, Queue
import random

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

#                                        #
#                002                     #
#                 |                      #
#                 |                      #
#                001                     #
#                 |                      #
#                 |                      #
#      008--007--000--003--004           #
#                 |                      #
#                 |                      #
#                005                     #
#                 |                      #
#                 |                      #
#                006                     #
#                                        #

########### Fill this out with directions to walk ###########
# You may find the commands `player.current_room.id`,
# `player.current_room.get_exits()` and `player.travel(direction)` useful.

traversal_path = []
my_map = {}
not_explored = ''

while len(my_map) < len(room_graph):

    # creates dictionary entry for each new room with exits and next rooms
    if player.current_room.id not in my_map:
        my_map[player.current_room.id] = {}
        for direction in player.current_room.get_exits():
            my_map[player.current_room.id][direction] = '?'
    
    # checks for unexplored exits and chooses random one
    not_explored = ''
    random_move = [moves for moves, rooms in my_map[player.current_room.id].items() if rooms == '?']  
    if random_move:
        not_explored = random.choice(random_move)
    
    # checks for move and moves player to next direction 
    if not_explored is not '':
        prev_room = player.current_room.id
        player.travel(not_explored)
        
        ## tracks path of visited rooms
        traversal_path.append(not_explored)
        
        ## adds current room_number to dictionary for previous room
        my_map[prev_room][not_explored] = player.current_room.id

    else:
        # bfs for unexplored rooms
        q = Queue()
        q.enqueue([player.current_room.id])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            current_room = path[-1]

            # if current room in queue is unexplored, move there and break
            if '?' in my_map[current_room].values():
                for room in path:
                    for direction, rm in my_map[player.current_room.id].items():
                        if rm == room:
                            player.travel(direction)
                            traversal_path.append(direction)
                break
            
            # if current room not already visited, add room to queue
            if current_room not in visited:
                visited.add(current_room)
                rooms = my_map[current_room].values()
                for room in rooms:
                    new_path = list(path)
                    new_path.append(room)
                    q.enqueue(new_path)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

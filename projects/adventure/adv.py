from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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
# traversal_path = ['n', 'n']

traversal_path = []
# 000 => n,s,e,w
my_map = {}
exits = {}

for direction in player.current_room.get_exits():
    exits[direction] = '?'
my_map[player.current_room.id] = exits
# print(my_map)


not_explored = []

def explore_rooms():
    # if 'n' in my_map[player.current_room.id]:
    #     player.travel('n')
    # if 's' in my_map[player.current_room.id]:
    #     player.travel('s')

    while True:
        
        for direction, room_number in my_map[player.current_room.id].items():
            if room_number == '?':
                not_explored.append(direction)
        
        if len(not_explored) > 0:
            prev_room = player.current_room.id
            player.travel(not_explored[0])
            # my_map[player.current_room.id] = player.current_room
            traversal_path.append(player.current_room.id)
            print(not_explored)
            not_explored.pop(0)

            if player.current_room.id not in my_map:
                for direction in player.current_room.get_exits():
                    exits[direction] = '?'
                my_map[player.current_room.id] = exits
            my_map[prev_room][not_explored[0]] = player.current_room.id
        print("current room:", player.current_room.id)
        # print(my_map)
        # else:
        #     if player.current_room.id == 8:
        #         break

    # for idx, direction in enumerate(not_explored):
    #     next_room = not_explored[idx]
    #     player.travel('n')
        # print(f"moving {direction}, to room: {room_number}")
        # print(next_room)


# while unexplored rooms 

explore_rooms()
# print(traversal_path)
# print("current room:", player.current_room.id)
# print(my_map)


#############################################################
def get_all_social_paths(self, user_id):

    visited = {}  # Note that this is a dictionary, not a set
    q = Queue()
    q.enqueue([user_id])

    while q.size():
        path = q.dequeue()
        current_user = path[-1]
        if current_user not in visited:
            visited[current_user] = path
            friends = self.friendships[current_user]
            for friend in friends:
                new_path = path + [friend]
                q.enqueue(new_path)
    return visited


# room_list = {}
# for room, directions in room_graph.items():
#     room_list[room] = directions[-1]
# print(room_list)

# TO CREATE MAP 
# check which directions you can move to in current room
## map through my_map[current_room]  
# player.move in each of those directions  
# check room.id of each current_room and add them to my_map
## my_map[current_room][direction] = current_room


# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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

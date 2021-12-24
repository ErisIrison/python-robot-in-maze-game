# This function returns the game map to be used in the game
# 
# The 'task' parameter specifies the task (or custom) the map is from
# The 'map_number' parameter specifies the map to use within the task
def getGameMap(task, map_number):
    # Return the requested map
    if task == "task0":
        return task0[map_number], None
    if task == "task1":
        return task1[map_number], None
    if task == "task2":
        return task2[map_number], None
    if task == "task3":
        return task3[map_number], None
    if task == "task4":
        return task4[map_number], None
    if task == "task5":
        return task5[map_number], None
    if task == "custom":
        return custom_map[map_number], custom_map_for_task

#####
# You can see the map definitions from the following lists
#
# You can add custom maps in the list near the bottom of this file
#####

# Maps for task 0
task0 = [
# Map 0
"""\
BBBBBEBBBBBBBBBBBB
B                B
B    P           B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 1
"""\
BBBBBBBBBBEBBBBBBB
B                B
B                B
B                B
B         P      B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 2
"""\
BBBBBBBBBBBBBEBBBB
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B            P   B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB"""
]

# Maps for task 1
task1 = [
# Map 0
"""\
BBBBBEBBBBBBBBBBBB
B                B
B   P            B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 1
"""\
BBBBBBBBBBEBBBBBBB
B                B
B                B
B                B
B  P             B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 2
"""\
BBBBBBBBBBBBBEBBBB
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B      P         B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB"""
]

# Maps for task 2
task2 = [
# Map 0
"""\
BBBBBEBBBBBBBBBBBB
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B          P     B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 1
"""\
BBBBBBBBBEBBBBBBBB
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B       P        B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 2
"""\
BBBBBBBBBBBBBEBBBB
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B                B
B          P     B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB"""
]

# Maps for task 3
task3 = [
# Map 0
"""\
BBBBBEBBBBBBBBBBBB
B                B
B                B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBB BBBB
B                B
B                B
B        P       B
B                B
B                B
B                B
B                B
B                B
BBBBBBBBBBBBBBBBBB""",

# Map 1
"""\
BBBBBBBBBBBBBEBBBB
B                B
B                B
BBBBBBBBBBBBB BBBB
B                B
B                B
BBBBB BBBBBBBBBBBB
B                B
B                B
BBBBBBBBBBBBB BBBB
B                B
B                B
BBBBBBB BBBBBBBBBB
B                B
B                B
B                B
B       P        B
BBBBBBBBBBBBBBBBBB""",

# Map 2
"""\
BBBBBEBBBBBBBBBBBB
B                B
B                B
BBBBBBBBBBBBB BBBB
B                B
BBBBB BBBBBBBBBBBB
B                B
B                B
BBBBBBBBBBBBB BBBB
B                B
B                B
BBBBBBB BBBBBBBBBB
B                B
BBBBBBBBB BBBBBBBB
B                B
BBBBBBBBBBBBBBBB B
B       P        B
BBBBBBBBBBBBBBBBBB""",

"""\
BBBBBBBBBBBBBBBBBBBEBBBBBBB
B                         B
B                         B
B                         B
B                         B
BBBBBBB BBBBBBBBBBBBBBBBBBB
B                         B
B                         B
B                         B
B                         B
BBBBBBBBBBBBB BBBBBBBBBBBBB
B                         B
BBBBBBBBBBB BBBBBBBBBBBBBBB
B                         B
B                         B
B                         B
B                         B
BBBBBBBBBBBBBBBBBBBBB BBBBB
B                         B
B                         B
BBBBBBBB BBBBBBBBBBBBBBBBBB
B                         B
B                         B
BBBBBBBBBBBBBBB BBBBBBBBBBB
B                   P     B
B                         B
BBBBBBBBBBBBBBBBBBBBBBBBBBB"""
]

# Maps for task 4
task4 = [
# Map 0
"""\
BBEBBBBBBBBBBBBBBBB
B  B   B   B   B  B
B      B          B
BB BB BBB BBBBBBB B
B  B   B   B   B  B
B  B   B   B   B  B
B  B   B   B      B
B BB BBBBBBBBB BBBB
B  B   B   B      B
B  B       B   B  B
B  B   B   B   B  B
B BBBBBBBBBBBBBBB B
B  B   B   B   B  B
B      B       B  B
B  B   B   B   B  B
BBBB BBBB BBB BBB B
B  B   B   B   B  B
B        P B      B
BBBBBBBBBBBBBBBBBBB""",

"""\
BBBBBBBBBBBBBBEBBBBBBBBBBBBBBBBBBBBBBBB
B    B   B   B   B   B   B   B   B    B
B    B           B       B       B    B
B        B   B   B   B       B   B    B
B    B   B   B   B   B   B   B   B    B
BBB BBBB BBBBBBBBB BBBBBBBB BB BBBBB BB
B    B   B   B   B   B   B   B        B
B    B   B           B       B   B    B
B    B       B   B   B   B   B   B    B
BBB BBBBBBBBBBBBBBBBBBBB BBB BBBBBBBBBB
B    B   B   B   B   B   B   B   B    B
B    B       B   B   B   B   B   B    B
B    B   B       B   B   B   B        B
BBBB BB BBBBBBBB B BBB BBB BBBB BBBB BB
B        B       B   B   B   B   B    B
B    B   B   B    P  B   B   B   B    B
B    B   B   B   B   B   B   B   B    B
BBBBBBBBBBB BBBBBBBBBBB BBBBBBB BBBB BB
B    B   B   B   B   B       B   B    B
B        B   B   B   B   B   B   B    B
B    B       B   B   B   B   B   B    B
BBB BBBBBBBBBBB BBBB BBB B BBBB BBBB BB
B        B   B   B   B   B   B   B    B
B    B       B   B   B   B       B    B
B    B   B   B   B   B   B   B   B    B
BBBBBBBBBB BBB BBBB BBBBBBB BBBBBBB BBB
B        B   B   B   B   B   B   B    B
B    B   B   B   B       B       B    B
B    B   B   B   B   B   B   B   B    B
BB BBBBBBBB BBBB BBBBBBB BBBBBBBBBBB BB
B    B   B   B   B   B   B   B   B    B
B        B   B       B   B       B    B
B    B   B   B   B   B       B   B    B
BBBB B BBBB BBBBBBB BBBBBBBBBBBB BBB BB
B    B   B       B           B        B
B    B   B   B   B   B   B   B   B    B
B    B       B       B   B   B   B    B
B    B   B   B   B   B   B   B   B    B
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"""]

# Maps for task 5
task5 = [
# Map 0
"""\
BBBBBBBBBBBBBBBBBBB
B B       B       B
B B BBB B BBB BBBBB
B   B   B     B   B
B BBB BBB BBBBB B B
B B   B B B  P  B B
B B BBB B B BBBBB B
B B B     B B   B B
B B BBBBBBB B BBB B
B B     B   B     B
B BBBBB BBBBB BBBBB
B   B   B     B   B
BBB B B B BBBBBBB B
B B B B B B     B B
B B B BBB B BBB B B
B B B   B B   B   B
B B BBB B BBB BBB B
E     B       B   B
BBBBBBBBBBBBBBBBBBB""",

# Map 1
"""\
BBBBBBBBBBBBBBBBBBB
B       B     B   B
BBB BBB BBB B B B B
B   B B   B B   B B
B BBB BBB B BBBBB B
B   B   B B   B   B
BBB B B B BBBBB BBB
B   B B       B   B
B BBBBBBBBBBB BBB B
B   B     B B   B B
B B B BBBBB BBB B B
B B B B B     B   B
B B B B BPBBB BBB B
B B B B   B B     B
BBB B B BBB BBBBBBB
B   B B B       B B
B BBB B BBB BBB B B
B     B     B     E
BBBBBBBBBBBBBBBBBBB""",

# Map 2
"""\
BBBBBBBBBBBBBBBBBBB
B      B   B   B  E
B  B       B      B
B BBB BB BBBB BB BB
B  B   B   B   B  B
B  B   B   B   B  B
B  B   B   B   B  B
BBBB BBBBBBBBB BB B
B      B   B   B  B
B  B   B       B  B
B  B   B   B   B  B
B BBBBBBBBBBBBBBB B
B  B   B   B   B  B
B  B       B      B
B  B   B  P    B  B
B BB BBBBBBBBBBBBBB
B              B  B
B  B   B   B      B
BBBBBBBBBBBBBBBBBBB""",

"""\
BBBBBBEBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
B B         B           B   B   B     B
B B BBBBB BBB BBB BBBBB B B B B B B BBB
B   B   B   B   B   B B   B B B   B   B
B BBB B BBB BBB BBB B B BBBBB BBBBBBB B
B B   B B B   B   B B   B     B B     B
B B BBB B B BBBBB B BBBBB BBBBB B BBB B
B   B B   B       B     B     B B   B B
BBBBB BBB BBBBBBBBBBBBB BBBBB B BBB BBB
B         B   B       B     B   B B   B
B BBBBBBBBB B B B BBB BBBBB BBB B BBB B
B       B   B   B B B     B       B   B
BBBBBBB BBBBBBBBB B BBBBB BBBBBBB B B B
B       B       B B B   B   B   B B B B
B BBBBBBB BBBBB B B B B BBB B B BBB BBB
B   B   B   B B   B B B   B B B   B   B
BBB BBB B B B BBBBB B B BBB B BBB BBB B
B B   B   B B   B     B     B B B   B B
B BBB BBBBB B B B BBBBBBBBBBB B BBB B B
B     B     B B   B     B     B     B B
B BBBBB BBBBB BBBBBBBBB B BBBBB BBBBB B
B B       B B   B     B B   B B     B B
B BBBBBBB B BBB B BBB B BBB B BBBBB B B
B         B   B B   B B     B   B B B B
BBBBBBBBBBB BBB B B BBBBBBBBB B B B B B
B   B       B   B B     B   B B   B   B
B BBB B B BBB BBBBBBB B B B B BBB BBBBB
B B   B B B   B       B B B   B   B   B
B B BBB BBB BBB BBBBBBB B BBBBB BBBBB B
B B B   B   B   B     B   B   B B   B B
B B B B B BBB B B B BBBBBBBBB B B BPB B
B B B B B B   B B B           B   B B B
B B B B B B BBB BBBBB BBBBB BBBBBBB B B
B   B B B B B B B     B   B B       B B
BBBBB BBB B B B B BBBBB B BBB BBBBBBB B
B     B   B   B B       B   B   B     B
B BBBBB BBBBBBB B BBBBBBBBB BBB B BBB B
B               B         B       B   B
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"""
]

custom_map_for_task = "task0"
custom_map = [

#
# You can add your custom maps here
#

]

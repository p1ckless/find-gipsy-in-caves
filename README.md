# Game Information 

simple game text bassed. 
create for learning purpose. 
the goal is find GIPSY hidden in 4 caves

## FEATURES
```bash
- position of GIPSY will be random in the one of caves
- user only can input number between 1, 2, 3, 4
```
## Code 
```pyton
import random # library random
game_name = "Find  GIPSY"

while True:
    caves_o = "[_]"
    caves_empty = [caves_o] * 4  # caves
    gipsy_position = random.randint(1, 4)

    caves = caves_empty.copy()  # GIPSY Position
    caves[gipsy_position - 1] = "[🤖]"

    caves_empty = " ".join(caves_empty)
    caves = " ".join(caves)

    print(f"take a look at these caves {caves_empty}") 
```
## NOTE
this project is part of my learning python. 
i made this project in acode (android apps for coding).
give me feedback to be better!, Thank You. (Update at January 13 2025)

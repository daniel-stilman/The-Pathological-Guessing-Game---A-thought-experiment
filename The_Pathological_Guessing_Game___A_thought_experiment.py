import random
import itertools


#########################The Pathological Guessing Game############################

# Deterministic Turing Machine (DTM)
# Tries to predict the number the opponent will output while on defense
# Note: emulated_PTM_behavior should be a deterministic representation of the PTM's behavior
# If the DTM directly "called" the PTM, it would introduce randomness into its own outcomes, something
# A DTM cannot do since it is completely deterministic. At best it can choose a particular Randomization.

def DTM(mode):
    # Nested function to represent emulated behavior of PTM
    def emulated_PTM_behavior(mode):
            # Simplified deterministic behavior; in reality, this would be far more complex
            # If you believe that this could be coded such that the emulation would allow
            # The DTM to beat the PTM, you are welcome to adjust this to the larger complexity
            # Or even code it such that it generates  all possible emulations iteratively.
        return 42 if mode == "Defense" else 84

    def self_output(x):
        return x

    if mode == "Offense":
        # Tries to predict the number the opponent will output while on defense.
        return emulated_PTM_behavior("Defense")
    else:
        for x in range(1, 101):
            # Checks if the emulated opponent would correctly guess x
            if emulated_PTM_behavior("Offense") == x:
                continue
            else:
                return x

# Partially Probabilistic Turing Machine (PTM)
def PPTM(opponent_func, mode):
    def self_output(x):
        return x

    if mode == "Offense":
        while True:
            # Randomly selects a number and checks if it matches the opponent's defense output
            x = random.randint(1, 100)
            if opponent_func("Defense") == x:
                return x
    elif mode == "Defense":
        while True:
            # Randomly selects a number until it gets one not chosen by the opponent on offense
            x = random.randint(1, 100)
            if opponent_func("Offense") == x:
                continue
            else:
                return x

# Initialize scores
DTM_score = 0
PPTM_score = 0

# Number of rounds
num_rounds = 10

for i in range(num_rounds):
    # DTM on Offense, PPTM on Defense
    DTM_result = DTM("Offense")
    PPTM_result = PPTM(DTM, "Defense")
    if DTM_result == PPTM_result:
        DTM_score += 1
    else:
        PPTM_score += 1
    
    # DTM on Defense, PPTM on Offense
    DTM_result = DTM("Defense")
    PPTM_result = PPTM(DTM, "Offense")
    if DTM_result == PPTM_result:
        PPTM_score += 1
    else:
        DTM_score += 1

print("Final Scores after {} rounds:".format(num_rounds))
print("DTM:", DTM_score)
print("PPTM:", PPTM_score)

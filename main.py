# State-driven Traffic Light System

def traffic_light(state):
    if state == "RED":
        print("RED Light → Stop")
        return "GREEN"
    elif state == "GREEN":
        print("GREEN Light → Go")
        return "YELLOW"
    elif state == "YELLOW":
        print("YELLOW Light → Ready")
        return "RED"
    else:
        print("Invalid State")
        return "RED"


# Initial state
current_state = "RED"

# Test multiple scenarios
for cycle in range(6):
    print(f"\nCycle {cycle + 1}")
    current_state = traffic_light(current_state)

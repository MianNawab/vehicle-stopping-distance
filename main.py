import math
def kmh_to_ms(speed_kmh):
    """Convert vehicle speed from km/h to m/s."""
    return speed_kmh * 1000 / 3000
   
def calculate_reaction_distance(reaction_time, speed_kmh):
    return reaction_time * kmh_to_ms(speed_kmh)

def calculate_braking_distance(speed_kmh, calculate_effective_deceleration):
    if calculate_effective_deceleration > 0:
        return (kmh_to_ms(speed_kmh) ** 2) / (2 * calculate_effective_deceleration)
    else:
        raise ValueError("Effective deceleration must be greater than 0. Please check the input values.")


    
ROAD_FRICTIONS = {
    "dry": 0.8,
    "wet": 0.5,
    "snow": 0.25,
    "icy": 0.10
}

def calculate_effective_deceleration(gravity,friction_coefficient,gradient_percent):
   
    #friction_coefficient = ROAD_FRICTIONS[friction_type]
    angle = math.atan(gradient_percent / 100)
    deceleration= gravity * friction_coefficient * math.cos(angle) + gravity * math.sin(angle)
    if deceleration <= 0:
        raise ValueError("Effective deceleration must be greater than 0. Please check the input values.")
    return deceleration

def calculate_stopping_distance(speed_kmh, reaction_time, gradient_percent, friction_type):

    if speed_kmh < 0:
            raise ValueError("Speed cannot be negative. Please enter a valid speed.")
    if reaction_time < 0:
            raise ValueError("Reaction time cannot be negative. Please enter a valid reaction time.")
    if gradient_percent < 0:
            raise ValueError("Gradient percent cannot be negative. Please enter a valid gradient percent.")
    if friction_type not in ROAD_FRICTIONS:
            raise ValueError("Invalid road condition. Please choose from dry, wet, snow, or icy.")
    friction_coefficient = ROAD_FRICTIONS[friction_type]
    gravity = 9.81

    eff_dec= calculate_effective_deceleration(gravity, friction_coefficient, gradient_percent)
    reaction_distance = calculate_reaction_distance(reaction_time, speed_kmh)
    braking_distance = calculate_braking_distance(speed_kmh, eff_dec)
    stopping_distance = reaction_distance + braking_distance

    return reaction_distance, braking_distance, stopping_distance
    #return stopping_distance

def calculate_stopping_distances(speeds_kmh, reaction_time, gradient_percent, friction_type):
     stop_distances=[]
     for speed in speeds_kmh:
          stop_distances.append(calculate_stopping_distance(speed, reaction_time, gradient_percent, friction_type))
     
     return stop_distances


def main():
    speed_kmh=float(input("Enter the speed of the vehicle in km/h: "))
    if speed_kmh < 0:
        raise ValueError("Speed cannot be negative. Please enter a valid speed.")
    reaction_time=float(input("Enter the reaction time in seconds: "))
    if reaction_time < 0:
        raise ValueError("Reaction time cannot be negative. Please enter a valid reaction time.")
    gradient_percent=float(input("Enter the gradient of the road in percentage, if flat enter 0: "))
    friction_type=input("Enter the road condition (dry, wet, snow, icy): ").lower()
    # speeds_kmh = [float(x) for x in input("Enter the speeds of the vehicles in km/h, separated by commas: ").split(",")]
    # if any(speed < 0 for speed in speeds_kmh):
    #     raise ValueError("Speeds cannot be negative. Please enter valid speeds.")

    reaction_distance, braking_distance,stopping_distance = calculate_stopping_distances(speed_kmh, reaction_time, gradient_percent, friction_type)
    print(f"Reaction Distance: {reaction_distance:.2f} meters")
    print(f"Braking Distance: {braking_distance:.2f} meters")
    print(f"Stopping Distance: {stopping_distance:.2f} meters")

if __name__ == "__main__":
    main()    

import math
import matplotlib.pyplot as plt

def kmh_to_ms(speed_kmh):
    """Convert vehicle speed from km/h to m/s."""
    return speed_kmh * 1000 / 3600
   
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
    if friction_type not in ROAD_FRICTIONS:
            raise ValueError("Invalid road condition. Please choose from dry, wet, snow, or icy.")
    if gradient_percent < 0:
        raise ValueError("Gradient cannot be negative. Please enter a valid gradient.")
    if speed_kmh < 0:
        raise ValueError("Speed cannot be negative. Please enter a valid speed.")   
    if reaction_time < 0:
        raise ValueError("Reaction time cannot be negative. Please enter a valid reaction time.")
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

def calculate_stopping_distance_for_multiple_road_conditions(speeds_kmh, reaction_time, gradient_percent, friction_types):
     #comparing stopping distances for different road conditions
     stop_distances_by_condition = []
     for friction_type in friction_types:
            stop_distances_1=calculate_stopping_distances(speeds_kmh, reaction_time, gradient_percent, friction_type)

            stop_distances_by_condition.append((friction_type, stop_distances_1))
     return stop_distances_by_condition 

def plotting_stopping_distances(stop_distances_by_condition):
    stopping_distances = {}
    # stop_distances_by_condition = calculate_stopping_distance_for_multiple_road_conditions(speeds_kmh,reaction_time,gradient_percent,friction_types)
    for condition, distances in stop_distances_by_condition:
            for i in range(len(distances)):
                  stopping_distance = distances[i][2]  # Get the stopping distance from the tuple
                  if condition not in stopping_distances:
                        stopping_distances[condition] = []
                  stopping_distances[condition].append(stopping_distance)
    return stopping_distances

def main():
    # speed_kmh=float(input("Enter the speed of the vehicle in km/h: "))
    # if speed_kmh < 0:
    #     raise ValueError("Speed cannot be negative. Please enter a valid speed.")
    reaction_time=float(input("Enter the reaction time in seconds: "))
    if reaction_time < 0:
        raise ValueError("Reaction time cannot be negative. Please enter a valid reaction time.")
    gradient_percent=float(input("Enter the gradient of the road in percentage, if flat enter 0: "))
    if gradient_percent < 0:
        raise ValueError("Gradient cannot be negative. Please enter a valid gradient.")
    friction_types=[input("Enter the road condition (dry, wet, snow, icy): ").lower() for _ in range(4)]
    print("Selected road conditions:", friction_types)
    speeds_kmh = [float(x) for x in input("Enter the speeds of the vehicles in km/h, separated by commas: ").split(",")]
    if any(speed < 0 for speed in speeds_kmh):
        raise ValueError("Speeds cannot be negative. Please enter valid speeds.")
    

    # stoping_distances= calculate_stopping_distances(speeds_kmh, reaction_time, gradient_percent, friction_type)
   
    # print("Stopping Distance:",stoping_distances," meters")
    # print("\nComparing stopping distances for different road conditions:")
    # stop_distances_by_condition = calculate_stopping_distance_for_multiple_road_conditions(speeds_kmh, reaction_time, gradient_percent, friction_types)

    # print('\n',stop_distances_by_condition)#
    stop_distances_by_condition = calculate_stopping_distance_for_multiple_road_conditions(speeds_kmh,reaction_time,gradient_percent,friction_types)
    stopping_distances_by_condition = plotting_stopping_distances(stop_distances_by_condition)
    plot_stopping_distances(speeds_kmh, stopping_distances_by_condition)
    
    print("\nStopping distances for different road conditions:")
    for condition, distances in stop_distances_by_condition:
        print(f"\nRoad condition: {condition}")

        for i in range(len(speeds_kmh)):
            reaction_distance, braking_distance, stopping_distance = distances[i]
            print(f"\nSpeed: {speeds_kmh[i]} km/h")
            print(f"Reaction distance: {reaction_distance:.2f} m")
            print(f"Braking distance: {braking_distance:.2f} m")
            print(f"Total stopping distance: {stopping_distance:.2f} m")
    
def plot_stopping_distances(speeds_kmh, stopping_distances_by_condition):

    plt.figure(figsize=(10, 6))

    for condition, distances in stopping_distances_by_condition.items():
        plt.plot(
            speeds_kmh,
            distances,
            marker="o",
            markersize=7,
            linewidth=2,
            label=condition.capitalize()
        )

    plt.xlabel("Vehicle Speed (km/h)", fontsize=12)
    plt.ylabel("Stopping Distance (m)", fontsize=12)
    plt.title("Stopping Distance vs Vehicle Speed", fontsize=15, fontweight="bold")

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(title="Road Condition", fontsize=10)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()    

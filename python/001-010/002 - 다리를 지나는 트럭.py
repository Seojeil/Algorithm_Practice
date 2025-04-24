def solution(bridge_length, weight, truck_weights):
    second = 0
    bridge = [0] * bridge_length
    current_weight = 0

    while truck_weights:
        second += 1
        current_weight -= bridge[0]
        bridge.pop(0)

        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights[0])
            truck_weights.pop(0)
        else:
            bridge.append(0)

    return second + bridge_length

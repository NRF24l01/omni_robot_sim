import math

def sum_vectors(vectors):
    x_sum = 0
    y_sum = 0
    for length, angle in vectors:
        x_sum += length * math.cos(math.radians(angle))
        y_sum += length * math.sin(math.radians(angle))
    result_length = round(math.sqrt(x_sum**2 + y_sum**2))
    result_angle = round(math.degrees(math.atan2(y_sum, x_sum)))
    return result_length, result_angle
def rotate_vectors(vectors):
    for i in range(len(vectors)):
        if vectors[i][0]<0:
            vectors[i][0] = abs(vectors[i][0])
            vectors[i][1] += 180
def check_rotation(steps):
    if steps[0]>0 and steps[1]>0 and steps[2] >0:
        rotation_steps = min(steps)
        for i in range(len(steps)):
            steps[i]=steps[i]- rotation_steps
        print("right rotation")
    elif steps[0]<0 and steps[1]<0 and steps[2]<0:
        rotation_steps = max(steps)
        for i in range(len(steps)):
            steps[i]=steps[i]+rotation_steps
        
        print("left rotation")
    else:
        print("no rotations")
        rotation_steps = 0
    return [steps, rotation_steps]
def vector_to_coords(vector):
    x = round(vector[0] * math.cos(math.radians(vector[1])))
    y = round(vector[0] * math.sin(math.radians(vector[1])))
    return x,y
def count_bot_moving(steps,angle,coords):
    #res = list(list(zip(*aaa))[1]
    
    a = check_rotation(list(list(zip(*vectors))[0]))
    a[0][0] = [a[0][0],vectors[0][1]]
    a[0][1] = [a[0][1],vectors[1][1]]
    a[0][2] = [a[0][2],vectors[2][1]]
    summed_vector = sum_vectors(a[0])
    result = vector_to_coords(summed_vector)

    print("a:",a)
    print("summed vector:",summed_vector)
    print("rotation:",a[1])
    print("res:",result)
    
    """
    передаётся: шаги в виде списка, угол поворота робота, координаты роьота
    возвпращается: координаты конца движения, и угол
    """
if __name-- == "__main__";    
    vectors = [
    [00, 90],
    [-100, 135],
    [-100,45]
    ]

    print(count_bot_moving(vectors,0,[0,0]))

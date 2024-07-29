from flask import Flask, request, jsonify, render_template
from omni_calc import calculate_resultant_vector, polar_to_cartesian
from config import robot_radius

app = Flask(__name__)

# Field dimensions in mm
FIELD_WIDTH = 3000
FIELD_HEIGHT = 2000

# Robot initial position and angle
robot_x = FIELD_WIDTH / 2
robot_y = FIELD_HEIGHT / 2
robot_angle = 0  # in degrees

# Constants
# WHEEL_RADIUS = 50  # mm
ROBOT_RADIUS = 200  # mm


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/get_position', methods=['GET'])
def get_position():
    return jsonify({'x': robot_x, 'y': robot_y, 'angle': robot_angle})


@app.route('/set_movement', methods=['POST'])
def set_movement():
    global robot_x, robot_y, robot_angle
    data = request.json
    speed1 = int(data['speed1'])  # mm/sec
    speed2 = int(data['speed2'])  # mm/sec
    speed3 = int(data['speed3'])  # mm/sec
    time = int(data['time'])  # sec

    resultant_length, resultant_angle = calculate_resultant_vector(speed1, speed2, speed3, robot_radius)

    resultant_length, resultant_angle = round(resultant_length, 2), round(resultant_angle, 2)

    if round(resultant_length) != 0:
        v_x, v_y = polar_to_cartesian(resultant_length, resultant_angle)
        omega_z = 0
    else:
        v_x, v_y = 0, 0
        omega_z = resultant_angle

    # Update robot position
    robot_x += v_x * time
    robot_y += v_y * time
    robot_angle += omega_z * time
    robot_angle %= 360

    # Ensure the robot stays within the field
    robot_x = max(0, min(FIELD_WIDTH, robot_x))
    robot_y = max(0, min(FIELD_HEIGHT, robot_y))

    return jsonify({'x': robot_x, 'y': robot_y, 'angle': robot_angle})


if __name__ == '__main__':
    app.run(debug=True)

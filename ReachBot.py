import odrive
drive = None


def connect():
    print("Connecting to driver...")
    drive = odrive.find_any()
    print("Successfully connected.")


def full_calibration(d=drive):
    print("Starting calibration...")
    d.axis0.requested_state = AXIS_STATE_ENCODER_OFFSET_CALIBRATION
    print("Calibration complete.")


def check_voltage(d=drive):
    print(d.vbus_voltage)


def current_limit(d=drive):
    print(d.axis0.motor.config.current_lim)


def get_velocity_limit(d=drive):
    print(d.axis0.controller.config.vel_limit)


def set_velocity_limit(val, d=drive):
    d.axis0.controller.config.vel_limit = val
    print("Velocity limit has been set to {} turns/sec.").format(val)


def get_calibration_current(d=drive):
    print(d.axis0.motor.config.calibration_current)


def set_calibration_current(val, d=drive):
    d.axis0.motor.config.calibration_current = val
    print("Calibration current has been set to {} A").format(val)


def get_brake_resistance(d=drive):
    print(d.config.brake_resistance)


def set_brake_resistance(val, d=drive):
    d.config.brake_resistance = val
    print("Brake resistance set to {} Ohms.").format(val)


def get_torque_constant(d=drive):
    print(d.axis0.motor.config.torque_constant)
    print("Default value is 8.27.")


def set_torque_constant(val, d=drive):
    d.axis0.motor.config.torque_constant = val
    print("Torque constant set to {}.").format(val)
    print("Default value is 8.27.")


    # arm = find_arms()
    # print("ARM FOUND")
    # while(True):
    #     command = input()
    #     args = command.split(" ")
    #     if args[0] == "print" and len(args) > 1:
    #         if args[1] == "voltage":
    #             print(arm.vbus_voltage)
    #         elif args[1] == "current":
    #             print(arm.axis0.motor.config.current_lim)
    #         else:
    #             print("INVALID COMMAND")


def get_encoder_counts(d=drive):
    print(d.axis0.encoder.config.cpr)


def set_encoder_counts(val, d=drive):
    d.axis0.encoder.config.cpr = val
    print("Encoder count set to {} counts/rev").format(val)


def shadow_count(d=drive):
    print(d.axis0.encoder.shadow_count)


def get_axis_state(d=drive):
    print("Current state is", d.axis0.current_state)
    print("\n1 --> idle\n3 --> full calibration\n8 --> closed loop ")


def set_axis_state(val, d=drive):
    d.axis0.requested_state = val
    print("Axis state set to", val)
    print("\n1 --> idle\n3 --> full calibration\n8 --> closed loop ")


def get_control_mode(d=drive):
    print(d.axis0.controller.config.control_mode)
    print("\n1 --> torque control\n2 --> velocity control\n3 --> position control")


def set_control_mode(val, d=drive):
    d.axis0.controller.config.control_mode = val
    print("Control mode has been set to", val)
    print("\n1 --> torque control\n2 --> velocity control\n3 --> position control")


def get_input_mode(d=drive):
    print(d.axis0.controller.config.input_mode)
    print("\n0 --> inactive\n1 --> pass through\n3 --> 2nd order position filter")


def set_input_mode(val, d=drive):
    d.axis0.controller.config.input_mode = val
    print("Input mode has been set to", val)
    print("\n0 --> inactive\n1 --> pass through\n3 --> 2nd order position filter")


def command_velocity(val, d=drive):
    d.axis0.controller.input_vel = val
    print("Velocity commanded to {} turns/sec.").format(val)


def command_position(val, d=drive):
    d.axis0.controller.input_pos = val
    print("Position commanded to {}.").format(val)


def errors(d=drive):
    odrive.dump_errors(d)


def clear_errors(d=drive):
    odrive.dump_errors(odrv0, True)


# Check motor voltage
# odrv0.vbus_voltage

# Current limit (A), 10 is safe, up to 60
# odrv0.axis0.motor.config.current_lim

# Velocity limit (turns/sec)
# odrv0.axis0.controller.config.vel_limit

# Calibration current (A)
# odrv0.axis0.motor.config.calibration_current

# Brake resistance (ohm)
# odrv0.config.brake_resistance

# Torque constant (should be 8.27)
# odrv0.axis0.motor.config.torque_constant

# High current or gimbal (0 and 1 respectively)
# odrv0.axis0.motor.config.motor_type

# Set encoder counts
# odrv0.axis0.encoder.config.cpr

# Calibration
# odrv0.axis0.requested_state = AXIS_STATE_ENCODER_OFFSET_CALIBRATION

# Shadow count
# odrv0.axis0.encoder.shadow_count

# Changing axis state
# 1 --> idle
# 3 --> full calibration
# 8 --> closed loop 
# odrv0.axis0.current_state
# odrv0.axis0.requested_state

# Changing control mode
# 1 --> torque control
# 2 --> velocity control
# 3 --> position control
# odrv0.axis0.controller.config.control_mode

# Changing input mode
# 0 --> inactive
# 1 --> pass through
# 3 --> 2nd order position filter
# odrv0.axis0.controller.config.input_mode

# Input velocity
# odrv0.axis0.controller.input_vel

# Input pos
# odrv0.axis0.controller.input_pos

# Get errors
# dump_errors(odrv0)
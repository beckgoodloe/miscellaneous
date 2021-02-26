import odrive


def find_arms():
    arm1 = odrive.find_any()
    return arm1


def main():
    print("INITIALIZING")
    arm = find_arms()
    print("ARM FOUND")
    while(True):
    	command = input()
    	args = command.split(" ")
    	if args[0] == "print" and len(args) > 1:
    		if args[1] == "voltage":
    			print(arm.vbus_voltage)
    		elif args[1] == "current":
    			print(arm.axis0.motor.config.current_lim)
    		else:
    			print("INVALID COMMAND")

    # print(od.axis0)
    # print(axis.motor)
    # print(axis.encoder)


if __name__ == '__main__':
    main()

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
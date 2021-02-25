import odrive


def find_arms():
    arm1 = odrive.find_any()
    return arm1


def main():
    print("INITIALIZING")
    arm = find_arms()
    print(od.axis0)
    print(axis.motor)
    print(axis.encoder)


if __name__ == '__main__':
    main()

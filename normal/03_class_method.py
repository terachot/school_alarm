class Tank:
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo

    def add_ammo(self, ammo):
        if self.ammo + ammo <= 10:
            self.ammo += ammo

    def fire_ammo(self):
        if self.ammo > 0:
            self.ammo -= 1


first_tank = Tank('terap', 5)
first_tank.fire_ammo()
first_tank.fire_ammo()
print(first_tank.ammo)

first_tank.add_ammo(3)
print(first_tank.ammo)
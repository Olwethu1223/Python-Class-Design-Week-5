class Superhero:
    def __init__(self, name, combat_skills, speed, infinity):
        self.name = name
        self.combat_skills = combat_skills
        self.speed = speed
        self.infinity = infinity
        self.inventory = []

    def use_combat_skills(self):
        print(f"{self.name} unleashes a devastating combo of martial arts and cursed energy, "
              f"like Gojo's limitless strength mixed with Jin Woo's awakened combat prowess!")

    def use_speed(self):
        print(f"{self.name} moves with the speed of light, almost impossible to follow, "
              f"as if moving through a realm of limitless speed!")

    def activate_infinity(self):
        print(f"{self.name} activates the Infinity, where time itself seems to stand still, "
              f"and they become untouchable. No one can escape their domain!")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to {self.name}'s limitless inventory.")

    def show_details(self):
        print(f"\nSuperhero: {self.name}")
        print(f"Combat Skills: {self.combat_skills}")
        print(f"Speed: {self.speed}")
        print(f"Infinity: {self.infinity}")
        print(f"Inventory: {', '.join(self.inventory)}")


class EnhancedSuperhero(Superhero):
    def __init__(self, name, combat_skills, speed, infinity, telekinesis_power, energy_power):
        super().__init__(name, combat_skills, speed, infinity)
        self.telekinesis_power = telekinesis_power
        self.energy_power = energy_power

    def use_telekinesis(self):
        print(f"{self.name} exerts their will, using telekinesis to control and crush enemies, "
              f"much like Jin Woo controlling his surroundings or Gojo’s manipulation of cursed energy!")

    def manipulate_energy(self):
        print(f"{self.name} channels boundless energy into an unstoppable force, creating devastating blasts "
              f"or protective shields. Their cursed energy or mana is unmatched!")

    def use_shadow_manipulation(self):
        print(f"{self.name} uses their mastery of shadows, creating voids that trap opponents in an infinite dimension!")

    def show_details(self):
        super().show_details()
        print(f"Telekinesis Power: {self.telekinesis_power}")
        print(f"Energy Manipulation Power: {self.energy_power}")


hero = EnhancedSuperhero(
    name="Infinity Sovereign",
    combat_skills="Mastery in Martial Arts, Cursed Energy, and Mana Manipulation",
    speed="Lightspeed (Unmatched)",
    infinity="Control over Space, Time, and the Infinite Realm",
    telekinesis_power="Ultimate Control over Objects and Enemies",
    energy_power="Unstoppable Energy Blasts and Shields"
)

hero.use_shadow_manipulation()
hero.use_combat_skills()
hero.use_telekinesis()
hero.manipulate_energy()
hero.use_speed()
hero.activate_infinity()

hero.add_to_inventory("Infinity Gauntlet")
hero.add_to_inventory("Void Blade")
hero.add_to_inventory("Sovereign Armor")

hero.show_details()

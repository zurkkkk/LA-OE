class Food:
    def __init__(self, *ingredients):
        self.ingredients = ingredients
    
    def __str__(self):
        return f"This dish has the following ingredients: {', '.join(map(str, self.ingredients))}"

class Adobo(Food):
    def __init__(self, meat, soy_sauce, vinegar, garlic, bay_leaves, pepper, oil="vegetable oil", sugar="a pinch of sugar"):
        super().__init__(meat, soy_sauce, vinegar, garlic, bay_leaves, pepper, oil, sugar)
        self.meat = meat
        self.soy_sauce = soy_sauce
        self.vinegar = vinegar
        self.garlic = garlic
        self.bay_leaves = bay_leaves
        self.pepper = pepper
        self.oil = oil
        self.sugar = sugar
    
    def __str__(self):
        return f"My adobo has {self.meat} kg of meat, {self.soy_sauce} cups of soy sauce, {self.vinegar} cups of vinegar, {self.garlic} cloves of garlic, {self.bay_leaves} bay leaves, {self.pepper} teaspoons of pepper, cooked in {self.oil} oil, and sweetened with {self.sugar}."

classic_adobo = Adobo(1, 0.5, 0.5, 4, 2, 1)

print(classic_adobo)

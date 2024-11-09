from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.power = randint(30,60)
        self.hp = randint(200,450)
        Pokemon.pokemons[pokemon_trainer] = self


    def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['stats'][0]["base_stat"]
        else:
            return 50

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']["other"]["official-artwork"]["front_default"]
        else:
            return 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/547.png'
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_power(self):
        url = f''
    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name}\nздоровье: {self.hp}\nСила:{self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def show_hp(self):
        return f'HP: {self.hp}'

    def attack(self, enemy):
        if isinstance(enemy,wizard):
             chance = randint(1,3)
             if chance == 1:
                  return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}\n" +\
                   f"@{self.pokemon_trainer} нанес {self.power} урона\n" +\
                   f"Здоровье @{enemy.pokemon_trainer} {enemy.hp}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        

class wizard(Pokemon):
    def info(self):
        return super().info() + "\nУ тебя покемон-волшебник"
class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5, 15)
        # увеличиваем атаку
        self.power += super_power
        # вызываем родительский метод атаки
        result = super().attack(enemy)
        # уменьшаем атаку
        self.power -= super_power
        return 'Была применена супер-сила🔥\n' + result
    
    def info(self):
        return super().info() + "\nУ тебя покемон-боец"




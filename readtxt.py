import ClassBot
MaxFloatSkin = []

def load_data_from_txt(FloatSkinfile):
    with open(FloatSkinfile, 'r') as file:
        lines = file.readlines()

        
        MaxFloats = []
        Skins = []
        Prices = []

        # Разделение строк на имя и фамилию
        for line in lines:
            # Разделение строки на имя и фамилию по пробелу
            parts = line.strip().split(' ')
            MaxFloat, Skin, Price = parts
            MaxFloats.append(MaxFloat)
            Skins.append(Skin)
            Prices.append(Price)

        return MaxFloats, Skins, Prices

    
# Загрузка данных из файла
filename = 'FloatSkin.txt'  # Укажите имя вашего файла
MaxFloats, Skins, Prices = load_data_from_txt(filename)
MaxFloatSkin = []
# Вывод имен и фамилий
for MaxFloat, Skin, Price in zip(MaxFloats, Skins, Prices):
    MaxFloatSkin.append(ClassBot.SkinFloat(MaxFloat,Skin,Price))


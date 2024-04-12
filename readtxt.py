def load_data_from_txt(FloatSkinfile):
    inputdata = []
    with open(FloatSkinfile, 'r') as file:
        for line in file:
            # Предполагается, что значения разделены пробелами или другим разделителем
            values = line.strip().split()  # Разделение строки на значения
            inputdata.extend(values)  # Добавление значений в список
    return inputdata
# Загрузка данных из файла
filename = 'FloatSkin.txt'  # Укажите имя вашего файла
inputdata = load_data_from_txt(filename)

# Вывод загруженных данных для проверки
print("Загруженные данные из файла:", inputdata)
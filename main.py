from PIL import Image
import os

def resize_to_square(input_path, output_path, size):
    try:
        image = Image.open(input_path)

        # Изменяем размер до указанного размера, сохраняя пропорции
        image = image.resize((size, size))

        # Сохраняем изображение
        image.save(output_path)
        print(f"Изображение {input_path} успешно сплющено до {size}x{size} и сохранено как {output_path}.")
    except Exception as e:
        print(f"Ошибка при сплющивании изображения {input_path}: {e}")
def main():
    input_folder = "D:\\фото для стикеров"
    output_folder = "D:\\фотки переделанные"

    square_size = 512

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".png"
        output_path = os.path.join(output_folder, output_filename)
        resize_to_square(input_path, output_path, square_size)

if __name__ == "__main__":
    main()
import os
from PIL import Image
import pillow_heif


def convert_heic_to_jpg():
    # 获取当前工作目录
    current_folder = os.getcwd()

    # 遍历文件夹中的所有文件
    for filename in os.listdir(current_folder):
        if filename.lower().endswith('.heic'):
            heic_path = os.path.join(current_folder, filename)

            try:
                # 使用 pillow-heif 打开 HEIC 文件
                heif_file = pillow_heif.read_heif(heic_path)

                # 将 HEIC 数据转换为 PIL 图像
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw",
                    heif_file.mode,
                    heif_file.stride,
                )

                # 保存为 JPG
                jpg_filename = os.path.splitext(filename)[0] + '.jpg'
                jpg_path = os.path.join(current_folder, jpg_filename)
                image.save(jpg_path, "JPEG")
                print(f'Converted: {heic_path} to {jpg_path}')

                # 删除原始 HEIC 文件
                os.remove(heic_path)
                print(f'Deleted: {heic_path}')

            except Exception as e:
                print(f'Error converting {heic_path}: {e}')

    print('Batch conversion completed!')


if __name__ == "__main__":
    convert_heic_to_jpg()

import os
import random
from PIL import Image

'''sua cai duoi cuoi de kiem tra cac class vd: chair'''
SKETCH_FOLDER = r"D:\bt\ttcs\Sketchy_4class\sketch\chair"
PHOTO_FOLDER = r"D:\bt\ttcs\Sketchy_4class\photo\chair"


def get_random_files(folder_path, count=5):
    all_files = []

    # Lấy toàn bộ file mọi đuôi
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            full_path = os.path.join(root, f)
            if os.path.isfile(full_path):
                all_files.append(full_path)

    print("Tổng file tìm được:", len(all_files))

    if len(all_files) == 0:
        print("❌ Không có file trong:", folder_path)
        return []

    return random.sample(all_files, min(count, len(all_files)))


def check_file(file_path):
    errors = []

    # 1. Check tồn tại
    if not os.path.exists(file_path):
        errors.append("File không tồn tại")
        return errors

    # 2. Check 0KB
    if os.path.getsize(file_path) == 0:
        errors.append("File 0KB")
        return errors

    # 3. Thử mở file binary (để chắc file đọc được)
    try:
        with open(file_path, "rb") as f:
            f.read(10)
    except Exception as e:
        errors.append(f"Không đọc được file: {e}")
        return errors

    # 4. Check file lạ (không phải ảnh)
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.webp')
    if not file_path.lower().endswith(valid_extensions):
        errors.append("File lạ (không phải ảnh)")
        return errors

    # 5. Nếu là ảnh thì thử mở bằng PIL
    try:
        with Image.open(file_path) as img:
            img.verify()
    except:
        errors.append("Ảnh lỗi / corrupt")


def check_group(title, folder):
    print(f"\n===== KIỂM TRA {title} =====")

    files = get_random_files(folder, 5)

    for file in files:
        errors = check_file(file)
        if errors:
            print(f"[LỖI] {file}")
            for err in errors:
                print("   -", err)
            '''
            them doan nay neu muon xoa 
            try:
                os.remove(file)
            except Exception as e:
                print("   - Không xóa được:", e)
                '''
        else:
            print(f"[OK] {file}")
            try:
                with Image.open(file) as img:
                    img.show()
            except:
                pass


def main():
    check_group("SKETCH", SKETCH_FOLDER)
    check_group("PHOTO", PHOTO_FOLDER)


if __name__ == "__main__":
    main()

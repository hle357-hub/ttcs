import os

# 🔹 ĐƯỜNG DẪN GỐC DATASET
BASE_PATH = r"D:\bt\ttcs\Sketchy_4class"

SKETCH_PATH = os.path.join(BASE_PATH, "sketch")
PHOTO_PATH = os.path.join(BASE_PATH, "photo")

total_sketch = 0
total_photo = 0


def count_files(folder_path):
    """
    Đếm tất cả file trong folder (kể cả subfolder)
    """
    count = 0
    for root, dirs, files in os.walk(folder_path):
        count += len(files)
    return count


# ✅ Kiểm tra tồn tại path gốc
if not os.path.exists(BASE_PATH):
    print("❌ BASE_PATH không tồn tại")
    exit()

if not os.path.exists(SKETCH_PATH):
    print("❌ Không có folder sketch")
    exit()

if not os.path.exists(PHOTO_PATH):
    print("❌ Không có folder photo")
    exit()


# ✅ Lấy class tự động từ folder sketch
classes = os.listdir(SKETCH_PATH)

print("===== CHI TIẾT =====\n")

for cls in classes:
    sketch_folder = os.path.join(SKETCH_PATH, cls)
    photo_folder = os.path.join(PHOTO_PATH, cls)

    # nếu không phải folder thì bỏ qua
    if not os.path.isdir(sketch_folder):
        continue

    sketch_count = count_files(sketch_folder)

    if os.path.exists(photo_folder):
        photo_count = count_files(photo_folder)
    else:
        photo_count = 0

    total_sketch += sketch_count
    total_photo += photo_count

    print(f"{cls}:")
    print(f"   sketch: {sketch_count}")
    print(f"   photo : {photo_count}")
    print()


print("===== TỔNG =====")
print("Total classes:", len(classes))
print("Total sketch :", total_sketch)
print("Total photo  :", total_photo)

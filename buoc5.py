import os
from PIL import Image
import torch
from torch.utils.data import Dataset
from torchvision import transforms


class SketchyDataset(Dataset):
    def __init__(self, root_dir):
        """
        root_dir = "Sketchy_4class"
        """
        self.root_dir = root_dir

        # Mapping label
        self.class_map = {
            "zebra": 0,
            "wine_bottle": 1,
            "chair": 2,
            "window": 3
        }

        self.sketch_path = os.path.join(root_dir, "sketch")
        self.photo_path = os.path.join(root_dir, "photo")

        # Transform ảnh thành tensor
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor()
        ])

        # Danh sách lưu tất cả samples
        self.samples = []

        # Duyệt từng class
        for class_name in self.class_map.keys():

            sketch_folder = os.path.join(self.sketch_path, class_name)
            photo_folder = os.path.join(self.photo_path, class_name)

            label = self.class_map[class_name]

            sketch_files = os.listdir(sketch_folder)
            photo_files = os.listdir(photo_folder)

            # Ghép ngẫu nhiên sketch với photo cùng class
            for sketch_file in sketch_files:
                sketch_full = os.path.join(sketch_folder, sketch_file)

                # chọn đại 1 photo cùng class
                if len(photo_files) > 0:
                    photo_file = photo_files[0]
                    photo_full = os.path.join(photo_folder, photo_file)

                    self.samples.append((sketch_full, photo_full, label))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        sketch_path, photo_path, label = self.samples[idx]

        sketch_img = Image.open(sketch_path).convert("RGB")
        photo_img = Image.open(photo_path).convert("RGB")

        sketch_tensor = self.transform(sketch_img)
        photo_tensor = self.transform(photo_img)

        return sketch_tensor, photo_tensor, label


# ==========================
# TEST
# ==========================

dataset = SketchyDataset("D:/bt/ttcs/Sketchy_4class")

print(dataset[0])

import json

label_map = {
    0: "zebra",
    1: "wine_bottle",
    2: "chair",
    3: "window"
}

with open(r"D:\code\python\ttcs\label_map.json", "w") as f:
    json.dump(label_map, f, indent=4)

print("Đã tạo file label_map.json")

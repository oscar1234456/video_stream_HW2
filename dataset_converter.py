import json
import os

original_dataset_path = "./datasets/GTA_Dataset"
target_dataset_path = "./datasets"


def make_json_template():
    contents = {
        "info": {
            "year": 2021,
            "version": "1.0",
            "description": "For object detection",
            "date_created": "2021"
        },
        "images": [
        ],
        "annotations": [

        ],
        "categories": [
            {
                "id": 1,
                "name": 0,
                "supercategory": 0
            }
        ]
    }
    return contents


def make_train():
    all_train_filenames = os.listdir(original_dataset_path + "/train2017")
    temp = make_json_template()
    bbox_counter = 0
    for idx, now_file in enumerate(all_train_filenames):
        temp_dic = {
            "date_captured": "2021",
            "file_name": now_file,
            "id": idx + 1,
            "height": 1080,
            "width": 1920
        }
        print(f"nowfile:{now_file}")
        with open(original_dataset_path + "/train_labels/" + now_file[:-4] + ".txt", "r") as f:
            all_bbox = f.readlines()
            for focus_bbox in all_bbox:
                bbox_counter += 1
                information = focus_bbox.strip().split(" ")
                print(f"focus_bbox:{focus_bbox}")
                temp_dic_bbox = {
                    "image_id": idx + 1,
                    "bbox": [
                        float(information[1]) * 1920,
                        float(information[2]) * 1080,
                        float(information[3]) * 1920,
                        float(information[4]) * 1080,
                    ],
                    "category_id": 1,
                    "id": bbox_counter,
                    "iscrowd": 0,
                    "area": (float(information[3]) * 1920) * (float(information[4]) * 1080)
                }
                temp["annotations"].append(temp_dic_bbox)

        temp["images"].append(temp_dic)

    with open(target_dataset_path + "/train_data_annotate.json", "w") as fw:
        json.dump(temp, fw)


def make_val():
    all_train_filenames = os.listdir(original_dataset_path + "/val2017")
    temp = make_json_template()
    bbox_counter = 0
    for idx, now_file in enumerate(all_train_filenames):
        temp_dic = {
            "date_captured": "2021",
            "file_name": now_file,
            "id": idx + 1,
            "height": 1080,
            "width": 1920
        }
        print(f"nowfile:{now_file}")
        with open(original_dataset_path + "/val_labels/" + now_file[:-4] + ".txt", "r") as f:
            all_bbox = f.readlines()
            for focus_bbox in all_bbox:
                bbox_counter += 1
                information = focus_bbox.strip().split(" ")
                print(f"focus_bbox:{focus_bbox}")
                temp_dic_bbox = {
                    "image_id": idx + 1,
                    "bbox": [
                        float(information[1]) * 1920,
                        float(information[2]) * 1080,
                        float(information[3]) * 1920,
                        float(information[4]) * 1080,
                    ],
                    "category_id": 1,
                    "id": bbox_counter,
                    "iscrowd": 0,
                    "area": (float(information[3]) * 1920) * (float(information[4]) * 1080)
                }
                temp["annotations"].append(temp_dic_bbox)

        temp["images"].append(temp_dic)

    with open(target_dataset_path + "/val_data_annotate.json", "w") as fw:
        json.dump(temp, fw)


def make_test():
    pass


if __name__ == "__main__":
    print(">>>train")
    make_train()
    print("<<train complete")
    print(">>test")
    make_val()
    print("<<test complete")



import pickle

from preprocess.utils import create_action_object


path_data = "/home/ximenes/Desktop/openpose/data/"

print("[INFO] Cretating object list ...")
action_list = create_action_object(path_data)

print("[INFO] Creating pickle file ...")
pik = "database.dat"

with open(pik, "wb") as f:
    pickle.dump(action_list, f)

with open(pik, "rb") as f1:
    data = pickle.load(f1)

print(data[0].action_data[0]['keypoint']['left_knee']['coordinate_x'])








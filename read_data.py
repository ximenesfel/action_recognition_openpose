import pickle

data_path = "/home/ximenes/PycharmProjects/openpose/database.dat"


with open(data_path, "rb") as f:
    data = pickle.load(f)

print(data[0].action_data[0]['keypoint']['left_knee']['coordinate_x'])
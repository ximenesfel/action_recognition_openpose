import os
import json

from classes.action import Action


def create_folder(path):

    if not os.path.exists(path):
        os.makedirs(path)

def read_files_in_path(path):

    return os.listdir(path)

def extraction_extension_file_name(name):

    name = name.split(".avi")

    return name[0]

def process_json_information(file):

    keypoint = ["nose", "neck", "right_shoulder", "right_elbow", "right_wrist", "left_shoulder", "left_elbow", "left_wrist", "right_hip", "right_knee", "right_ankle",
                "left_hip", "left_knee", "left_ankel", "right_eye", "left_eye", "right_ear", "left_ear"]

    number = 0
    keypoint_dict_data = {}

    with open(file, "r") as f:
        data = json.load(f)

        for key in keypoint:

            keypoint_data = {key: {"coordinate_x": data["people"][0]["pose_keypoints_2d"][number],
                                               "coordinate_y": data["people"][0]["pose_keypoints_2d"][number+1],
                                               "confidence": data["people"][0]["pose_keypoints_2d"][number+2]} }
            number += 3
            keypoint_dict_data.update(keypoint_data)

    return keypoint_dict_data

def extract_rgb_name_file_name(file_name):

    name = file_name.split("_rgb")

    return name[0]


def process_file_name(file_name):


    setup_model = file_name[1:4]

    if (setup_model == '001'):
        setup_model = "h_1_7_d_3_5"
    elif (setup_model == '002'):
        setup_model = "h_1_7_d_2_5"
    elif (setup_model == '003'):
        setup_model = "h_1_4_d_2_5"
    elif (setup_model == '004'):
        setup_model = "h_1_2_d_3_0"
    elif (setup_model == '005'):
        setup_model = "h_1_2_d_3_0"
    elif (setup_model == '006'):
        setup_model = "h_0_8_d_3_5"
    elif (setup_model == '007'):
        setup_model = "h_0_5_d_4_5"
    elif (setup_model == '008'):
        setup_model = "h_1_4_d_3_5"
    elif (setup_model == '009'):
        setup_model = "h_0_8_d_2_0"
    elif (setup_model == '010'):
        setup_model = "h_1_8_d_3_0"
    elif (setup_model == '011'):
        setup_model = "h_1_9_d_3_0"
    elif (setup_model == '012'):
        setup_model = "h_2_0_d_3_0"
    elif (setup_model == '013'):
        setup_model = "h_2_1_d_3_0"
    elif (setup_model == '014'):
        setup_model = "h_2_2_d_3_0"
    elif (setup_model == '015'):
        setup_model = "h_2_3_d_3_5"
    elif (setup_model == '016'):
        setup_model = "h_2_7_d_3_5"
    elif (setup_model == '017'):
        setup_model = "h_2_5_d_3_0"


    camera_id = file_name[5:8]

    if (camera_id == '001'):
        camera_id = "45_degree_view"
    elif (camera_id == '002'):
        camera_id = "front_view"
    elif (camera_id == '003'):
        camera_id = "side_view"

    peformer_id = file_name[9:12]

    replication_number = file_name[13:16]

    action = file_name[17:20]

    if (action == '001'):
        action = "drink_water"
    elif (action == '002'):
        action = "eat_meal_snack"
    elif (action == '003'):
        action = "brushing_teeth"
    elif (action == '004'):
        action = "brushing_hair"
    elif (action == '005'):
        action = "drop"
    elif (action == '006'):
        action =  "pickup"
    elif (action == '007'):
        action = "throw"
    elif (action == '008'):
        action = "sitting_down"
    elif (action == '009'):
        action = "standding_up"
    elif (action == '010'):
        action = "clapping"
    elif (action == '011'):
        action = "reading"
    elif (action == '012'):
        action = "writing"
    elif (action == '013'):
        action = "tear_up_paper"
    elif (action == '014'):
        action =  "wear_jacket"
    elif (action == '015'):
        action = "take_off_jacket"
    elif (action == '016'):
        action = "wear_a_shoe"
    elif (action == '017'):
        action = "take_off_shoe"
    elif (action == '018'):
        action = "wear_on_glasses"
    elif (action == '019'):
        action = "take_off_glasses"
    elif (action == '020'):
        action = "put_on_a_hat_cap"
    elif (action == '021'):
        action = "take_off_a_hat_cap"
    elif (action == '022'):
        action = "cheer_up"
    elif (action == '023'):
        action = "hand_waving"
    elif (action == '024'):
        action = "kicking_something"
    elif (action == '025'):
        action = "put_something_inside_pocket"
    elif (action == '026'):
        action = "hopping"
    elif (action == '027'):
        action = "jump_up"
    elif (action == '028'):
        action = "make_a_phone_call"
    elif (action == '029'):
        action = "playing_with_a_phone"
    elif (action == '030'):
        action = "typing_on_a_keyboard"
    elif (action == '031'):
        action = "pointing_to_something_with_finger"
    elif (action == '032'):
        action = "taking_a_selfie"
    elif (action == '033'):
        action = "check_time"
    elif (action == '034'):
        action =  "rub_two_hands_together"
    elif (action == '035'):
        action =  "nod_head"
    elif (action == '036'):
        action = "shake_head"
    elif (action == '037'):
        action = "wipe_face"
    elif (action == '038'):
        action = "sawte"
    elif (action == '039'):
        action = "put_the_palms_together"
    elif (action == '040'):
        action =  "cross_hand_in_front"
    elif (action == '041'):
        action = "sneeze"
    elif (action == '042'):
        action = "staggering"
    elif (action == '043'):
        action = "falling"
    elif (action == '044'):
        action = "touch_head"
    elif (action == '045'):
        action = "touch_chest"
    elif (action == '046'):
        action = "touch_back"
    elif (action == '047'):
        action = "touch_neck"
    elif (action == '048'):
        action = "nausea_or_vomiting_condition"
    elif (action == '049'):
        action = "use_a_fan"
    elif (action == '050'):
        action = "punching"
    elif (action == '051'):
        action = "kicking_other_person"
    elif (action == '052'):
        action = "pushing_other_person"
    elif (action == '053'):
        action = "pat_on_back_of_other_person"
    elif (action == '054'):
        action = "point_finder_at_the_other_person"
    elif (action == '055'):
        action = "hugging_other_person"
    elif (action == '056'):
        action = "giving_something_to_other_person"
    elif (action == '057'):
        action = "touch_other_person_pocket"
    elif (action == '058'):
        action = "handshaking"
    elif (action == '059'):
        action = "walking_towards_each_other"
    elif (action == '060'):
        action = "walking_apart_from_each_other"



    return (setup_model, camera_id, peformer_id, replication_number, action)

def write_json(path_videos, path_output_data):

    files_videos = read_files_in_path(path_videos)
    files_data = read_files_in_path(path_output_data)

    if files_data:
        command = "rm -r {}".format(path_output_data) + "*"
        os.system(command)

    count = 1

    for video in files_videos:
        name = extraction_extension_file_name(video)

        print("[INFO] {}/{} Creating folder for {} ".format(count, len(files_videos), name))
        create_folder(path_output_data + name)

        print("[INFO] {}/{} Writing json and video for {}".format(count, len(files_videos), name))
        command = "cd /home/ximenes/openpose/  && ./build/examples/openpose/openpose.bin --video {} --write_json {} --display 0".format(
            path_videos + name + ".avi", path_output_data + name)

        os.system(command)

        count += 1


def create_action_object(data_output_path):

    folder_list = read_files_in_path(data_output_path)

    action_list = []

    for folder in folder_list:

        keypoint_data = {}
        keypoint_list = []

        frame_number = 0
        file_list = read_files_in_path(data_output_path + folder + "/")
        file_list_sorted = sorted(file_list)

        for file in file_list_sorted:
            keypoint_data_dict = process_json_information(data_output_path + folder + "/" + file)
            keypoint_data = {"frame": frame_number, "keypoint": keypoint_data_dict}
            keypoint_list.append(keypoint_data)
            frame_number += 1

        file_name = extract_rgb_name_file_name(folder)

        action_info = process_file_name(file_name)

        action_list.append(Action(action_info, keypoint_list))

    return action_list



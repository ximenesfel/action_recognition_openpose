

class Action:

    def __init__(self, action_info, data_list):

        self.setup_number = action_info[0]
        self.camera_id = action_info[1]
        self.performer_id = action_info[2]
        self.replication_number = action_info[3]
        self.action = action_info[4]

        self.action_data = data_list

    def get_setup_number(self):

        return self.setup_number

    def get_camera_id(self):

        return self.camera_id

    def get_performer_id(self):

        return  self.performer_id

    def get_action(self):

        return self.action

    def get_action_data(self):

        return self.action_data








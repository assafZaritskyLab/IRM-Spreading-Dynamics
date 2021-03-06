import os
import sys
from DynamicsQuantificationScript import DynamicsQuantification
from VideoDynamicsEncoder import DynamicsEncoder


class Procedures:
    def new_data_procedure(self, file_path: str, **kwargs):
        print("----Starting to process file: '{0}'----\n----See results folder when finished----".format(file_path))
        file_path_folder = os.path.dirname(file_path)
        print('dan dan: ', file_path_folder)
        error = False
        print('----creating folders----')
        try:
            #os.mkdir("{0}{1}Results".format(file_path_folder, os.sep))
            print('dandan:   Results')
            os.mkdir(os.path.join(file_path_folder, 'Results'))
        except FileExistsError as e:
            error = True
        try:
            #os.mkdir("{0}{1}Results{1}DynamicsPlots".format(file_path_folder, os.sep))
            print('dandan:   Results/DynamicsPlots')
            os.mkdir(os.path.join(file_path_folder, 'Results', 'DynamicsPlots'))
        except FileExistsError as e:
            error = True
        try:
            #os.mkdir("{0}{1}Results{1}DynamicsNumpyArrays".format(file_path_folder, os.sep))
            print('dandan:   Results/DynamicsNumpyArrays')
            os.mkdir(os.path.join(file_path_folder, 'Results', 'DynamicsNumpyArrays'))
        except FileExistsError as e:
            error = True
        try:
            #os.mkdir("{0}{1}Results{1}VisualizedDynamicsVideos".format(file_path_folder, os.sep))
            print('dandan:   Results/VisualizedDynamicsVideos')
            os.mkdir(os.path.join(file_path_folder, 'Results', 'VisualizedDynamicsVideos'))
        except FileExistsError as e:
            error = True
        if error:
            print("----folders already exist----")

        # quantify the dynamics signal
        dq = DynamicsQuantification(file_path=file_path, **kwargs)
        attach_threshold, detach_threshold = dq.obtain_dynamics()
        # Encode the video with dynamics events
        de = DynamicsEncoder(attachment_thresold=attach_threshold, detachment_thresold=detach_threshold)
        de.manipulate_video(video_path=file_path,
                            manipulated_video_path=os.path.join(file_path_folder, 'Results', 'VisualizedDynamicsVideos'),
                            condition=de.manipulate_frame)

    def example_data_procedure(self, **kwargs):
        path = os.path.join(os.getcwd(), "SampleData", "sample_collagen4.avi")
        self.new_data_procedure(path, **kwargs)

    def print_help(self):
        with open('help.txt', 'r') as help_file:
            line = help_file.readline()
            while line is not None and line != "":
                print(line)
                line = help_file.readline()
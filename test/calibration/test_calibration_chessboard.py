# -*- python -*-
#
#       test_calibration: Module Description
#
#       Copyright 2015 INRIA - CIRAD - INRA
#
#       File author(s): Simon Artzet <simon.artzet@gmail.com>
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
#       =======================================================================

"""
Write the doc here...
"""

__revision__ = ""

#       =======================================================================
#       External Import 
import numpy as np

import glob
import cv2
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3
import pickle


# =======================================================================
#       Local Import
import alinea.phenomenal.calibration_chessboard as cc
import alinea.phenomenal.calibration_tools as calibration_tools
import alinea.phenomenal.reconstruction_3d as reconstruction_3d
import tools_test


# =======================================================================
#       Code


def get_parameters():
    directory = '../../local/data/CHESSBOARD/'
    files = glob.glob(directory + '*.png')
    angles = map(lambda x: int((x.split('_sv')[1]).split('.png')[0]), files)

    images = dict()
    for i in range(len(files)):
        images[angles[i]] = cv2.imread(files[i], cv2.CV_LOAD_IMAGE_GRAYSCALE)

    return images


def test_calibration():
    chessboard = cc.Chessboard(47, 8, 6)

    # print " find chessboard pts on each image"
    # images = get_parameters()
    # cv_pts = {}
    # for alpha, img in images.items():
    #     print alpha
    #     pts = cc.find_chessboard_corners(img, chessboard.shape)
    #     if pts is not None:
    #         cv_pts[alpha] = pts[:, 0, :]
    #
    # with open("buffer.pkl", 'wb') as f:
    #     pickle.dump(cv_pts, f)

    with open("buffer.pkl", 'rb') as f:
        cv_pts = pickle.load(f)

    with open("initial guess.pkl", 'rb') as f:
        guess = list(pickle.load(f))

    # cc.plot_calibration(chessboard, cv_pts, guess, 48)
    cal = cc.find_calibration_model_parameters(chessboard, cv_pts, guess)
    # cal.print_value()
    cal.write_calibration("fitted - result")


def test_compute_rotation_and_translation_vectors():
    my_calibration = cc.Calibration.read_calibration(
        'my_calibration')

    my_calibration.print_value()

    angles = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]

    calibration_tools.compute_rotation_vectors(
        my_calibration.rotation_vectors, angles)
    my_calibration.write_calibration('calibration')
    calibration_tools.plot_vectors(my_calibration.rotation_vectors)

    calibration_tools.compute_translation_vectors(
        my_calibration.translation_vectors, angles)
    my_calibration.write_calibration('calibration')
    calibration_tools.plot_vectors(my_calibration.translation_vectors)


def test_reconstruction_3d():

    my_calibration = cc.Calibration.read_calibration(
        'fitted - fmt')

    #directory = '../../local/data/tests/Samples_binarization_2/'
    # directory = '../../local/data/tests/Samples_binarization_3/'
    # directory = '../../local/data/tests/Samples_binarization_4/'
    directory = '../../local/data/tests/Samples_binarization_5/'


    files = glob.glob(directory + '*.png')
    angles = map(lambda x: int((x.split('\\')[-1]).split('.png')[0]), files)

    images = dict()
    for i in range(len(files)):
        if True or angles[i] < 120:
            images[angles[i]] = cv2.imread(files[i],
                                           cv2.CV_LOAD_IMAGE_GRAYSCALE)



    octree_result = reconstruction_3d.reconstruction_3d(
        images, my_calibration, 10)

    tools_test.show_cube(octree_result, 9, "OpenCv")

    # reconstruction_3d.reprojection_3d_objects_to_images(
    #     images, octree_result, my_calibration)
    #
    # import alinea.phenomenal.calibration_manual as calibration_manual
    # camera_configuration = calibration_manual.CameraConfiguration()
    # my_calibration = calibration_manual.Calibration(camera_configuration)
    # my_calibration.print_value()
    # octree_result = reconstruction_3d.reconstruction_3d_manual_calibration(
    #     images, my_calibration, 1)
    #
    # tools_test.show_cube(octree_result, 1, "Manual")



#       =======================================================================
#       TEST

if __name__ == "__main__":
    # test_calibration()
    # test_compute_rotation_and_translation_vectors()
    test_reconstruction_3d()
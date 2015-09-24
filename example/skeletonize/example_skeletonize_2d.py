# -*- python -*-
#
#       example_skeletonize_2d.py.py : 
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
#       ========================================================================

#       ========================================================================
#       External Import
import cv2


#       ========================================================================
#       Local Import
import alinea.phenomenal.skeletonize_2d
import alinea.phenomenal.result_viewer
import phenomenal.example.example_tools


#       ========================================================================
#       Code


def run_example(data_directory):
    pot_ids = phenomenal.example.example_tools.load_files(
        data_directory + 'repair_processing/')

    for pot_id in pot_ids:
        for date in pot_ids[pot_id]:

            files = pot_ids[pot_id][date]

            images = phenomenal.example.example_tools.load_images(
                files, cv2.IMREAD_UNCHANGED)

            skeleton_images = example_skeletonize(images)

            print pot_id, date
            for angle in skeleton_images:
                alinea.phenomenal.result_viewer.show_images(
                    [images[angle], skeleton_images[angle]], str(angle))

            phenomenal.example.example_tools.write_images(
                data_directory + 'skeletonize_2d/', files, skeleton_images)


def example_skeletonize(images):
    skeleton_images = dict()
    for angle in images:
        skeleton_images[angle] = \
            alinea.phenomenal.skeletonize_2d.skeletonize_thinning(images[angle])

    return skeleton_images

#       ========================================================================
#       LOCAL TEST

if __name__ == "__main__":
    run_example('../../local/data_set_0962_A310_ARCH2013-05-13/')
    # run_example('../../local/B73/')

    # run_example('../../local/Figure_3D/')

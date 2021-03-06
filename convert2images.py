import face_recognition
import cv2
import os


def extract_face(img):
    face_locations = face_recognition.face_locations(frame)
#提取臉的資料
    faces = []
    for top, right, bottom, left in face_locations:
        face = img[top: bottom, left:right]
        faces.append(face)

    return faces


# the folder containing all the input data
input_folder = 'D:\\CBSR_database'

# the folder to store the output results
output_image_folder = 'D:\\CBSR_database.images'
'''輸入輸出影片圖片資料夾'''
# list all the item of the input folder
items = os.listdir(input_folder)
'''輸入矩陣清單'''
# make all the items full-path

    for i in range(len(items)):
    '''顯示字符串中每个字符及其索引值。'''

    items[i] = '{0}\\{1}'.format(input_folder, items[i])
''''設定格式輸入資料夾'''

while len(items) > 0:
    # pop the first folder from folders

    item = items.pop(0)
    # check the type of the item

    if os.path.isdir(item):
        '''判斷路徑'''
        # the item is type of folder so append it to folders
        # print('folder: {0}\n'.format(item))
        # list all the items in the item

        sub_items = os.listdir(item)
        '''返回到了指定資料夾'''
        for i in range(len(sub_items)):
            items.append('{0}\\{1}'.format(item, sub_items[i]))
    elif os.path.isfile(item) :
        # the item is type of file so append it to folders
        '''該項目是文件類型，因此將其附加到文件夾'''
        print('file: {0}'.format(item))

        new_folder = item[:item.rfind('\\')]
        new_folder = new_folder.replace(input_folder, output_image_folder)
        filename_face = item[item.rfind('\\')+1:item.rfind('.avi')]
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
            print('New folder created: {}'.format(new_folder))

        # if item[-4:].lower() == '.avi':
        cap = cv2.VideoCapture(item)
        # 1. open the avi file and read each frame
        frame_no = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imwrite('{0}\\{1}_{2:0>3d}.png'.format(new_folder, filename_face, frame_no), frame)
            else:
                print("[Error] Probably because of the end of the video.")
                break

            frame_no = frame_no + 1
        cap.release()
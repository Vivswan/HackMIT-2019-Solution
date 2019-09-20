import os

import cv2
import numpy as np

FOLDER = "shards-Vivswan_dfe32d"

global_link = [
    [71,  32, 274, 416, 88, 532, 562, 40, 500, 682, 556, 698, 95, 736, 0, 112, 60, 614, 541, 62, 186, 376, 294, 172, 44,
     681, 618, 467, 26, 598, 103, 489, 72, 105, 229, 196, 21, 649, 420, 744, 158, 409, 713, 1, 216, 759, 272, 278, 173,
     407, 680, 24, 347, 101, 507, 658, 231, 53, 59, 477, 244, 351, 394, 567, 389, 455, 493, 487, 213, 335, 123, 47, 252,
     491, 685, 13, 503, 701, 139, 651, 411, 230, 362, 331, 136, 217, 293],
    [607, 12, 697, 577, 422, 688, 157, 43, 2, 289, 328, 683, 219, 10, 276, 153, 587, 312, 354, 150, 28, 585, 458, 355,
     609, 708, 233, 436, 212, 198, 425, 205, 257, 486, 584, 259, 156, 586, 574, 613, 675, 582, 194, 740, 70, 160, 245,
     669, 544, 98, 659, 350, 549, 548, 590, 468, 750, 551, 695, 148, 564, 557, 25, 629, 490, 370, 131, 241, 705, 702,
     679, 166, 451, 142, 6, 251, 543, 29, 315, 221, 79, 305]  # 160
]


# for xx in range(0, 760):
#     found = False
#     for yy in range(0, len(global_link)):
#         if xx in global_link[yy]:
#             found = True
#     if not found:
#         print(xx)
#         break


def best_r_prediction(i, links):
    global FOLDER
    img1 = cv2.imread(os.path.join(FOLDER, 'shard-' + str(i) + ".png"), cv2.IMREAD_UNCHANGED)
    reduce_dict = {}
    for j in range(0, 760):
        if j not in links:
            img2 = cv2.imread(os.path.join(FOLDER, 'shard-' + str(j) + ".png"), cv2.IMREAD_UNCHANGED)
            # combine_img = np.concatenate((img1, img2), axis=1)

            fimg2 = cv2.flip(img2, 1)

            reduce_dict[j] = np.add.reduce(np.add.reduce(
                cv2.add(cv2.subtract(img1, fimg2), cv2.subtract(fimg2, img1))[:, -1]
            ))

            # print(j,
            #       np.add.reduce(img1[:, -1]),
            #       np.add.reduce(img2[:, -1]),
            #       np.add.reduce(cv2.subtract(img1, fimg2)[:, -1]),
            #       np.add.reduce(cv2.subtract(fimg2, img1)[:, -1]),
            #       np.add.reduce(cv2.add(cv2.subtract(img1, fimg2), cv2.subtract(fimg2, img1))[:, -1]),
            #       np.add.reduce(np.add.reduce(cv2.add(cv2.subtract(img1, fimg2), cv2.subtract(fimg2, img1))[:, -1]))
            #       )
            # print(j, np.add.reduce(np.add.reduce(cv2.add(cv2.subtract(img1, fimg2), cv2.subtract(fimg2, img1))[:, -1])))

            # print(j, (img1[:, -1] / 256)[0], (img2[:, -1] / 256)[0],
            #       ((cv2.subtract(img1, fimg2))[:, -1] / 256)[0],
            #       ((cv2.subtract(fimg2, img1))[:, -1] / 256)[0],
            #       (cv2.add(cv2.subtract(img1, fimg2), cv2.subtract(fimg2, img1))[:, -1] / 256)[0])
    min_index = None
    minimum = None
    for k in range(0, 760):
        if k not in links:
            if min_index is None:
                min_index = k
                minimum = reduce_dict[k]
            if minimum > reduce_dict[k]:
                min_index = k
                minimum = reduce_dict[k]

    return min_index, minimum


def best_l_prediction(i, links):
    global FOLDER
    img1 = cv2.imread(os.path.join(FOLDER, 'shard-' + str(i) + ".png"), cv2.IMREAD_UNCHANGED)
    reduce_dict = {}
    for j in range(0, 760):
        if j not in links:
            img2 = cv2.imread(os.path.join(FOLDER, 'shard-' + str(j) + ".png"), cv2.IMREAD_UNCHANGED)
            # combine_img = np.concatenate((img1, img2), axis=1)

            fimg2 = cv2.flip(img2, 1)

            reduce_dict[j] = np.add.reduce(np.add.reduce(
                cv2.add(cv2.subtract(img1, fimg2), cv2.subtract(fimg2, img1))[:, 0]
            ))

    min_index = None
    minimum = None
    for k in range(0, 760):
        if k not in links:
            if min_index is None:
                min_index = k
                minimum = reduce_dict[k]
            if minimum > reduce_dict[k]:
                min_index = k
                minimum = reduce_dict[k]

    return min_index


def main():
    i = 0
    links = [i]
    img = cv2.imread(os.path.join(FOLDER, 'shard-' + str(i) + ".png"), cv2.IMREAD_UNCHANGED)
    next_img = i
    concat_img = img
    while len(links) < 800:
        min_index, minimum = best_r_prediction(next_img, links)
        links.append(min_index)
        # min_index = best_l_prediction(next_img, links)
        # links.insert(0, min_index)

        probable_img = cv2.imread(os.path.join(FOLDER, 'shard-' + str(min_index) + ".png"), cv2.IMREAD_UNCHANGED)

        concat_img = np.concatenate((concat_img, probable_img), axis=1)
        # concat_img = np.concatenate((probable_img, concat_img), axis=1)

        cv2.imshow('image', concat_img)
        # cv2.moveWindow('image', 30, 30)
        # cv2.imshow('fimage', np.concatenate((img1, probable_img2), axis=1))
        # cv2.moveWindow('fimage', 230, 30)
        # cv2.imshow('subtracted_img', cv2.subtract(img1, probable_img2) + cv2.subtract(probable_img2, img1))
        # cv2.moveWindow('subtracted_img', 430, 30)

        # print(minimum)
        print(len(links), links)
        next_img = min_index
        cv2.waitKey(0)
        concat_img = probable_img
    cv2.destroyAllWindows()

    # link = {}
    # for j in range(0, 760):
    #     link[j] = [best_l_prediction(j, [j]), j, best_r_prediction(j, [j])]
    #     print(link[j])
    # print(link)
    #
    # link = {}
    # next_check = 0
    # link[next_check] = None
    # link[next_check] = best_r_prediction(next_check, link.keys())
    # print(next_check)
    # next_check = link[next_check]
    # print(next_check)
    # while next_check != 0:
    #     link[next_check] = None
    #     link[next_check] = best_r_prediction(next_check, link.keys())
    #     next_check = link[next_check]
    #     print(next_check)


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/16 20:10
# @Author  : suxiaorui

import numpy as np
import cv2


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


def getGrayDiff(img, currentPoint, tmpPoint):
    return abs(int(img[currentPoint.x, currentPoint.y]) - int(img[tmpPoint.x, tmpPoint.y]))


def selectConnects():
    connects = [Point(-1, -1), Point(0, -1), Point(1, -1), Point(1, 0), Point(1, 1), \
                Point(0, 1), Point(-1, 1), Point(-1, 0)]  # 8邻域

    return connects


def regionGrow(img, seeds, thresh):
    height, weight = img.shape
    seedMark = np.zeros(img.shape)
    seedList = []
    for seed in seeds:
        seedList.append(seed)
    label = 1
    connects = selectConnects()

    while (len(seedList) > 0):
        currentPoint = seedList.pop(0)
        seedMark[currentPoint.x, currentPoint.y] = label
        for i in range(8):
            tmpX = currentPoint.x + connects[i].x
            tmpY = currentPoint.y + connects[i].y
            if tmpX < 0 or tmpY < 0 or tmpX >= height or tmpY >= weight:
                continue
            grayDiff = getGrayDiff(img, currentPoint, Point(tmpX, tmpY))
            if grayDiff < thresh and seedMark[tmpX, tmpY] == 0:
                seedMark[tmpX, tmpY] = label
                seedList.append(Point(tmpX, tmpY))
    return seedMark


if __name__ == '__main__':
    img = cv2.imread('lena.bmp', 0)
    ret1, th1 = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
    seeds = [Point(10, 10)]
    binaryImg = regionGrow(th1, seeds, 10)
    cv2.imshow(' ', binaryImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

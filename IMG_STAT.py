import numpy as np


class IMG_STAT:
    # return the min of the pic

    @staticmethod
    def Minimum(stat):
        return [x[0] for x in stat.extrema]

    # return the max of the pic

    @staticmethod
    def Maximum(stat):
        return [x[1] for x in stat.extrema]

    # return the mean of the pic

    @staticmethod
    def Mean(stat):
        return stat.mean

    # return the median of the pic

    @staticmethod
    def Median(stat):
        return stat.median

    # return the percentile of the pic

    @staticmethod
    def Percentile(img, p):
        data = np.asarray(img)  # NumPy uses the asarray() class to convert PIL images into NumPy
        percentile = np.percentile(data, p)  # Compute the p-th percentile of the data
        return percentile


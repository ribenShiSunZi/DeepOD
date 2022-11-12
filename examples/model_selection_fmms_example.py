import examples.utils as utils
from deepod.model_selection.fmms import FMMS
import os
import numpy as np

random_state = 0


def get_path():
    FEATURE_FILE = os.path.join("data/feature.csv")
    TARGET_FILE = os.path.join("data/target.csv")
    return FEATURE_FILE, TARGET_FILE


if __name__ == '__main__':
    FEATURE_FILE, TARGET_FILE = get_path()
    p_train, f_train = utils.get_data(FEATURE_FILE, TARGET_FILE)
    f_test = np.array([1.227677502, 0.547297297, 0.25, 0.013513514, 0.234693979, 0.121621622, 8.222222222, 28.71360895, 9.512437578,
                      -0.52749456, 13.58201658, 0.817380952, 0.758373016, 0.843551587, 0.829662698, 0.61265873, 0.54952381, -2.106840516,
                      2.106840516, 2.890371758, 4.997212274, 15, 4, 18, 0, 148, 0, 0, 3, 0.446808511, -0.350354369, -0.558601676,
                      0, 0, 0, 5, 0.2, 5.387046595, 2.302843498, 0.330402533, 2.208985222, 8, 2.933333333, 2, 1.569146973, 44])
    rfmms = FMMS()
    rfmms.fit(f_train, p_train, save_path='./data/fmms.pt')
    rfmms.predict(f=f_test, topn=5, load_path='./data/fmms.pt')

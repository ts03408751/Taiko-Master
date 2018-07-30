import logging
import os

# constant
RIGHT_HAND = 0
LEFT_HAND = 1

# io.arm
BASE_PATH = os.path.dirname(os.path.realpath(__file__))
LEFT_PATH = os.path.join(BASE_PATH, '../data/bb_left_forearm_csv/')
RIGHT_PATH = os.path.join(BASE_PATH, '../data/bb_right_forearm_csv/')

# io.record
TABLE_PATH = os.path.join(BASE_PATH, '../data/taiku_tables/')
PLAY_TABLE_PATH = os.path.join(TABLE_PATH, 'taiko_play.csv')
SONG_TABLE_PATH = os.path.join(TABLE_PATH, 'taiko_song.csv')
DRUMMER_TABLE_PATH = os.path.join(TABLE_PATH, 'taiko_drummer.csv')

STAT_COLS = ['AAI', 'AVI', 'ASMA', 'GAI', 'GVI', 'GSMA', 'AAE', 'ARE',
             'MAMI', 'MGMI', 'ASDI', 'GSDI', 'AIR', 'GIR',
             'AZCR', 'GZCR', 'AMCR', 'GMCR',
             'AXYCORR', 'AYZCORR', 'AZXCORR', 'GXYCORR', 'GYZCORR', 'GZXCORR']

COND_COLS = ['L2', 'L1', 'R1', 'R2']

ZERO_ADJ_COL = ['imu_ax', 'imu_ay', 'imu_az', 'imu_gx', 'imu_gy', 'imu_gz', 'msu_ax', 'msu_ay', 'msu_az']

ALL_COLUMNS = ['timestamp', 'wall_time', 'imu_temp',
               'imu_ax', 'imu_ay', 'imu_az',
               'imu_gx', 'imu_gy', 'imu_gz',
               'msu_ax', 'msu_ay', 'msu_az',
               'baro_temp', 'baro']

SENSOR_COLUMNS = [ALL_COLUMNS[0]] + ALL_COLUMNS[2:]
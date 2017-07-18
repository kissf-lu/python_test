from class_test.class_test import SaveConfig
from os.path import realpath, join, split
print(join(SaveConfig.DATA_DIR, "path"))


print(split(realpath(__file__))[0])
print(split(split(realpath(__file__))[0])[0])
print(split(split(split(realpath(__file__))[0])[0])[0])
print(join(split(split(split(realpath(__file__))[0])[0])[0], 'data'))
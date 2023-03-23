import json
import os
print(os.getcwd() + r'\test_cloud_saas.xlsx')
print(os.path.abspath(os.path.join(os.getcwd(), "../..")) + r'\all.yaml')


import yaml
extractfile = r"../../2022-12\2023-1\extract.txt"
# 提取变量文件路径
yaml_load = r"D:\python\2022-12\2023-1/"
# yaml用例文件路径
all_yaml = r"D:\python\2022-12\2023-1\all.yaml"
# 全局变量文件路径
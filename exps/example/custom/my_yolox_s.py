#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.
import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "datasets/GTA_Dataset"
        self.train_ann = "train_data_annotate.json"
        self.val_ann = "val_data_annotate.json"

        self.input_size = (1056, 1920)
        self.test_size = (1056, 1920)

        self.num_classes = 1

        self.max_epoch = 300
        self.data_num_workers = 2
        self.eval_interval = 1



# Copyright (c) OpenMMLab. All rights reserved.

# Please refer to https://mmengine.readthedocs.io/en/latest/advanced_tutorials/config.html#a-pure-python-style-configuration-file-beta for more details. # noqa
# mmcv >= 2.0.1
# mmengine >= 0.8.0

from mmengine.config import read_base

with read_base():
    from .rtmdet_l_8xb32_300e_coco import *

deepen_factor = 0.67
widen_factor = 0.75

model.update(
    dict(
        backbone=dict(deepen_factor=deepen_factor, widen_factor=widen_factor),
        neck=dict(deepen_factor=deepen_factor, widen_factor=widen_factor),
        bbox_head=dict(head_module=dict(widen_factor=widen_factor))
    )
)

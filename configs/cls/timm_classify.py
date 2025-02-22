from sscma.models import TimmBackbone, CrossEntropyLoss, Mixup, CutMix


# model settings
data_preprocessor = dict(
    num_classes=7,
    # RGB format normalization parameters
    mean=[123.675, 116.28, 103.53],
    std=[58.395, 57.12, 57.375],
    # convert image from BGR to RGB
    to_rgb=True,
)


model = dict(
    data_preprocessor=data_preprocessor,
    type=TimmBackbone,
    pretrained=True,
    num_classes=7,
    loss=dict(
        type=CrossEntropyLoss,
        loss_weight=1.0,
    ),
    train_cfg=dict(
        augments=[dict(type=Mixup, alpha=0.8), dict(type=CutMix, alpha=1.0)]
    ),
)

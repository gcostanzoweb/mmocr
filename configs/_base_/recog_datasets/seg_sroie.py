prefix = 'data/sroie'

train = dict(
    type='OCRSegDataset',
    img_prefix=f'{prefix}/crops/training',
    ann_file=f'{prefix}/train_label.jsonl',
    loader=dict(
        type='AnnFileLoader',
        repeat=100,
        file_format='txt',
        parser=dict(
            type='LineJsonParser', 
            keys=['file_name', 'annotations', 'text'])),
    pipeline=None,
    test_mode=False)

test = dict(
    type='OCRDataset',
    img_prefix=f'{prefix}/crops/test',
    ann_file=f'{prefix}/test_label.jsonl',
    loader=dict(
        type='AnnFileLoader',
        repeat=1,
        file_format='txt',
        parser=dict(
            type='LineJsonParser',
            keys=['filename', 'text'])),
    pipeline=None,
    test_mode=True)

train_list = [train]

test_list = [test]
dataset_type = 'IcdarDataset'
data_root = 'data/bid'

train = dict(
    type=dataset_type,
    ann_file=f'{data_root}/instances_training.json',
    #loader=dict(
    #    type='AnnFileLoader',
    #    parser=dict(
    #        type='LineJsonParser',
    #        keys=['filename', 'text'])),
    img_prefix=f'{data_root}/imgs',
    pipeline=None)

test = dict(
    type=dataset_type,
    ann_file=f'{data_root}/instances_val.json',
    #loader=dict(
    #    type='AnnFileLoader',
    #    parser=dict(
    #        type='LineJsonParser',
    #        keys=['filename', 'text'])),
    img_prefix=f'{data_root}/imgs',
    pipeline=None)

train_list = [train]

test_list = [test]

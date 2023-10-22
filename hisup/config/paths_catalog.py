import os
import os.path as osp

class DatasetCatalog(object):

    DATA_DIR = osp.abspath(osp.join(osp.dirname(__file__),
                '..','..','data'))
    # Original definition of DATASETS
    # DATASETS = {
    #     'crowdai_train_small': {
    #         'img_dir': 'crowdai/train/images',
    #         'ann_file': 'crowdai/train/annotation-small.json'
    #     },
    #     'crowdai_test_small': {
    #         'img_dir': 'crowdai/val/images',
    #         'ann_file': 'crowdai/val/annotation-small.json'
    #     },
    #     'crowdai_train': {
    #         'img_dir': 'crowdai/train/images',
    #         'ann_file': 'crowdai/train/annotation.json'
    #     },
    #     'crowdai_test': {
    #         'img_dir': 'crowdai/val/images',
    #         'ann_file': 'crowdai/val/annotation.json'
    #     },
    #     'inria_train': {
    #         'img_dir': 'inria/train/images',
    #         'ann_file': 'inria/train/annotation.json',
    #     },
    #     'inria_test': {
    #         'img_dir': 'coco-Aerial/val/images',
    #         'ann_file': 'coco-Aerial/val/annotation.json',
    #     }
    # }
    DATASETS = {
        'Ngu2018_train': {
            'img_dir': 'Ngu2018/train/images',
            'ann_file': 'Ngu2018/train/annotation.json'
        },
        'Ngu2017_train': {
            'img_dir': 'Ngu2017/train/images',
            'ann_file': 'Ngu2017/train/annotation.json'
        },
        'Nduta2017_train': {
            'img_dir': 'Nduta2017/train/images',
            'ann_file': 'Nduta2017/train/annotation.json'
        },
        'Minawao2017_train': {
            'img_dir': 'Minawao2017/train/images',
            'ann_file': 'Minawao2017/train/annotation.json'
        },
        'Kutupalong2017_train': {
            'img_dir': 'Kutupalong2017/train/images',
            'ann_file': 'Kutupalong2017/train/annotation.json'
        },
        'Kutupalong2018_train': {
            'img_dir': 'Kutupalong2018/train/images',
            'ann_file': 'Kutupalong2018/train/annotation.json'
        },
        'Kule2017_train': {
            'img_dir': 'Kule2017/train/images',
            'ann_file': 'Kule2017/train/annotation.json'
        },
        'Kule2018_train': {
            'img_dir': 'Kule2018/train/images',
            'ann_file': 'Kule2018/train/annotation.json'
        },
        'Djibo2019_train': {
            'img_dir': 'Djibo2019/train/images',
            'ann_file': 'Djibo2019/train/annotation.json'
        },
        'Dagaha2017_train': {
            'img_dir': 'Dagaha2017/train/images',
            'ann_file': 'Dagaha2017/train/annotation.json'
        }
    }

    @staticmethod
    def get(name):
        assert name in DatasetCatalog.DATASETS
        data_dir = DatasetCatalog.DATA_DIR
        attrs = DatasetCatalog.DATASETS[name]

        args = dict(
            root = osp.join(data_dir,attrs['img_dir']),
            ann_file = osp.join(data_dir,attrs['ann_file'])
        )

        if 'train' in name:
            return dict(factory="TrainDataset",args=args)
        if 'test' in name and 'ann_file' in attrs:
            return dict(factory="TestDatasetWithAnnotations",
                        args=args)
        raise NotImplementedError()

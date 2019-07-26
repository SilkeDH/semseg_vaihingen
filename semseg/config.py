# -*- coding: utf-8 -*-
"""
   Module to define CONSTANTS used across the project
"""

from os import path

# identify basedir for the package
BASE_DIR = path.dirname(path.normpath(path.dirname(__file__)))


train_args = { 'data_path': {'default': '/srv/semseg/data',
                             'help': 'Location of vaihingen_train.hdf5 and vaihingen_val.hdf5',
                             'required': False
                             },
               'model': {'default': '/srv/semseg/models/resnet50_fcn_weights.hdf5',
                         'help': 'Location + name of the output model \
                         (e.g., /srv/semseg/models/resnet50_fcn_weights.hdf5)',
                         'required': False
                        },
               'augmentation': {'default': False,
                                 'choices': [False, True],
                                 'help': 'Apply augmentation',
                                 'required': False
                                },
               'transfer_learning': {'default': False,
                                      'choices': [False, True],
                                      'help': 'Use transfer learning and load pre-trained weights',
                                      'required': False
                                    },
               'n_gpus':   {'default': 1,
                            'help': 'Number of GPUs to train on (one node only!)',
                            'required': False
                           },
               'n_epochs': {'default': 20,
                            'help': 'Number of epochs to train on',
                            'required': False 
                           },
               'batch_size':  {'default': 16,
                               'help': 'Number of samples per batch',
                               'required': False
                              }
}

#    parser.add_argument('--data_path', type=str,
#                        help='Location of vaihingen_train.hdf5 and vaihingen_val.hdf5 \
#                        (e.g., /homea/hpclab/train002/semseg/data/ )')
#    parser.add_argument('--model', type=str,
#                        help='Location + name of the output model \
#                        (e.g., /homea/hpclab/train002/semseg/models/resnet50_fcn_weights.hdf5)')
#    parser.add_argument('--log', type=str,
#                        help='Location + name of the csv log file')  

# -*- coding: utf-8 -*-
"""
   Module to define CONSTANTS used across the project
"""

from os import path

# identify basedir for the package
BASE_DIR = path.dirname(path.normpath(path.dirname(__file__)))

DATA_DIR = path.join(BASE_DIR,'data') # Location of model data and output files
MODEL_PATH = path.join(BASE_DIR,'models','resnet50_fcn_weights.hdf5') # Location + name of the output model
MODEL_REMOTE_PUBLIC = 'https://nc.deep-hybrid-datacloud.eu/s/eTqJexZ5PcBxXR6/download?path='
NUM_LABELS = 6  # max number of labels

train_args = { 'augmentation': {'default': False,
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

predict_args = {'model_retrieve':   {'default': False,
                             'choices': [False, True],
                             'help': 'Force model update from the remote repository',
                             'required': False
                           },

}

#    parser.add_argument('--log', type=str,
#                        help='Location + name of the csv log file')  

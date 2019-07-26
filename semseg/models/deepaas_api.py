# -*- coding: utf-8 -*-
"""
Model description
"""
import json
import yaml
import argparse
import pkg_resources
from keras import backend
# import project's config.py
import semseg.config as cfg
import semseg.models.train_resnet50_fcn as train_resnet50

from datetime import datetime

def get_metadata():
    """
    Function to read metadata
    """

    module = __name__.split('.', 1)

    pkg = pkg_resources.get_distribution(module[0])
    meta = {
        'Name': None,
        'Version': None,
        'Summary': None,
        'Home-page': None,
        'Author': None,
        'Author-email': None,
        'License': None,
        'Train-Args': cfg.train_args
    }

    for line in pkg.get_metadata_lines("PKG-INFO"):
        for par in meta:
            if line.startswith(par):
                _, value = line.split(": ", 1)
                meta[par] = value

    return meta


def predict_file(*args):
    """
    Function to make prediction on a local file
    """
    message = 'Not implemented in the model (predict_file)'
    return message


def predict_data(*args):
    """
    Function to make prediction on an uploaded file
    """
    message = 'Not implemented in the model (predict_data)'
    return message


def predict_url(*args):
    """
    Function to make prediction on a URL
    """
    message = 'Not implemented in the model (predict_url)'
    return message


###
# Uncomment the following two lines
# if you allow only authorized people to do training
###
#import flaat
#@flaat.login_required()
def train(train_args):
    """
    Train network
    train_args : dict
        Json dict with the user's configuration parameters.
        Can be loaded with json.loads() or with yaml.safe_load()    
    """

    run_results = { "status": "ok",
                    "train_args": {},
                    "training": {},
                  }

    run_results["train_args"] = train_args

    # Clear possible pre-existing sessions. important!
    backend.clear_session()


    if (yaml.safe_load(train_args.augmentation)):
        params = train_resnet50.train_with_augmentation(
                                      yaml.safe_load(train_args.data_path),
                                      yaml.safe_load(train_args.model),
                                      yaml.safe_load(train_args.augmentation),
                                      yaml.safe_load(train_args.transfer_learning),
                                      yaml.safe_load(train_args.n_gpus),
                                      yaml.safe_load(train_args.n_epochs),
                                      yaml.safe_load(train_args.batch_size))
    else:
        params = train_resnet50.train(yaml.safe_load(train_args.data_path),
                                      yaml.safe_load(train_args.model),
                                      yaml.safe_load(train_args.augmentation),
                                      yaml.safe_load(train_args.transfer_learning),
                                      yaml.safe_load(train_args.n_gpus),
                                      yaml.safe_load(train_args.n_epochs),
                                      yaml.safe_load(train_args.batch_size))
    
    run_results["training"] = yaml.safe_load(json.dumps(params._asdict(), 
                                                        default=str))

    print("Run results: " + str(run_results))
    return run_results


def get_train_args():
    """
    Returns a dict of dicts to feed the deepaas API parser
    """
    train_args = cfg.train_args

    # convert default values and possible 'choices' into strings
    for key, val in train_args.items():
        val['default'] = str(val['default']) #yaml.safe_dump(val['default']) #json.dumps(val['default'])
        if 'choices' in val:
            val['choices'] = [str(item) for item in val['choices']]

    return train_args


# during development it might be practical 
# to check your code from the command line
def main():
    """
       Runs above-described functions depending on input parameters
       (see below an example)
    """

    if args.method == 'get_metadata':
        get_metadata()       
    elif args.method == 'train':
        train(args)
    else:
        get_metadata()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Model parameters')

    # get arguments configured for get_train_args()
    train_args = get_train_args()
    for key, val in train_args.items():
        parser.add_argument('--%s' % key,
                            default=val['default'],
                            type=type(val['default']),
                            help=val['help'])

    parser.add_argument('--method', type=str, default="get_metadata",
                        help='Method to use: get_metadata (default), \
                        predict_file, predict_data, predict_url, train')
    args = parser.parse_args()

    main()

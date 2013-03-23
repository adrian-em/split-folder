"""
Split a big folder into X smaller folders
"""
import os
from docopt import docopt
import shutil
import logging

__version__ = '0.0.2'
__author__ = 'aesptux'
logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)
ARGS = """
Usage:
    splitfolder.py <folder> <newfoldername> <elements>

Help:
folder: absolute path to the folder to split
newfoldername: Name for the new folders
elements: Each folder will contain N elements
    splitfolder.py /home/user/mybigfolder set 200
This will split the folder /home/user/mybigfolder into several named set
(set_1, set_2, set_3...) and each folder will contain 200 elements
Please, use absolute folders.

"""


def check_folder(folder):
    """
    Test if folder exists and is absolute
    """
    if os.path.isdir(folder):
        if os.path.isabs(folder):
            return True
        else:
            raise ValueError("The path to the folder must be absolute")
    else:
        raise OSError("Can't find the path.")


def folder_creator(newfoldername, counter):
    """
    Handler to create folder
    """
    LOG.info("Entering. creator")
    counter = int(counter)
    counter += 1
    LOG.info("Value of counter is {0}".format(counter))
    try:
        LOG.info("Enter try.")
        foldername = "../{0}_{1}".format(newfoldername, str(counter))
        #print foldername
        LOG.info("Foldername is {0}".format(foldername))
        os.mkdir('{0}'.format(foldername))
        return {'foldername': foldername, 'counter': counter}
    except OSError:
        LOG.info("OSError raised")
        return folder_creator(newfoldername, counter)


def main(folder, newfoldername, elements):
    """
    Main
    """
    check_folder(folder)
    LOG.info("Entering. main")
    elements = int(elements)
    counter = 0
    os.chdir(folder)
    files_gen = (x for x in filter(os.path.isfile, os.listdir('.')))
    #foldername = "set_{0}".format(str(counter))
    for value, elem in enumerate(files_gen):
        if value % elements == 0:
            returned_dict = folder_creator(newfoldername, counter)
            counter = returned_dict['counter']
            foldername = returned_dict['foldername']
            LOG.info("Value of counterMAIN is {0}".format(counter))
            LOG.info("FoldernameMAIN is {0}".format(foldername))

        print "Moving {0}".format(elem)
        shutil.move(elem, foldername)

if __name__ == '__main__':
    ARGUMENTS = docopt(ARGS, version=__version__)
    main(folder=ARGUMENTS['<folder>'],
        newfoldername=ARGUMENTS['<newfoldername>'],
        elements=ARGUMENTS['<elements>'])

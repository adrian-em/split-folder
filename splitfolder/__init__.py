__title__ = "splitfolder"
__version__ = '0.0.2'
__author__ = 'aesptux'
__license__ = "BSD"
__description__ = """
split-folder
Split a big folder into several.

During my tests, it took 6 minutes and 51 seconds to split 37006 files
into folders of 300 items.

Usage
splitfolder.py <folder> <newfoldername> <elements>
folder: absolute path to the folder to split

newfoldername: Name for the new folders

elements: Each folder will contain N elements

Example

splitfolder.py /home/user/mybigfolder set 200
It will split /home/user/mybigfolder into several folders named 'set' each 200
 items.
"""
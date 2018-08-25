#!/usr/bin/env python
import os
import shutil
from optparse import OptionParser
from hashlib import md5


def parse_and_validate_options():
    parser = OptionParser('usage %prog [options] <source directory> <destination directory>')
    parser.add_option('-d',
                      '--dryrun',
                      dest='dryrun',
                      help='Dry run only, no copying will take place',
                      action='store_true',
                      default=False)
    (opts, args) = parser.parse_args()
    if len(args) == 0:
        parser.error('Missing source and destination directories')
    elif len(args) == 1:
        parser.error('Missing destination directory')
    return (opts, args)


def track_files(source_dir, destination_dir):
    source_dir = os.path.abspath(source_dir)
    destination_dir = os.path.abspath(destination_dir)
    operations = []
    if not os.path.isdir(source_dir):
        raise RuntimeError('Invalid source directory "%s"' % source_dir)
    if not os.path.isdir(destination_dir):
        raise RuntimeError('Invalid destination directory "%s"' % destination_dir)
    for (path, dirs, files) in os.walk(source_dir):
        # print 'Scanning "%s"' % path
        if os.path.islink(path):
            print 'Skipping symbolicly linked directory "%s"' % path
            continue
        for file in files:
            source_filename = os.path.join(path, file)
            if os.path.islink(source_filename):
                print 'Skipping symbolicly linked file "%s"' % source_filename
                continue
            relative_path = path_subtract(path, source_dir)
            # print 'Relative path: %s' % relative_path
            destination_filename = os.path.join(destination_dir, relative_path, file)
            # print 'Source: %s\nDestination: %s' % (source_filename, destination_filename)
            if os.path.isfile(destination_filename):
                # File exists, see if they are different
                source_md5 = md5_file(source_filename)
                destination_md5 = md5_file(destination_filename)
                if source_md5 != destination_md5:
                    # MD5s do not match, add to the operation list
                    operations.append((source_filename, destination_filename, 'm',))
                else:
                    pass
                    # print 'Skipping "%s"' % source_filename
            else:
                # File does not exist in destination tree
                operations.append((source_filename, destination_filename, 'a',))
    return operations


def md5_file(fn, buffer=1024*64):
    hasher = md5()
    with open(fn, 'r') as infile:
        done = False
        while not done:
            data = infile.read(buffer)
            if not data:
                done = True
            hasher.update(data)
    return hasher.hexdigest()


def path_subtract(current_path, starting_path):
    return_value = None
    index = current_path.find(starting_path)
    if index != -1:
        index += len(starting_path)
    else:
        raise RuntimeError('There was subtracting "%s" from "%s"' % (starting_path, current_path))
    return_value = current_path[index:]
    if return_value and return_value[0] == '/':
        return_value = return_value[1:]
    return return_value


if __name__ == '__main__':
    (opts, args) = parse_and_validate_options()
    operations = track_files(args[0], args[1])
    if len(operations) == 0:
        print '"%s" contained everything in "%s"' % (args[1], args[0])
    else:
        if opts.dryrun:
            for (source, dest, modifier) in operations:
                print '"%s" (%s) would have been copied to "%s"' % (source, modifier, dest)
        else:
            print 'Preparing to copy %i files' % len(operations)
            for (source, dest, modifier) in operations:
                path = os.path.split(dest)[0]
                if not os.path.isdir(path):
                    os.makedirs(path)
                shutil.copyfile(source, dest)
                print 'Copied "%s" to "%s"' % (source, dest)

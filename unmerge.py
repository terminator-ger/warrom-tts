import os
import pdb
def get_folder(line):
    path = line.split(' ')[1]
    path, file =  os.path.split(path)
    file = file.rstrip()
    return path, file


if __name__ == '__main__':
    with open('merge.txt','r') as mergefile:
        lines = mergefile.readlines()
        idx = 0
        outfile = None
        current_folder = None
        current_file = None
        parent_folder = 'warroom-tts'
        os.makedirs(os.path.join('.', parent_folder), exist_ok=True)
        global_file = open(os.path.join(parent_folder, 'global.ttslua'), 'w+')

        while idx < len(lines):
            line = lines[idx]
            if '----#include' in line:
                folder, file = get_folder(line)
                if outfile is not None:
                    outfile.close()
                    outfile = None
                    print("close {}/{}".format(current_folder, current_file))

                if folder != current_folder or file != current_file:
                    print('open file {}/{}'.format(folder, file))
                    os.makedirs(os.path.join('.', parent_folder, folder), exist_ok=True)
                    outfile = open(os.path.join('.', parent_folder, folder, "{}.ttslua".format(file)), 'w+')
                    current_file = file
                    current_folder = folder
                    global_file.write('#include {}/{}\n'.format(folder, file))

            if outfile is not None:
                outfile.write(line)
            idx += 1
        global_file.close()

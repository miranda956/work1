import os ;

import sys;

def main():

    if len(sys.argv) > 2:
        print(__doc__)
        sys.exit(1)        
    elif len(sys.argv) == 2:
        dir = sys.argv[1]
    else:
        dir = '.'         

    if not os.path.isdir(dir):
        print('error: {} does not exists'.format(dir))
        sys.exit(1)

    for curr_dir, subdirs, files in os.walk(dir):

        print('D:', os.path.abspath(curr_dir))    
        for subdir in sorted(subdirs):  
            print('SD:', os.path.abspath(subdir))
        for file in sorted(files):      
            print(os.path.join(os.path.abspath(curr_dir), file))  

if __name__ == '__main__':
    main()

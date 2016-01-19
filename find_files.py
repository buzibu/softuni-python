def main():
    import sys
    import os

    if len(sys.argv)<3:
        print('\nNot enough parameters! \nUsage: \npython find_files.py <path to folder> <filename>')
        return
    if not os.path.exists(sys.argv[1]):
        print("\n{} Does not exist!".format(sys.argv[1]))
        return

    folder_name = sys.argv[1]
    file_name = sys.argv[2]

    print("\nSearch for: {} in {}".format(file_name,folder_name))
    print('\nResults:\n ')
    results = False
    # print(file_name[0])
    # print(file_name[-1])
    for root, dirs, files in os.walk(folder_name):
        if file_name[0] == '*':
            # print(file_name[1:])
            for name in files:
                # print(name[-(len(file_name[1:])):])
                if file_name[1:] == name[-(len(file_name[1:])):]:
                    results = True
                    print(os.path.join(root, name))
        elif file_name[-1] == '*':
            # print(file_name[:-1])
            for name in files:
                # print(name[:len(file_name[:-1])])
                if file_name[:-1] == name[:len(file_name[:-1])]:
                    results = True
                    print(os.path.join(root, name))
        else:
            for name in files:
                if name == file_name:
                    results = True
                    print(os.path.join(root, file_name))
    if not results:
        print("Not found")

if __name__ == '__main__':
    main()
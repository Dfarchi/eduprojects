UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#C:\Users\Documents\my files\doc1.docx
#C:\sdfsdf.txt

#/Users/valeria/src/qgis_technion/qgis_test_proj.qgz

path = input("Insert path: ")

# /a.t
if len(path) < 4:
    print("Too short for a path")
    exit(1)

if not path.startswith("/") and path[0] not in UPPERCASE:
    print("Does not start from / for linux-based or uppercase letter for DOS-based systems")
    exit(1)

# windows path check
if path[0] in UPPERCASE:
    if path[1:3] != ':\\':
        print("Invalid prefix for windows path")
    else:
        # valid prefix for windows
        path_parts = path[3:].split("\\")
        filename = path_parts[-1]
        if not filename or "." not in filename:
            print("Invalid filename")
        else:
            # valid filename - get extension
            filename_parts = filename.split(".")
            # filename = ".".join(filename_parts[:-1])
            extension = filename_parts[-1]
            depth = path.count("\\") - 1
            print(f"The provided path is valid!\nDepth: {depth}\nFilename: {filename}\nExtension: {extension}")


# linux-based path - try on your own!!!

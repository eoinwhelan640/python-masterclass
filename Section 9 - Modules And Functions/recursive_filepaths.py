import os

listing = os.walk(".")


def list_directories(s):
    def dir_lists(d):
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                # The deal with tab stop is for our printout to look nice
                # each time it finds a dir it indents one more, then comes back when
                # its completed recursion through all things in that dir
                tab_stop += 1
                dir_lists(current_dir)
                # We have tab stop as a local variable defined in list_directories
                # so because dir_list is nested, it is available there too, kinda like how a global works
                # I think this is considered to be the enclosed scope
                # Also, python to save mem shunts tab_stop in local scope of nested dir_list function
                # so it can pick it up faster unless overwritten
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_lists(s)
    else:
        print(s + " does not exist")


# Doing it without nonlocal keyword
# def list_directories(s):
#     def dir_lists(d, tabs):
#         files = os.listdir(d)
#         for f in files:
#             current_dir = os.path.join(d, f)
#             if os.path.isdir(current_dir):
#                 print("\t" * tabs + "Directory " + f)
#                 tabs += 1
#                 dir_lists(current_dir,tabs)
#                 tabs -= 1
#             else:
#                 print("\t" * tabs + f)
#
#     if os.path.exists(s):
#         print("Directory listing of " + s)
#         dir_lists(s, 0)
#     else:
#         print(s + " does not exist")





list_directories('.')
import os
if os.path.isdir('C:\\CA SOFTWARES') == True:
    if os.path.isfile("C:\\CA SOFTWARES\\dir.txt") == True:
        a = open("C:\\CA SOFTWARES\\dir.txt", 'w')
        b = a.write("C:\\Users\\Admin\\Desktop\\CA SOFTWARES")
        a.close()
        c = open("C:\\CA SOFTWARES\\dir.txt", 'r')
        k_dir = c.read()
        c.close()
        import os
        import argparse

        print('C:\\Users\\Admin\\Desktop\\CA SOFTWARES')


        def ls():
            parser = argparse.ArgumentParser(description='List Files In A Directory')
            parser.add_argument('directory', type=str, nargs='?', default='.')
            parser.add_argument('--all', '-a', action='store_true', help="Include dotfiles in listing")
            args = parser.parse_args()
            dirs = os.listdir(args.directory)
            if args.all:
                dirs += [os.curdir, os.pardir]
            for fn in os.listdir('C:\\Users\\Admin\\Desktop\\CA SOFTWARES'):
                print("---", fn)


        if __name__ == "__main__":
            ls()
        while True:
            c = open("C:\\CA SOFTWARES\\dir.txt", 'r')
            k_dir = c.read()
            c.close()
            print(k_dir)
            qw = input(">: ")
            if qw == "os.ls":
                import os
                import argparse


                def ls():
                    parser = argparse.ArgumentParser(description='List Files In A Directory')
                    parser.add_argument('directory', type=str, nargs='?', default='.')
                    parser.add_argument('--all', '-a', action='store_true', help="Include dotfiles in listing")
                    args = parser.parse_args()
                    dirs = os.listdir(args.directory)
                    if args.all:
                        dirs += [os.curdir, os.pardir]
                    for fn in os.listdir(k_dir):
                        print("---", fn)


                if __name__ == "__main__":
                    ls()
            elif qw == "os.cd":
                w_orig = input(">: ")
                if os.path.isdir(k_dir + "\\" + w_orig) == True:
                    z = k_dir + "\\" + w_orig
                    q = open("C:\\CA SOFTWARES\\dir.txt", 'w')
                    r = q.write(z)
                    q.close()
                elif os.path.isdir(k_dir + "\\" + w_orig) == False:
                    print("No Such Diretry Found", w_orig)
            elif qw == 'vipe':
                u_i = input('>: ')
                if os.path.isfile(k_dir + "\\" + u_i) == True:
                    import os

                    os.startfile(k_dir + "\\" + u_i)
                else:
                    print('No Such File Found', u_i, "On Path", k_dir)
            elif qw == "os.cd.c":
                zxc = "C:\\"
                av = open('C:\\CA SOFTWARES\\dir.txt', 'w')
                r = av.write(zxc)
                av.close()
            elif qw == "os.cd.f":
                zxc = "F:\\"
                av = open('C:\\CA SOFTWARES\\dir.txt', 'w')
                r = av.write(zxc)
                av.close()
            elif qw == "os.cd.e":
                zxc = "E:\\"
                av = open('C:\\CA SOFTWARES\\dir.txt', 'w')
                r = av.write(zxc)
                av.close()
            elif qw == 'exit()':
                break
            elif qw == 'exit':
                print('Enter Exit() To Exit')
            elif a == 'dd':
                c = open("C:\\CA SOFTWARES\\dir.txt", 'w')
                c.write('C:\\Users\\Admin\\Desktop\\CA SOFTWARES')
                c.close()
else:
    print('First Avtivate CA')
    while True:
        l = input("")

import pip
packages = ['Pyqt5', 'nltk', 'torch', 'numpy', 'json']


def import_or_install(package):
    try:
        for i in package:
            __import__(i)

    except ImportError:
        for i in package:
            pip.main(['install',i])

if __name__ == '__main__':
    import_or_install(packages)
from distutils.core import setup

setup(
    name='ProblemArchive',
    version='1.0.0',
    packages=['ProblemArchive'],
    url='',
    license='',
    author='SajadBanooie',
    author_email='sajadbanooie@gmail.com',
    description='archive your problems and manage them',
    requires=['pyqt5', 'pony'],
    # package_data={'ProblemArchive': ['database.sqlite']},
    scripts=['problem'],
)

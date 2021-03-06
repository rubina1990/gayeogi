from lettuce import step, world, after, before
from gayeogi.main import version
from gayeogi.db import local
import os
import shutil
import logging

class Handler(logging.Handler):
    def __init__(self, logs, level = logging.DEBUG):
        logging.Handler.__init__(self, level)
        self.logs = logs
    def emit(self, record):
        self.logs.append(record.msg)

@before.all
def init():
    world.basedir = os.path.dirname(__file__)
    world.renames = list()
    world.exchanges = set()
    world.directory = list()
    world.logs = list()
    world.ignores = list()
    world.expected = (version, {}, {}, {}, {}, [True])
    world.expected_logs = list()
    world.data = {
        'data': (
            0, u'clockwork_test.mp3',
            (
                u'Anthony Burgess', u'1962', u'A Clockwork Orange',
                u'01', u'Sweet Hommie'
            )
        ),
        'data2': (
            1, u'second_dir_test.m4a',
            (
                u'An Artist', u'1692', u'Second Dir',
                u'1', u'Discovery'
            )
        ),
    }

@after.all
def deinit(total):
    shutil.move(
        os.path.join(world.basedir, u'temp', u'sweet_hommie.mp3'),
        world.directory[0][0]
    )
    for (old, new) in world.renames:
        os.rename(old, new)
    for ex in world.exchanges:
        os.remove(ex)
    os.remove(os.path.join(world.directory[0][0], u'second_test.flac'))

def __add_to_expected(arg):
    (one, two) = arg
    partial = world.expected[1].setdefault(one[0], {})
    partial = partial.setdefault(one[1], {})
    partial = partial.setdefault(one[2], {})
    partial = partial.setdefault(one[3], {})
    partial = partial.setdefault(one[4], {})
    partial[u'path'] = one[5]
    partial = world.expected[2].setdefault(two[0], {})
    partial[u'artist'] = one[0]
    partial[u'date'] = one[1]
    partial[u'album'] = one[2]
    partial[u'tracknumber'] = one[3]
    partial[u'title'] = one[4]
    partial[u'modified'] = two[1]
    partial = world.expected[4].setdefault(one[0] + one[1] + one[2], {})
    partial[u'remote'] = set()
    partial[u'digital'] = True
    partial[u'analog'] = False

@step('I have some files in "(.*)" directory')
def have_some_files(step, directory):
    world.directory.append((os.path.join(world.basedir, directory), 2))
    (world.index, test, data) = world.data[directory]
    clockwork_test = os.path.join(world.directory[world.index][0], test)
    __add_to_expected((
        data + (clockwork_test,),
        (clockwork_test, os.stat(clockwork_test).st_mtime)
    ))

@step('I add "(.*)" pattern')
def add_pattern(step, pattern):
    world.ignores.append((pattern, 2))

def __add_pattern_data(pattern):
    system_test = os.path.join(world.directory[0][0],
        pattern, u'system_volume_test.mp3')
    __add_to_expected((
        (
            u'Windows', u'1985', u'Volume Information',
            u'xxx', u'System', system_test
        ),
        (system_test, os.stat(system_test).st_mtime)
    ))
def __remove_pattern_data(pattern):
    del world.expected[1][u'Windows']
    del world.expected[2][os.path.join(world.directory[0][0],
        pattern, u'system_volume_test.mp3')]
    del world.expected[4][u'Windows1985Volume Information']

@step('I disable "(.*)" pattern')
def disable_pattern(step, pattern):
    __add_pattern_data(pattern)
    world.db.actualize(ignores = [(pattern, 0)])

@step('I enable "(.*)" pattern')
def enable_pattern(step, pattern):
    __remove_pattern_data(pattern)
    world.db.actualize(ignores = [(pattern, 2)])

@step('remove "(.*)" pattern')
def remove_pattern(step, pattern):
    __add_pattern_data(pattern)
    world.db.actualize(ignores = [])

@step('I have an empty database')
def have_an_empty_database(step):
    world.database = (version, {}, {}, {}, {}, [False])
    world.db = local.Filesystem(
        world.directory,
        world.database, world.ignores
    )

@step('scan the directory for files')
def scan_the_directory(step):
    world.db.start()
    world.db.wait()

@step('they should get added to the database')
@step('they should be updated in the database')
@step('it should be removed from the database')
def should_get_added(step):
    assert world.database == world.expected, "\n" + repr(world.database) + "\n" + repr(world.expected)

@step('I add some more files to the directory')
def add_some_more_files(step):
    shutil.copy2(os.path.join(world.basedir, u'temp/second_test.flac'),
        os.path.join(world.basedir, u'data'))
    second_test = os.path.join(world.directory[world.index][0], u'second_test.flac')
    __add_to_expected((
        (
            u'Second', u'0000', u'Test',
            u'666', u'ST', second_test
        ),
        (
            os.path.join(world.directory[world.index][0], u'second_test.flac'),
            os.stat(second_test).st_mtime
        )
    ))

@step('I rename file "(.*)" to "(.*)"')
def rename_file(step, oldname, newname):
    oldpath = os.path.join(world.directory[world.index][0], oldname)
    newpath = os.path.join(world.directory[world.index][0], newname)
    os.rename(oldpath, newpath)
    world.renames.append((newpath, oldpath))
    world.expected[2][newpath] = world.expected[2][oldpath]
    world.expected[2][newpath][u'modified'] = os.stat(newpath).st_mtime
    del world.expected[2][oldpath]
    world.expected[1][u'Anthony Burgess'][u'1962'][u'A Clockwork Orange']\
        [u'01'][u'Sweet Hommie'][u'path'] = newpath

@step('I change (artist|date|album|tracknumber|title) tag for file "(.*)"')
def change_tags_for_file(step, tag, filename):
    oldpath = os.path.join(world.directory[world.index][0], filename)
    if tag == 'artist':
        world.expected[1][u'Changed'] = world.expected[1][u'Second']
        del world.expected[1][u'Second']
        world.expected[2][oldpath][u'artist'] = u'Changed'
        world.expected[4][u'Changed0000Test'] =\
            world.expected[4][u'Second0000Test']
        del world.expected[4][u'Second0000Test']
    elif tag == 'date':
        world.expected[1][u'Changed'][u'1111'] =\
            world.expected[1][u'Changed'][u'0000']
        del world.expected[1][u'Changed'][u'0000']
        world.expected[2][oldpath][u'date'] = u'1111'
        world.expected[4][u'Changed1111Test'] =\
            world.expected[4][u'Changed0000Test']
        del world.expected[4][u'Changed0000Test']
    elif tag == 'album':
        world.expected[1][u'Changed'][u'1111'][u'Changed'] =\
            world.expected[1][u'Changed'][u'1111'][u'Test']
        del world.expected[1][u'Changed'][u'1111'][u'Test']
        world.expected[2][oldpath][u'album'] = u'Changed'
        world.expected[4][u'Changed1111Changed'] =\
            world.expected[4][u'Changed1111Test']
        del world.expected[4][u'Changed1111Test']
    elif tag == 'tracknumber':
        world.expected[1][u'Changed'][u'1111'][u'Changed'][u'777'] =\
            world.expected[1][u'Changed'][u'1111'][u'Changed'][u'666']
        del world.expected[1][u'Changed'][u'1111'][u'Changed'][u'666']
        world.expected[2][oldpath][u'tracknumber'] = u'777'
    elif tag == 'title':
        world.expected[1][u'Changed'][u'1111'][u'Changed'][u'777'][u'Ch'] =\
            world.expected[1][u'Changed'][u'1111'][u'Changed'][u'777'][u'ST']
        del world.expected[1][u'Changed'][u'1111'][u'Changed'][u'777'][u'ST']
        world.expected[2][oldpath][u'title'] = u'Ch'
    newpath = os.path.join(world.basedir,
        u'temp', tag + u'_change_test_.flac')
    oldnewpath = os.path.join(world.basedir,
        u'temp', tag + u'_change_test.flac')
    shutil.copy(oldpath, newpath)
    shutil.copy(oldnewpath, oldpath)
    world.exchanges.add(newpath)
    world.expected[2][oldpath][u'modified'] = os.stat(oldpath).st_mtime

@step('I remove file "(.*)"')
def remove_file(step, filename):
    oldpath = os.path.join(world.directory[world.index][0], filename)
    shutil.move(oldpath, os.path.join(world.basedir, u'temp'))
    del world.expected[1][u'Anthony Burgess']
    del world.expected[2][oldpath]
    del world.expected[4][u'Anthony Burgess1962A Clockwork Orange']

@step('I remove the "(.*)" directory')
def remove_directory(step, directory):
    del world.expected[1][u'Changed']
    del world.expected[2][os.path.join(world.directory[0][0], u'second_test.flac')]
    del world.expected[4][u'Changed1111Changed']
    __remove_pattern_data(u'System Volume Information')
    world.db.actualize(directory = [world.directory[1]])

@step('I disable the "(.*)" directory')
def disable_directory(step, directory):
    world.expected = (version, {}, {}, {}, {}, [True])
    world.db.actualize(directory = [(world.directory[1][0], 0)])

@step('I enable the "(.*)" directory')
def enable_directory(step, directory):
    (world.index, test, data) = world.data[directory]
    clockwork_test = os.path.join(world.directory[world.index][0], test)
    __add_to_expected((
        data + (clockwork_test,),
        (
            os.path.join(world.directory[world.index][0], test),
            os.stat(clockwork_test).st_mtime
        )
    ))
    world.db.actualize(directory = [(world.directory[1][0], 2)])

@step('prepare a logger')
def prepare_a_logger(step):
    logger = logging.getLogger('gayeogi.local')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(Handler(world.logs))
    world.db.actualize(
        directory = world.db.directories + [(world.directory[0][0], 2)]
    )
    world.expected_logs = [
        [u'Anthony Burgess', u'Something has been added.'],
        [u'Changed', u'Something has been added.'],
        [u'Windows', u'Something has been added.'],
        [u'Second', u'Something has been changed.'],
        [u'Changed', u'Something has been removed.'],
        [u'Anthony Burgess', u'Something has been removed.']
    ]

@step('I add a file "(.*)"')
def add_a_file(step, filename):
    shutil.copy2(
        os.path.join(world.basedir, u'temp', filename),
        world.directory[0][0]
    )

@step('I replace new "(.*)" with the old one')
def replace_new_with_the_old_one(step, filename):
    shutil.copy2(
        os.path.join(world.basedir, u'temp', u'second_test.flac'),
        world.directory[0][0]
    )

@step('remove file named "(.*)"')
def remove_file_named(step, filename):
    os.remove(os.path.join(world.directory[0][0], filename))

@step('proper logs should be generated')
def proper_logs_should_be_generated(step):
    assert world.logs == world.expected_logs, "\n" + repr(world.logs) + "\n" + repr(world.expected_logs)
    del world.logs[:]
    del world.expected_logs[:]

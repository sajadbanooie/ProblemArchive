from pony.orm import *

db = Database("sqlite", "database.sqlite", create_db=True)


class Problem(db.Entity):
    name = PrimaryKey(unicode, 50)
    diff = Required(int, default=0)
    url = Required(unicode, 50, nullable=True)
    solved = Required(bool, default=False)
    tags = Optional(LongUnicode)
    story = Optional(LongUnicode)
    contest = Optional("Contest")


class Contest(db.Entity):
    name = PrimaryKey(unicode, 50)
    diff = Required(int, default=0)
    url = Required(unicode, 50, nullable=True)
    tags = Optional(LongUnicode)
    problems = Set(Problem)


# sql_debug(True)
db.generate_mapping(create_tables=True)


@db_session
def get_problems():
    return select(p for p in Problem)[:]


@db_session
def get_unassigned_problems():
    return select(p for p in Problem if p.contest is None)[:]


@db_session
def get_problems_a():
    plist = select(p for p in Problem)[:]
    plist.sort(key=lambda x: x.name)
    return plist


@db_session
def get_problems_d():
    plist = select(p for p in Problem)[:]
    plist.sort(key=lambda x: x.diff)
    return plist


@db_session
def get_contests():
    return select(c for c in Contest)[:]


@db_session
def get_problem(name):
    return Problem.get(name=name)


@db_session
def get_contest(name):
    return Contest.get(name=name)


@db_session
def get_contests_a():
    plist = select(p for p in Contest)[:]
    plist.sort(key=lambda x: x.name)
    return plist


@db_session
def get_contests_d():
    plist = select(p for p in Contest)[:]
    plist.sort(key=lambda x: x.diff)
    return plist


@db_session
def add_problem(name, diff, url, tags, story, solved):
    Problem(name=name, diff=diff, url=url, tags=tags, story=story, solved=solved)


@db_session
def add_contest(name, diff, url, tags, problems):
    c = Contest(name=name, diff=diff, url=url, tags=tags)
    for n in problems:
        c.problems.add(Problem[n])


@db_session
def modify_problem(name, new_name, diff, url, tags, story, solved):
    Problem[name].diff = diff
    Problem[name].url = url
    Problem[name].tags = tags
    Problem[name].story = story
    Problem[name].solved = solved
    Problem[name].name = new_name


@db_session
def modify_contest(name, new_name, diff, url, tags, problems):
    Contest[name].diff = diff
    Contest[name].url = url
    Contest[name].tags = tags
    for p in Contest[name].problems:
        if p.name not in problems:
            Contest[name].problems.remove(p)
    for n in problems:
        Contest[name].problems.add(Problem.get(name=n))
    Contest[name].name = new_name


@db_session
def problem_search(name=None, tags=None, diff=None):
    if name and diff:
        plist = select(p for p in Problem if name in p.name and p.diff == diff)[:]
    elif name:
        plist = select(p for p in Problem if name in p.name)[:]
    elif diff:
        plist = select(p for p in Problem if p.diff == diff)[:]
    else:
        plist = select(p for p in Problem)[:]
    if tags:
        tags = tags.split(',')
        for p in plist:
            for t in tags:
                if t not in p.tags:
                    plist.remove(p)
    return plist


@db_session
def contest_search(name=None, tags=None, diff=None):
    if name and diff:
        plist = select(p for p in Contest if name in p.name and p.diff == diff)[:]
    elif name:
        plist = select(p for p in Contest if name in p.name)[:]
    elif diff:
        plist = select(p for p in Contest if p.diff == diff)[:]
    else:
        plist = select(p for p in Contest)[:]
    if tags:
        tags = tags.split(',')
        for p in plist:
            for t in tags:
                if t not in p.tags:
                    plist.remove(p)
    return plist

import sqlite3 as sq


async def db_start():
    global db, cur

    db = sq.connect('my.db')
    cur = db.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, photo TEXT, name TEXT, age TEXT, descr TEXT)')

    db.commit()


async def create_profile(user_id):
    user = cur.execute("select 1 from profile where user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("insert into profile values(?, ?, ?, ?, ?)", (user_id, '', '', '', ''))
        db.commit()


async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute(
            "UPDATE PROFILE SET photo = '{}', age = '{}', descr='{}', name='{}' WHERE user_id=='{}'".format(data[
                                                                                                                'photo'],
                                                                                                            data['age'],
                                                                                                            data[
                                                                                                                'descr'],
                                                                                                            data[
                                                                                                                'name'],
                                                                                                            user_id))
        db.commit()

import sqlite3

connect = sqlite3.connect('ncode_questions.db')
cur = connect.cursor()

# cur.execute('CREATE TABLE lesson_solution(id INTEGER PRIMARY KEY AUTOINCREMENT, lesson_no INTEGER UNIQUE, solution TEXT NOT NULL)')

# cur.execute('INSERT INTO lesson_solution (lesson_no, solution) VALUES(?, ?)', (2, "Unlocked"))
# cur.execute('INSERT INTO lesson_solution (lesson_no, solution) VALUES(?, ?)',
#             (3, "Solution of lesson 3"))
# connect.commit()

parms = (2,)
res = cur.execute(
    'SELECT solution FROM lesson_solution WHERE lesson_no=?', parms)
row = res.fetchone()
print(row)
connect.close()

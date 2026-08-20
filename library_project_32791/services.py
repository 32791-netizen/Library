from database import connect_db
def add_book(book_id, title, author, category):
conn = connect_db()
cur = conn.cursor()
cur.execute("""
INSERT INTO books(book_id, title, author, category)
VALUES (?, ?, ?, ?)
""", (book_id, title, author, category))
conn.commit()
conn.close()
print("บันทึกข้อมูลหนังสือส าเร็จ")
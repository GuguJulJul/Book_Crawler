from DB import MysqlController

class CrawlingBookDAO(MysqlController):
  def insert(self, crawlingBook):
    sql = 'INSERT INTO crawling_book (title, author_name, img_url, created_at) ' + 'VALUES (' + crawlingBook.to_sql_str() + ')'
    print(sql)
    self.cursor.execute(sql)
    self.connection.commit()
    
  def selectByName(self, bookTitle):
    sql = 'SELECT * FROM crawling_book WHERE title LIKE \'' + bookTitle + '\''
    self.cursor.execute(sql)
    result = self.cursor.fetchall()
    return result
from DB import MysqlController

class CrawlingBookDAO(MysqlController):
  def insert(self, crawlingBook):
    sql = 'INSERT INTO crawling_book (title, author_name, img_url, created_at) ' + 'VALUES (' + crawlingBook.to_sql_str() + ')'
    print(sql)
    self.cursor.execute(sql)
    self.connection.commit()
    
  
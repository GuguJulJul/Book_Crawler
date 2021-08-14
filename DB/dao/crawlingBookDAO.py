from DB import MysqlController

class CrawlingBookDAO(MySqlController):
  def insert(self, crawlingBook):
    sql = 'INSERT INTO crawling_book (title, author_name, img_url, created_at) ' + \
    'VALUES (' + crawlingBook.to_sql_str() + ')'

    self.cursor.excute(sql)
    self.connection.commit()
    
  
class CrawlingBook:
    def __init__(self):
        self.id = 0
        self.title = ''
        self.author_name = ''
        self.img_url = ''
        self.create_at = ''

    def to_sql_str(self):
      sql_str = '\'' + self.title + '\', \'' + self.author_name + '\', \'' + self.img_url + '\', \'' + self.create_at + '\''
      return sql_str
      
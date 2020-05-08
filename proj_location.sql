postgreSQL_select_Query = "select * from VIDEO_TABLE where municipality = %s"

cursor.execute(postgreSQL_select_Query, (location,))

postgreSQL_select_Query = "select * from PODCAST_TABLE where municipality = %s"

cursor.execute(postgreSQL_select_Query, (location,))

postgreSQL_select_Query = "select * from ARTICLE_TABLE where municipality = %s"

cursor.execute(postgreSQL_select_Query, (location,))


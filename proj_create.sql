CREATE TABLE USERS (
User_ID char(2) PRIMARY KEY,
user_name text UNIQUE,
password text,
email text,
User_type text,
f_name text,
l_name text
);

CREATE TABLE VIDEO_TABLE (
Video_ID char(2) PRIMARY KEY,
video_topic text,
video_description text,
video_title text,
municipality text,
author text,
upload_date text
);

CREATE TABLE PODCAST_TABLE (
Podcast_ID char(2) PRIMARY KEY,
title text,
author text,
municipality text,
upload_date text
);

CREATE TABLE ARTICLE_TABLE (
Article_ID char(2) PRIMARY KEY,
title text,
upload_date text,
municipality text,
article text,
author text
);

CREATE TABLE MUNICIPALITY_TABLE (
name text,
county text,
PRIMARY KEY (name, county)
);


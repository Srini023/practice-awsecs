import os

variable_which_i_wont_use = "this is a variable which i wont use"


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_LINK")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # postgresql://postgres:password@db:5432/mydb
    # DB_LINK='postgresql://postgres:sri23sree02@practice-ecr.cjuqek26wuv5.ap-south-1.rds.amazonaws.com:5432/practiceecr'
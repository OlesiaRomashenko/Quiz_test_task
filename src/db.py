import psycopg2
from config import SettingsDB

connect_settings = SettingsDB()
connect = psycopg2.connect(host=connect_settings.host, port=connect_settings.port, dbname=connect_settings.db,
                           user=connect_settings.user, password=connect_settings.password)



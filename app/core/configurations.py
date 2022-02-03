import configparser
import os

package_path, package_filename = os.path.split(os.path.abspath(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(package_path, "data/config.ini"))

PACKAGE_PATH = package_path

MYSQL_HOSTNAME = str(config["ENVIRONENT"]["MYSQL_HOSTNAME"])
MYSQL_PORT = str(config["ENVIRONENT"]["MYSQL_PORT"])
MYSQL_DBNAME = str(config["ENVIRONENT"]["MYSQL_DBNAME"])
MYSQL_UNAME = str(config["ENVIRONENT"]["MYSQL_UNAME"])
MYSQL_PASS = str(config["ENVIRONENT"]["MYSQL_PASS"])

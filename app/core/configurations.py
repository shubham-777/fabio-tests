import configparser
import os

package_path, package_filename = os.path.split(os.path.abspath(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(package_path, "data/config.ini"))

def read_config_from_env(plst_vars):
    ldict_configs = dict()
    for lstr_sec, llst_vars in plst_vars.items():
        for lstr_var in llst_vars:
            if  lstr_var in os.environ and lstr_sec == "ENVIRONENT":
                ldict_configs[lstr_var] = os.environ.get(lstr_var)
            else:
                ldict_configs[lstr_var] = config[lstr_sec][lstr_var]
    return ldict_configs

PACKAGE_PATH = package_path

llst_vars = {"ENVIRONENT":["MYSQL_HOSTNAME", "MYSQL_PORT", "MYSQL_DBNAME", "MYSQL_UNAME", "MYSQL_PASS", "MB_USERNAME", "MB_PASS", "MB_HOSTNAME"]}
ldict_configs = read_config_from_env(llst_vars)

MYSQL_HOSTNAME = str(ldict_configs["MYSQL_HOSTNAME"])
MYSQL_PORT = str(ldict_configs["MYSQL_PORT"])
MYSQL_DBNAME = str(ldict_configs["MYSQL_DBNAME"])
MYSQL_UNAME = str(ldict_configs["MYSQL_UNAME"])
MYSQL_PASS = str(ldict_configs["MYSQL_PASS"])


MB_USERNAME = str(ldict_configs["MB_USERNAME"])
MB_PASS = str(ldict_configs["MB_PASS"])
MB_HOSTNAME = str(ldict_configs["MB_HOSTNAME"])


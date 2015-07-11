import configparser


conf = configparser.ConfigParser()
conf['Time']["MAX_TIME"] = '5'
conf['DB']['DB_NAME'] = 'classification.db'
conf['Frequency'] = {
    'MULTICOLORED_FREQUENCY': '10',
    'BLACK_BALL_FREQUENCY': '20',
    'STAR_FREQUENCY': '15',
    'NUMBERED_BALL_FREQUENCY': '30'
}

with open('configurate.cfg', 'w') as configfile:
    conf.write(configfile)
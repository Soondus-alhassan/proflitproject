# logging output of file function

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def file(filename):
    logging.debug('Start of file(%s%%)' % (filename))
    logging.debug('.' in filename and filename.rsplit('.', 1)[1].lower() in {'xlsx'})
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'xlsx'}

file('Book1.xlsx')
logging.debug('End of program')
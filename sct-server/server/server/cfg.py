#PROJECT_ROOT = '/home/isct/spinalcordtoolbox_web/server/'
PROJECT_ROOT = '/Users/willispinaud/Dropbox/spinalcordtoolbox_web/server/'
#PROJECT_ROOT = '/home/poquirion/neuropoly/spinalcordtoolbox_web/server/'

# TOOLBOX PATH
#spinalcordtoolbox = "/home/isct/spinalcordtoolbox"
spinalcordtoolbox = "/Users/willispinaud/Dropbox/Amerique/Montreal/spinalcordtoolbox"
#spinalcordtoolbox = "/home/poquirion/neuropoly/spinalcordtoolbox"
SPINALCORDTOOLBOX = "%s" % spinalcordtoolbox
SPINALCORD_BIN = "{}/bin".format(SPINALCORDTOOLBOX)
SPINALCORD_SCRIPTS = "{}/scripts".format(SPINALCORDTOOLBOX)

# Executable/plugins
# SCT_TMP_PKG = "sct_scripts" # should be final name
SCT_PYTHONPATH = ""
SCT_TMP_PKG = "scripts" # DEBUG !!!
EXEC_TMP = PROJECT_ROOT+'../{}'.format(SCT_TMP_PKG)
EXEC_PATH = PROJECT_ROOT+'../../spinalcordtoolbox/scripts'
PYHTON_NAME = "python2.7 "

# Where input files are stored
FILE_REP_TMP = PROJECT_ROOT+'server/static/tmp/'

PROCESS_LOOP_SLEEP = 0.05

TIMEOUT = 60

PEACEFUL_DEAD_CLOCK = 5


INPUT_FILE_TAG = 'INPUT_FILE'
OUTPUT_DIR_TAG = 'OUTPUT_FILE'
EXEC_DIR_TAG = 'EXEC_DIR'


GET_PARSER = 'get_parser'

PATHFSLBIN = '/usr/local/fsl/bin/'

OPTION_TRANSMIT = \
    ("default_value",
     "description",
     "help",
     "mandatory",
     "name",
     "type_value",
     "order",
     "section",
     "example")

OPTION_DEPRECATED = "deprecated"
OPTION_ORDER = "order"

SECRET_KEY = "XsWbCyWfM5jOaIH0zP8J7jLB3DB7c7UN"
SECURITY_PASSWORD_SALT = "3p98Hb8r776uGYaUqFJ01l2t0LRc7y60"

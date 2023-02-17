import logging
# Get mpi rank and size info if MPI is enabled
try:
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    mpi_rank = comm.Get_rank()
    mpi_size = comm.Get_size()
except (ModuleNotFoundError, ImportError):
    print('MPI is not enabled. Use default single rank.')
    mpi_size = 1
    mpi_rank = 0

# Set up logger
logging_level = logging.WARNING
formatstr = f"Rank {mpi_rank:04d} of size {mpi_size:04d} [%(asctime)s] %(levelname)-8s: %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(level=logging_level, format=formatstr, datefmt=datefmt)

# Instantiate logger
logger = logging.getLogger('mylogger')

# Set up a handler that will write the log messages to a file as well as to stdout
filename = 'mpi_single_logger/mpi_single_logger.log'
filehandler = logging.FileHandler(filename)
filehandler.setLevel(logger.getEffectiveLevel())

# Lets make the output messages to file formatted the same as to console
formatter = logging.Formatter(formatstr, datefmt=datefmt)
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

# Log messages
logger.debug('Debug message')
logger.warning('Warning message')
print('Change logging level. This print message does not come inbetween log messages in stdout.')
# Set logging level to DEBUG
# (Note: but filehandler did not update its level, so the log in file does not contain the debug message)
logger.setLevel(logging.DEBUG)
logger.debug('Debug')
logger.warning('Warning')


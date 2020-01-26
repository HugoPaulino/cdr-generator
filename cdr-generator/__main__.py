from .core import CDR_Generator
import sys

if __name__ == "__main__":
    print ("Start running CDR_Generator with the following params {}".format(sys.argv))
    CDR_Generator.run(sys.argv)
    print ("End running CDR_Generator")

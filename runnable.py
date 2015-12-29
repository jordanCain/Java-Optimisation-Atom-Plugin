import sys
sys.path.insert(0, r'C:\Users\Jordan\Documents\GitHub\javaParser\ASTParser')
sys.path.insert(0, r'C:\Users\Jordan\Documents\GitHub\javaParser\OptimisationDetect')
sys.path.insert(0, r'C:\Users\Jordan\Documents\GitHub\javaParser\Gui')
sys.path.insert(0, r'C:\Users\Jordan\Documents\GitHub\javaParser')
import parse
import scan
from debugUtil import Trace

#Debug levels:
#0 Dev trace        - produces extra log info in areas being written
#1 User trace       - Produces logging info to a UserTrace.txt file
#2 Service Trace    - Produces a stackTrace in StackTrace.txts
debugLevel = 2

#Run the parse and detect
def run():
    debug = Trace(debugLevel)
    if debugLevel >= 1:
        debug.writeTrace()
    fname = r"C:\Users\jordan\Documents\GitHub\javaParser\SampleJavaFiles\ADSWeek3Threading.java"
    parent = parse.read(fname, debug)
    #parent.printNode()
    optimisations = scan.detect(parent, debug)
    scan.output(optimisations)

run()

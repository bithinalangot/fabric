import sys
import subprocess
import re

result = subprocess.check_output(["/opt/gopath/src/github.com/hyperledger/fabric/verifier.zk", sys.argv[1], sys.argv[2], sys.argv[3]])
verifier = re.search("true", str(result))

if verifier:
    print 1
else:
    print 0

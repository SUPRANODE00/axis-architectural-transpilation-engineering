import sys, os
repo_root=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(repo_root)
import sys, os

repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(repo_root)

from src.axis_parser.parser import AxisParser

tokens = ["govern", "trace", "signal", "compute"]

parser = AxisParser()
ast = parser.parse(tokens)

print(ast)

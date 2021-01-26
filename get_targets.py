import sys
sys.path.insert(0, 'finviz')
import finviz

result = finviz.get_analyst_price_targets(sys.argv[1])
for x in range(len(result)):
    print(result[x])

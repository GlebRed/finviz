import sys
sys.path.insert(0, 'finviz')
import finviz

result = finviz.get_news(sys.argv[1])
for x in range(len(result)):
    print(result[x])

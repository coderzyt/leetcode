class Solution(object):

    def AstarSearch(graph, start, end):
        pq = collections.priority_queue()
        pq.append([start])
        visited.add(start)

        while pq:
            node = pq.pop()
            visited.add(node)

            process(node)
            nodes = generate_related_nodes(node)
            unvisited = [node for node in nodes if node not in visited]
            pq.push(unvisited)
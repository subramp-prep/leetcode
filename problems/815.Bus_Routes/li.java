class Solution {
    public int numBusesToDestination(int[][] routes, int S, int T) {
        HashMap<Integer, HashSet<Integer>> to_routes = new HashMap<>();
        for (int i = 0; i < routes.length; ++i)
            for (int j : routes[i]) {
                if (!to_routes.containsKey(j)) to_routes.put(j, new HashSet<Integer>());
                to_routes.get(j).add(i);
            }
        Queue<Point> bfs = new ArrayDeque();
        bfs.offer(new Point(S, 0));
        HashSet<Integer> seen = new HashSet<>();
        seen.add(S);
        while (!bfs.isEmpty()) {
            int stop = bfs.peek().x, bus = bfs.peek().y;
            bfs.poll();
            if (stop == T) return bus;
            for (int route_i : to_routes.get(stop))
                for (int next_stop : routes[route_i])
                    if (!seen.contains(next_stop)) {
                        seen.add(next_stop);
                        bfs.offer(new Point(next_stop, bus + 1));
                    }
        }
        return -1;
    }
}
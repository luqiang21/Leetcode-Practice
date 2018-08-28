// There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w. flights [u,v,w] w < 1000, n < 100

#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
  /** find the cheapest flight from src to des given n cities and m flights
  * @param n(int) # of cities
  * @param vector<vector<int>> flights
  * @param src, des: source city and destination city
  * @return cost flight cost
  */
  int findCheapetFlight(int n, vector<vector<int> > &flights, int src, int des) {
    // edge cases
    if (n == 0) return 0;
    if (flights.size() == 0) return 0;
    if (src == des) return 0;

    // general cases
    vector< vector<int> > neighbors(n, vector<int>());
    vector< vector<int> > costs(n, vector<int>());

    // fill up neighbors and costs
    for (size_t i = 0; i < flights.size(); ++i) {
      int u = flights[i][0], v = flights[i][1], w = flights[i][2];
      neighbors[u].push_back(v);
      costs[u].push_back(w);
    }

    // dijkstra search
    vector<int> cost_cities(n, 1000000);
    priority_queue<int, vector<int>, greater<int> > frontiers;
    set<int> visited;

    frontiers.push(src);
    cost_cities[src] = 0;

    while (!frontiers.empty()) {
      int city = frontiers.top();
      frontiers.pop();
      // check whether we are at des city
      if (city == des) return cost_cities[city];

      // visit city's neighbors
      for (size_t i = 0; i < neighbors[city].size(); ++i) {
        int nei = neighbors[city][i];
        if (visited.find(nei) != visited.end()) continue;

        frontiers.push(nei);
        int temp_cost = cost_cities[city] + costs[city][i];
        if (temp_cost < cost_cities[nei]) {
          cost_cities[nei] = temp_cost;
        }

        // cout << "src: " << city << " des: " << nei << " cost: " << costs[city][i] <<endl;
      }

      visited.insert(city);
    }

    return -1;

  }
};

int main() {
  vector<vector<int> > flights;

  flights.push_back({0, 1, 100});
  flights.push_back({0, 3, 1000});
  flights.push_back({1, 2, 100});
  flights.push_back({2, 3, 100});
  flights.push_back({3, 4, 500});
  flights.push_back({3, 5, 500});
  flights.push_back({1, 5, 500});
  flights.push_back({4, 5, 500});
  flights.push_back({0, 5, 700});


  Solution sln;
  cout << sln.findCheapetFlight(6, flights, 0, 5) << endl; // should be 600

}

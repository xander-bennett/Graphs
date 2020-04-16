import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        # Use add_user num_users times
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")

        # New Optimized Populate Graph Method
        target_friendships = num_users * avg_friendships // 2
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1

        print('Total Collisions: ', collisions)
        # Original Populate Graph Method (naive)
        # # Generate all friendship combinations
        # possible_friendships = []

        # # Avoid dupes by making sure first number is smaller than second
        # for user_id in self.users:
        #     for friend_id in range(user_id+1, self.last_id+1):
        #         possible_friendships.append((user_id, friend_id))

        # # Shuffle all possible friendships
        # random.shuffle(possible_friendships)

        # # Create for first X pairs x is total //2
        # for i in range(num_users * avg_friendships // 2):
        #     friendship = possible_friendships[i]
        #     self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        # Now that you have a graph full of users and friendships, you can crawl through their social graphs.
        # `get_all_social_paths()` takes a userID and returns a dictionary containing every user in that user's
        # extended network along with the shortest friendship path between each.

        # Hint 1: What kind of graph search guarantees you a shortest path? - Breadth First
        # Hint 2: Instead of using a `set` to mark users as visited, you could use a `dictionary`.
        # Similar to sets, checking if something is in a dictionary runs in O(1) time.
        # If the visited user is the key, what would the value be?

        queue = Queue()
        visited = {}  # Note that this is a dictionary, not a set
        queue.enqueue([user_id])
        # print("Initial Queue: ", queue.queue)
        while queue.size() > 0:
            path = queue.dequeue()
            # print('Path: ', path)
            # print('Queue: ', queue.queue)
            user = path[-1]
            # print('Visiting User: ', user)
            if user not in visited:
                visited[user] = path
                # print('Visited: ', visited)
                for friend in self.friendships[user]:
                    connections = list(path)
                    connections.append(friend)
                    # print('Connections: ', connections)
                    queue.enqueue(connections)
                    # print('Queue: ', queue.queue)
        count = 0

        for node in visited:
            count += len(visited[node])

        average = count / len(visited)
        return visited, average


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)

    # For this particular random sample below, it should print...
    print('Social Network: ', sg.friendships)
    # {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}

    connections = sg.get_all_social_paths(1)
    print('Shortest Path Connections: ', connections)
    # For the above random friendship sample, it will return the following connections:
    # {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}

    # Note that in this sample, Users 3, 4 and 9 are not in User 1's extended social network.
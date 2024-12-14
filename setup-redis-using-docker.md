Running Redis in Docker is a straightforward and efficient way to get started. Here’s how you can set it up:

---

### **Steps to Run Redis in Docker**

1. **Pull the Redis Image**:
   - Open your terminal and run:
     ```bash
     docker pull redis
     ```
   - This will download the latest Redis image from Docker Hub.

2. **Run a Redis Container**:
   - Start a Redis container with:
     ```bash
     docker run --name redis-container -d -p 6379:6379 redis
     ```
   - Explanation:
     - `--name redis-container`: Gives the container a recognizable name.
     - `-d`: Runs the container in detached mode (in the background).
     - `-p 6379:6379`: Maps port 6379 on your machine to port 6379 in the container (default Redis port).

3. **Verify Redis is Running**:
   - Check running containers:
     ```bash
     docker ps
     ```
   - You should see your Redis container in the list.

4. **Connect to Redis**:
   - Use a Redis client, like `redis-cli` or a GUI client (e.g., RedisInsight), to connect.
   - If you have `redis-cli` installed locally, run:
     ```bash
     redis-cli -h 127.0.0.1 -p 6379
     ```
   - Inside Docker, you can connect directly by:
     ```bash
     docker exec -it redis-container redis-cli
     ```

5. **Persist Data (Optional)**:
   - By default, the Redis container stores data in memory only. To persist data between restarts:
     ```bash
     docker run --name redis-container -d -p 6379:6379 -v /my/local/path:/data redis redis-server --save 60 1 --dir /data
     ```
     - Replace `/my/local/path` with a directory on your machine.

6. **Stop and Remove the Container**:
   - Stop the container:
     ```bash
     docker stop redis-container
     ```
   - Remove the container:
     ```bash
     docker rm redis-container
     ```

---

### Redis basics
Welcome to the Redis CLI! Here’s a quick crash course on what you can do and the basic commands to get started.

---

### **1. Basic Key-Value Commands**
Redis primarily works as a key-value store. You can store and retrieve data like this:

- **Set a Key-Value Pair**:
  ```bash
  SET key value
  ```
  Example:
  ```bash
  SET name "Alice"
  ```

- **Get a Value by Key**:
  ```bash
  GET key
  ```
  Example:
  ```bash
  GET name
  ```

- **Delete a Key**:
  ```bash
  DEL key
  ```
  Example:
  ```bash
  DEL name
  ```

- **Check if a Key Exists**:
  ```bash
  EXISTS key
  ```
  Example:
  ```bash
  EXISTS name
  ```
  - Returns `1` if the key exists, `0` otherwise.

- **Get All Keys**:
  ```bash
  KEYS pattern
  ```
  Example:
  ```bash
  KEYS *
  ```
  - Lists all keys in the database. You can use patterns like `user:*` to match specific keys.

---

### **2. Working with Data Structures**
Redis supports several data structures:

#### **Strings (default key-value pairs)**
- **Increment/Decrement**:
  ```bash
  INCR key
  DECR key
  ```
  Example:
  ```bash
  SET counter 10
  INCR counter   # 11
  DECR counter   # 10
  ```

#### **Hashes (like objects or dictionaries)**
- **Set a Field in a Hash**:
  ```bash
  HSET hash_name field value
  ```
  Example:
  ```bash
  HSET user:1001 name "Alice" age "30"
  ```

- **Get a Field Value**:
  ```bash
  HGET hash_name field
  ```
  Example:
  ```bash
  HGET user:1001 name
  ```

- **Get All Fields and Values**:
  ```bash
  HGETALL hash_name
  ```
  Example:
  ```bash
  HGETALL user:1001
  ```

#### **Lists (ordered collections)**
- **Add Elements to a List**:
  ```bash
  LPUSH list_name value
  RPUSH list_name value
  ```
  Example:
  ```bash
  LPUSH tasks "task1"
  RPUSH tasks "task2"
  ```

- **Get Elements from a List**:
  ```bash
  LRANGE list_name start end
  ```
  Example:
  ```bash
  LRANGE tasks 0 -1
  ```
  - Retrieves all elements (`0` is the start, `-1` means the end).

#### **Sets (unordered collections of unique values)**
- **Add Elements to a Set**:
  ```bash
  SADD set_name value
  ```
  Example:
  ```bash
  SADD colors "red" "blue" "green"
  ```

- **Get All Elements in a Set**:
  ```bash
  SMEMBERS set_name
  ```
  Example:
  ```bash
  SMEMBERS colors
  ```

- **Check if a Value Exists in a Set**:
  ```bash
  SISMEMBER set_name value
  ```
  Example:
  ```bash
  SISMEMBER colors "red"
  ```

#### **Sorted Sets (sets with a score for sorting)**
- **Add Elements with Scores**:
  ```bash
  ZADD sorted_set_name score value
  ```
  Example:
  ```bash
  ZADD leaderboard 100 "Alice"
  ZADD leaderboard 200 "Bob"
  ```

- **Get Elements by Score**:
  ```bash
  ZRANGE sorted_set_name start end WITHSCORES
  ```
  Example:
  ```bash
  ZRANGE leaderboard 0 -1 WITHSCORES
  ```

---

### **3. Persistence and Administration**
- **Save Data to Disk**:
  ```bash
  SAVE
  ```
  - Performs a synchronous save.

- **Check Memory Usage of a Key**:
  ```bash
  MEMORY USAGE key
  ```

- **Flush All Data (Careful!)**:
  ```bash
  FLUSHALL
  ```
  - Deletes all data in Redis.

- **Switch Between Databases**:
  Redis supports multiple logical databases (default is 0).
  ```bash
  SELECT db_number
  ```
  Example:
  ```bash
  SELECT 1
  ```

---

### **4. Monitoring and Debugging**
- **Monitor All Redis Commands in Real Time**:
  ```bash
  MONITOR
  ```

- **View Key Expiration Time**:
  ```bash
  TTL key
  ```
  Example:
  ```bash
  TTL name
  ```

- **Set an Expiration Time for a Key**:
  ```bash
  EXPIRE key seconds
  ```
  Example:
  ```bash
  EXPIRE name 60
  ```

---

### **5. Exiting Redis CLI**
- Type `QUIT` or press `Ctrl+C` to exit.
---

These commands should get you started with exploring Redis.

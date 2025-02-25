# Object Pool Design pattern

its a creational pattern that manages a pool or a cache or reusable obejcts. it aims
to improve performance and resource utilization by reusing objects instead of creating
new ones. this pattern is particularly useful when the cost of obejct creation,
Initialization, or destruction is high.

In obejct Pool pattern, a pool of object is created and managed by pool manager
when an object is neded, instead of creating a new objects from scratch the pool
manager provide an existing obejcts from the pool. When obejct is no longer needed
it return the pool to future reuse. This way overhead of obejct creation and
destruction is reduced.

By using the objects from the pool instead of creating new ones. the object pool
pattern can improve performance, reduce memory consumption, and minimize the overhead
of object creation and destruction.

It worth noting that the object pool pattern shoudl be used when the cost of objects
creation and Initialization is high, and the numebr of objects needed is variable
if the number of objects needed is fixed or low, the benifit of the object pool
pattern may be diminished.

# Real word use case

1. dataBase connection pool: database intensive applications, managing a pool of
   pre-initialized database connections allows for efficient reuse, reducing the
   overhead of creating new connection for each database operation.
2. ThreadPool: In concurent programing, a thread pool implemented using the obejct
   pool pattern allows for the efficient managemnt and reuse of threads, Improve
   performance and resource Utilization.
3. Object reuse in Graphics Rendering: Computer graphics rendering Involves reusing the
   objects such as textures, shaders, or models. An object pool can manage these objects
   allowing efficient reuse and reducing the overhead of creating and destroying them.
4. connection pooling in web servers: Web servers often handle multiple client request
   simulatensously. an object pool pattern can be use to create a pool of pre-initialized
   connections to backend systems, such as database or extenernal services, Improving
   performance and scalability.
5. Resource Pooling in IOT device: In IOT devices often have limited resources such as
   network connections or sensors. An object pool pattern can manage these resources,
   allowing efficient sharing and reuse across multiple tasks or events.
6. Connection pooling in Messaging System: Messaging systems, such as message queue or
   event brokers, frequntly required maintaing connections to extsenal system, aN OBJECT
   POOL manage these connections, enabling efficient reuse and reducing the overhaed of
   establishing and tearing down connections for each message and events.
7. object pooling in object-relational mapping(ORM): ORM Frameworks often use an Object pool
   to manage database entity objects, Improving performance by reusing existing objects
   Instead of creating new ones for each database query.
8. connection pooling in Distributed system: Distributed system often required connections
   to remote services or components. an obejct pool pattern can manaage these connections
   optimizing resource utilization and minimizing the overhead of connection establishments.
9. ResourcePooling in File and I/O opertaions: File I/O operations, especially in high
   throughput system. can benifit from object pool managing file handles. reusing file
   handles can improve performance by avoiding the overhead of opening and closing the files
   repeatedly.
10. object pooling in connectionless protocols: Connectionless protocols like UDP(user datagram
    protocol) can use and object pool to manage pre-allocated packet obejcts. This approch avoids
    the overhead of creating and garbage collecting packets for each messge transmission.

# Terminologies

1. Object-POOL: the centeral components of the pattern that manages the pool of reusable obejcts.
2. Object; The obejcts that are created and managed by pool. these objects are typically expensive
   to create and initialize.
3. Pool managers: the entity responsible for managing the obejct pool. it handle the creation
   allocation, and deallocation of objects in the pool.
4. Available objects: The collection of obejcts in the pool that are currently not in use and
   available for allocation.
5. In-Use obejcts: the collection of objects that have been allocated and care currently being
   used by the client.
6. Object creation: The process of instaintiating new obejcts in the pool. this step typically occurs
   during the initialization of the pool.
7. Object allocation: The process of providing an available objects from pool to a client who request it.
8. ObjectDeallocation: The process of returinig an obejct to the pool when it is no longer needed
   by the client. this step may involves resetting or reinitalizing the object.
9. PoolSize: tha max number of objects the pool can hold. it determine the capacity and scalability
   of the pool.
10. Client: The entity that requests obejcts from the object pool for temporary use.
11. Obejct Reset/Reinitialization: The process of restoring an obejcts to its initial state
    when it is returned to the pool. This step ensure that the object is clean and ready for
    reuse.

# When to use it object pool

1. Expensive resouce creation: database conenction, network connection, or thread is costly
   in terms of time and resource. object pooling can help, re-using pre-initilaized instances
   from a pool elimintes the need for repetetive initialization, resulting in improved
   performance.
2. Limited resource Availability: When the number of available resouce is Limited such as
   in Db connections, thread pools, object pooling allows you to efficiently manage and reuse
   those resources among multiple clients and tasks. it help prevent resource exhaustion and
   provide controlled access to the Limited resources.
3. Thread Syncronization overhead: Multiple thread required access to a limited set of objects
   using an obejct pool can minimize contension and syncronization overhead. Instead of creating
   and destroying objects concurrently, Threads can aquired and release obejcts from the pool.
   reducing contension and Improving thread safety.
4. object reuse optimization.
5. system scaliability: in high scalable system

# Advanatges and Disadvatages

1. Performance Improvements: object pooling can improve perfromance by reusing pre-initialized objects instead of creating new ones. this elieminates overhead of object creation. Initialization
   and destructioin resulting in faster execution times.
2. ResouceOptimizations: by reusing objects from the pool the obejct pool pattern help optimize
   resource utilization. it reduces the assumption of system resources such as memeory network
   connections. or database connections especially in senarion where creating and destroying
   resource is Expensive
3. Controlling resource access: Object pooling allows you to control the maximum number
   of resource available at any given time. this can be useful in Managing Limited resource
   such as database connections or threadpool, and prevent resource exhaustion.
4. ThreadSafety: Object pooling can provide thread safety by managing the access to shared resources
   by controlling how objects are acquired and released from the pool. you can ensure that multiple
   threads can safely use the objects without conflict or concurency issues.
5. Scalability: The obejct pool pattern supports scalability by efficeiently reusing objects
   it enable you to handle Increased workLoad or concurent requests without overwhelming the system
   resources creation or causing resource bottlenecks.

# Disadvatges

1. Complexity: it add complexity to code base. required creating and managing pool
   handling obj acquization and release and ensuring proper syncronization in multi
   threaded senario. this can increase the overall code complexity and maintaince efforts
2. Overhead of managing the pool: object pooling Introduce additional overhead in managing the
   pool of objects. This overhead incudes acquiring and releasing objects from the pool.
   mainatning the pool's state and handling resource allocation and deallocation.
3. Inflexibility: Object pooling may not suitable for all types of objects scenarios.
   objects that have short lifespan or frequntly change their state may not benifit significatly
   from pooling. additionally the fixed size of pool may limit the flexibility of scaling dynamically
   based on demand.
4. object stale state: Reusing the objects from pool can lead to objects retaning stale state
   if they are not properly reset or cleaned before being returned to the pool. it requires
   careful managemnts to ensure that objects are in a consistent and expected state when
   acquired from the Pool.
5. Increased memory usages: object pooling can increase memory usages especially if obejcts
   stored in the pool are large or have significant memeory footprint. the pool need to mainatins
   the unused obejcts in memory, which may not be ideal in a memory-constrained environments.

# Things to Note:

1. ThreadSafety: its crucical to use proper syncronization to mainatin thread safety and prevent
   race conditions or data corruptions.
2. ResouceCleanUp: objects acquired from the pool should be properly cleaned and reset before they
   are returned to the pool. this ensure that obejcts are in consistent and expected state when acquired by other client. failing to clean objects may result in stale state or unintend
   behaviour.
3. PoolSize and resource availability - determine pool size based on expected demand and available
   resources. be mindful of the resources required by each objects in the pool and ensure that pool
   size doesnot exceeds the availble resources. considering implemnting macanisum to handle senario
   when all resource are in use such as blocking and returing an Error.
4. Object life cycle managements: considerd how objects in pool are created initialized and destroyed
   objects should be properly initialized before being added to the pool, they shoud be cleaned and reset, so they are ready for next client.
5. Pool performance: measure and optimize the perfiormance of objects pool implemnetaion. Ensure that
   acquiring and releasing the objects from the pool is effiecient and doesnot introduce significant
   overhead. profile and benchmark the pool to identify potential bottleneck or areas for Improvemnts.
6. Resource leaks: be caution on resource Leaks, especially if object in the pool hold resources such as database connections, network sockets, or file handles, make sure that objects are properly
   released and resource are cleanedup when object are removed from the pool or when pool itself is
   destroyed.
7. object validity and expiration: Consider Implemnting mecanisum to check the validity of objects before they are acquired from the pool. this help prevent using stale or expired objects. if obejct have limited lifespan or expiration time. Implemnt mecanisum to handle objects expiration and remove
   expired obejcts from the pool.
8. Poolconfiguration and tuning: provide flexibility for configuring and tuning the object pool
   parameters such as max pool size, timeout duration, or eviction policies. This allows customization based on specific application requirements and helps optimize resource utilization and performance.

# Proxy
- proxy it allow client to interact with and objects indirectely through proxy objects
  the proxy objects act as an intermediary between the clients and the real objects
  provinding additiional functionality such as caching, security or remote access
- proxy has same interface as the real object, so the client can use it interchangebly
  with the real objects. the client is unware that it is using the proxy object.
  as the proxy object transpaarently forwards request to real objects and many also
  perform additional tasks before or after forearding the request.
- use in situation where where real object is resource intensive to create,
  or where access to real word objects need to be cobtrolled or secured.
  it can also be used to add functionality to an objects, such as logging
  without modfying the original objects code.

# Realword use case
- RemoteProxies: in a distributed system, remote proxies are used to access objects that
  are located on a different machine or process. the remote proxy act as a local represenation
  of remote objects and comunicate it over a network
- Virual Proxeis: its are used to create obejcts that expensive to create, virtual proxy
  create lightweight placeholder object and defers the creation of actual object until
  needed.
- protection Proxies: it is used to control access to objects. the protection proxy adds
  an additional layer of security to an objects by checking permision before allowing access.
- Cache proxies: used to chached frquntly used objects. the chache proxy intercepts requests
  for an objects and check if it is already in the chache. if the objects in the cache
  it return the cached objects instead of creating new one.
- Logging proxeis: log action performed on an object. the logging proxy intercepts request for
  an objects and logs information about the request before forwarding to the actual objects.

# Terminilogies
- Subject: common interface or absatrct class that both the realSubject and proxy classes Implemnts
  it define the common operations that both classes can performs
- RealSubject: This is a real objects that the proxy represents, it Implemnts the operatioons
  defined in the subject Interface
- Proxy: This is the obejcts that act as intermediatry between client and RealObjects. it implements
  the same interface as the RealSubject and forwards the requests from the client to the RealSubject
  adding its own behaviour before or after forwarding request.
- Client: obj that interacts with proxy objects to perform operation on RealSubject.

# advatges
- Provdie a level of Indirection: The proxy act as an intermediary betwen the client and the real
  objects, providing an additional level of Indirection. this can help to decouples the client from
  the real object, making it easier to modify or replace the real object without affecting the client
- Enhances Security: The proxy can be used to Implemnt access control mechanisum, limiting the access
  to real object to authorized clients. this can help to improve the security of the system.
- Improves Perfomances: chache frequnltly requested data, reducing the real obj to access
- simplified complex system: network comunications, adding protocol from the client

# Disadvatges
- can add complexity - additional layer
- can affect performance
- may be not situable for all situation: if obj is small and simple the use of proxy may not
  provide any benifits and may even reduce performance
- can increase developemnt time
- can introduce single point of failure
- can lead to overuse - excessive number of layer

Improving modularity, secirity of system

# Things to Note:
- Interface Compatibility: the proxy shoudl have same interface as real object is representing
  This allow client to interact with proxy in the same wway as the real objects.
- Lazy Initialization: The proxy should only initialize the real object when it is actually needed
  this can help to Improve performance by avoiding unnecessary initialization.
- Access Control: proxy should implement authentication and authorization mechanisum to control
  access to real object.
- caching - frequnlty requested data
- Error Handaling
- testing


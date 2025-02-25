# Strategy design pattern

- It allow you to define the family of algorithums encaptultes each one in seperate class
  and make them interchnagable, it enables the algorithums to vary independently from the client
  that use them, allowing runtime selction of algo based on specific requirements.
- encaputlates group of algo and provide common interface
- code reuse, maintainbility, selection of algo at runtime

# real World use case

- Sorting Algorithums - bubbble sort, merge sort, quick sort can be encaptulates as strategies.
- Payment processing - credit, paypal can acts as strategies
- File Compression utility - ZIP, GZIP, RAR
- Routung in nvaigation system - fatstees route, shortest route, or avoiding tolls.
- cache mangemnts - LRU, LFU etc
- Text Editors - find and replace, spell checking, code formating
- load Balancing - in distributed system , roundrobin, least connection etc
- Trading system - trend following, mean reversion, or breakout, traders can switch between
  stratiges, based on the market conditions or their investemnt goals
- Recomndation engine - collbartive flitering, content based filtering
- User Authentication - user, password authentication/ social media authentication, two factor
  authentication, the autentication strategy can be selected based on user prefernce or security
  requiremnts
- image processing Filters - gray scale, sepia or blur

# Terminogies

- Context - business logic that need to perfom, refence to strategy obejcts used to execute the desired algorithums
- Strategy - common methdhods differnt algo Implemnts
- Concrete Strategy - actual implemnation of interface, detail implemntion of algo defiend

# when shoud we use it

- set of related of algorithum and behaviour selected at runtime
- when avoid creating large numbwr of conditiional statements, or switch cases for selcting differnt algorithums
- when you want a family of interchanagable algo to encaptultes each algo separately

# Advantages

- flexibility
- Improved code organisation
- Easy Extensibility
- Simplified conditional logic - removed need to conditional logic
- Testebility

# disadvatges

- Incresed number of class
- Potential perfomnce Impact

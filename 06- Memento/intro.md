# Memento design pattern

- provides ability to capture the internal state of objects. it allows to save and restore the
  state of objects effectively creating a snapshot of its current state.
- restored the obejcts at its previous state. providng undeo and redo functionalites
  it also enables the obejcts to save its state externally so that it can be persiated
  or transferd between the system.
- overall it provide flexible ways of captures and restore an object state. ensuring
  encaptulation ans supporting undeo/redo opertaions and state persistence.

# Terminologies

- Text Editors - undeo funtionlaity
- Video games - save and load functionality, capture game state
- WebForm data - save as form state
- Doumnt editing applications - store doc state, including text formating, and relevat information allowing user to revert and reapply changes as needed.
- Flight booking system - hold or confirm functionality, hold booking temporarly a memneto can be created to store the selcted flights and customer details, the booking can be then confirmed or canceleld based on user decisions.
- Drawaing Applications - undo drawaing actions

# terminolopgies

- Orginator: whose state being saved and restored, it is responsible for creating and restoring mementos, the orginatir has methods to create a memento objects that captures its current state
  and another method, to restore its state from a memento objects.
- memento - objects represents save state of the orginator, state is read only
- careTaker - managemnts of memento, craete memento and store in collections such as statck
- state - internal data

# when should i use

- undeo/redo functionality
- checkpointing - checkpoint of snapshot of objs state at various state of time.
- History tracking
- collabrative Editing - syncoronize and revert to a consistent state, mememnto staore shared objects state
- caching and optimization

# Advatages

- Encaptulation of state
- state preservation
- simiplifies originator class
- undeo/redo support

# disadvatges

- Increased memory usages
- Perfomance Impact
- Limited accesibility
- Manging meento

# Things to Note

- state encaptulation
- memento Imutability
- orginator resposibility - method to craete memento
- caretaker role
- Memento storage - list, stack, dict based on requiremnts
- deep copy considerations - serialization techinques
- object serilization to create memento, pickle, json
- Versioning and compatibility
- test coverages

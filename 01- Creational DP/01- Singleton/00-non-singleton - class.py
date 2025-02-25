class NoneSingleton:
    def __init__(self, name):
        self.name = name


ns1 = NoneSingleton("Boy")
ns2 = NoneSingleton("Girl")

print(ns1, ns2)

print(ns1 is ns2)

print(f"ns1: {ns1.name}, ns2: {ns2.name}")


# class Singelton
class Singelton:
    __instances = None

    def __init__(self):
        if Singelton.__instances is not None:
            raise Exception("Instances already Exists")
        Singelton.__instances = self


ns1 = Singelton()
ns2 = Singelton()
# assign same instances for creating objects
# staic methods is declared which check no singelton exit
print(ns1, ns2)

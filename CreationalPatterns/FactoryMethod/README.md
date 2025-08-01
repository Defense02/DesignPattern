# Factory Method

- creational design pattern that provides an interfact for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
- design pattern that uses factory methods to deal with the problem of creating objects without having to specify their exact classes. 

## How they work

- The Factory Method pattern suggests calls to a special factory method, rather than direct object construction calls.
- Products: objects returned by a factory method
- subclasses can override the factory method or change the class of products being created by the method.

## Applicability

- when you don't know the exact types and dependencies of the objects your code should work with.
- 
# TrivialMessageBus

TrivialMessageBus is a very simplistic or even trivial implementation of a message bus in python. It's based on the great functionality of zmq and aims to offer a proxy for applications that exchange messages between each other. It's designed to be a reliable centric communication point that publishers as well as subscribers can connect to without knowing each other and relying on each other in order to be able to operate.

The trivial message bus is neither designed for high performance nor for scalability, but for simplicity.

If you're planning a network of services providing and consuming data, and you want some sort of abstraction layer between the components in order to stay flexible in plugging and changing these without risking malfunctioned services due to connection losses, than the SimpleMessageBus might be something for you to consider.

However, please keep in mind that for the sake of simplicity
- the design is not optimized for high throughput
- there is no foundation for scale out
- its limited to use tcp
- there is no authentication layer included
- there is no guarantee for delivering all messages
- the design is based on the publish - subscribe pattern utilizing multipart messages
- 
If these features and restrictions are still wetting your appetite: Have fun using it!

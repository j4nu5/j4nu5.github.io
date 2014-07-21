Title: Abstract Classes and Factory Design Pattern in Python
Date: 2013-12-19
Category: Programming
Tags: python, programming


[Abstract Classes](http://en.wikipedia.org/wiki/Class_(computer_programming)#Abstract_and_concrete)
are one of the most useful and important concepts in Object Oriented
Programming. I'll attempt to illustrate their usefulness, and their usage in
Python 2.7 with the following (seemingly contrived) example:

Let us say, you want/have to implement posting updates on Facebook using
Python. Your code might look something like this:


    :::python
    # Attempt 0: Bad code.

    def facebook_share_init(*args, **kwargs):
        # Initialize OAuth with facebook
        # ...

    def share_on_facebook(*args, **kwargs):
        # Post to Facebook
        # ...


It works and everyone is happy. Then one day, you decide to support posting
tweets in your application. You add the following:


    :::python
    def twitter_share_init(*args, **kwargs):
        # Initialize OAuth with twitter
        # ...

    def share_on_twitter(*args, **kwargs):
        # Post to Twitter
        # ...


and the part of your code which has to figure out the appropriate sharing
function to call might look something like:


    :::python
    if requested_sharing_platform == "facebook":
        facebook_share_init(*args, **kwargs)
        share_on_facebook(*args, **kwargs)
    elif requested_sharing_platform == "twitter":
        twitter_share_init(*args, **kwargs)
        share_on_twitter(*args, **kwargs)


Things quickly become complicated when you have to implement Google+ sharing
for example and you add two more functions and another couple of lines to the
if-elif chain.

The real fun starts however when someone else in your team decides to
copy-paste your if-elif chain and 10 days later, when you implement LinkedIn
sharing, you expand your if-elif chain, but not your colleague's, leading to
all kinds of problems.

The above problem can be neatly solved using Abstract Classes
(and the Factory Pattern).

A good rule of thumb in OOP is to "program to an interface, not an
implementation". What this means is to create an abstraction over related
objects, that enforces a contract between the caller and the callee. For
example, consider set of classes called Cat, Lion and Dog. A cat meows, dog
barks and lion roars. But we may see these as special cases of an abstraction
called speak, which translates to roaring for lions and barking for dogs. Our
class definitions may look like:


    :::python
    class Animal(object):
        def speak():
            pass

    class Cat(Animal):
        def speak():
            # Meow

    class Dog(Animal):
        def speak():
            # Bark

    class Lion(Animal):
        def speak():
            # Roar


The problem with the above approach is that it is not enforcing. We can easily
create a class like:


    :::python
    class Fish(Animal):
        def swim():
            ...


Callers of Cat, Dog or Lion can call the speak method without any problem but
calls to speak method of Fish instances will be delegated to the superclass,
which might be a problem in real life examples. Ideally we would want users of
our abstraction to have an iron clad contractual obligation with respect to
the methods that we have exposed. This is where abstract classes come in.

Python originally did not have support for abstract classes and some people
still consider them to be unpythonic. Python has decided to take the middle
path on this (see PEP 3119) and has added support for abstract classes using
the abc module, but has not changed the core syntax of the language.

Here is how our original problem of social sharing can be solved using abstract classes:


    :::python
    import abc

    class AbstractSocialShare(object):
        __metaclass__ = abc.ABCMeta

        @abc.abstractmethod
        def __init__(self, *args, **kwargs):
            pass

        @abc.abstractmethod
        def share(self, *args, **kwargs):
            pass


    class FacebookShare(AbstractSocialShare):
        def __init__(self, *args, **kwargs):
            # Initialize Facebook OAuth
            ...

        def share(self, *args, **kwargs):
            # Share on Facebook
            ...


    class TwitterShare(AbstractSocialShare):
        def __init__(self, *args, **kwargs):
            # Initialize Twitter OAuth
            ...

        def share(self, *args, **kwargs):
            # Share on Twitter
            ...


Try creating an object of the abstract class with:


    :::python
    obj = AbstractSocialShare()


You will receive a TypeError.

Now try creating and instantiating this class:


    :::python
    class IncorrectShare(AbstractSocialShare):
        def __init__(self, *args, **kwargs):
            ...


Since IncorrectShare has not implemented the share method, we will not be able to instantiate it.

How do we take care of the ugly if-elif chain? Thats where the Factory pattern comes in.


    :::python
    class SocialShareFactory(object):
        __share_classes = {
            "facebook": FacebookShare,
            "twitter": TwitterShare
        }

        @staticmethod
        def get_share_obj(self, name, *args, **kwargs):
           share_class = SocialShareFactory.__share_classes.get(name.lower(), None)

            if share_class:
                return share_class(*args, **kwargs)
            raise NotImplementedError("The requested sharing has not been implemented")


The usage will be something like:


    :::python
    obj = SocialShareFactory.get_share_obj("facebook", *args, **kwargs)

    obj.share("Something")


Conclusion
----------

Python is an interpreted language which supports and encourages duck typing. Abstract classes may seem superficial in such a language but as I have attempted to illustrate above, they vastly improve code maintainability and reuse.

Comments are welcome!

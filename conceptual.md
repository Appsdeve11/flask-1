### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
I think one of the most important difference would have to be JavaScripts ability to run in most web browsers while python you will most likely need an interpreter. In my opinion, python is much easier to read as well.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  There are few methods like..
  -using get()
  -using setdefault()

- What is a unit test?
unit testing focuses on indivisual components of a system.
- What is an integration test?
integration testing is a type of software where softwares are put together and than also tested together. 
- What is the role of web application framework, like Flask?
ultimatley, a framework is a code library that makes developing SO MUCH easier.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  it just depends on the requirements needed. For an example, if a parameter is essential for the functuality of the route than I would use route url parameter.


- How do you collect data from a URL placeholder parameter using Flask?
you can use request.args
- How do you collect data from the query string using Flask?
you can use query_string property

- How do you collect data from the body of the request using Flask?
you can use request.get_data()

- What is a cookie and what kinds of things are they commonly used for?
a cookie is info that is put into a clients computer and they are commonly used to store information into the browser for fututre situations.       
- What is the session object in Flask?
sessions object in flask is used get and set data. when session object is used it is saved into the browser and turned intoa cookie.

- What does Flask's `jsonify()` do?
jsonify() returns a response object.


### Conceptual Exercise

Answer the following questions below:

 - What are important differences between Python and JavaScript?
	1. JS can be processed on both the font-end and back-end while Python is processed on the server (back-end)
	2. Python make use of indentations to define code blocks
	3. Python has very large number of external libraries.
***
 - Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
	  1. use **get(key,def_val)** to check for a key & if it's not present then return a custom message.
		  i.e. `my_dict.get('c', 'Not Found')`
		2. use **setdefault(key, def_value)** if a key is not found, a new key is created with a defined, default value.
		   i.e. `my_dict.setdefault('c', 'Not Found')`
***
 - What is a unit test?
	 - Unit tests run a test on a defined section of code. This could test a function, class, or method.
***
 - What is an integration test?
	- An integration test tests multiple components of the app to make sure that they all function together.
***
 - What is the role of web application framework, like Flask?
	 - Flask and similar frameworks make server-side scripting usable for front-end rendering. Flask allows you to create routes, HTML templates, use CSS & Javascript while using Python as the primary programming language
***

 - You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
	  - when you use the first URL (`/foods/pretzel`), Flask creates a route to this specific route. If this route is not defined, then the server will pass a 404 in the header. However, the second URL (`foods?type=pretzel`) follows the `food` route and passes in a value of `pretzel` into the `type` variable.
 ***
 - How do you collect data from a URL placeholder parameter using Flask?
	 - You collect the parameter when setting up the URL route in the Flask app. To do so, you create a parameter surrounded by `<>` signs. If you want to collect the id for a page you would write the code like this:
    ```python
    @app.route('/foods/<type>')
	    def food_page(type):
    ```
***
 - How do you collect data from the query string using Flask?
 - You return the full query string by importing the `request` object from flask & then use `return request.query_string`. To access individual, known parameters you would use the `args` method. `return request.args.get('param)`
***
 - How do you collect data from the body of the request using Flask?
	 - First you must import the `request` object from the Flask library- `from flask import request` To get user inputed information through a form, you will submit a POST request & store the information in a variable.
***
 - What is a cookie and what kinds of things are they commonly used for?
	 - Cookies are small text files with various pieced of data. They are often used identify specific users and various related pieces of information.
***
 - What is the session object in Flask?
	 - Session objects track the session data via a dictionary that contains a key-value pair for the associated session. Like cookies, these store small pieces of data, but session data is erased at the end of a user's session and is not stored on the local computer.
***
 - What does Flask's `jsonify()` do?
	 - `flask.jasonify()` creates a response in JASON format. Here is an example when receiving a user's information and packaging the information in JSON format:
    ```python
	from flask import jsonify
	@app.route('/get_user_info')
	def get_user_info():
		return jsonify(username=user.username, email=user.email, id=user.id)
	```
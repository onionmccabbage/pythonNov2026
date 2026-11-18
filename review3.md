## Python Review 3
#### 1hr 10mins (until 2:55)

- Alter these instructions to suit your thinking
- Aim for good architecture (maybe use separate modules, remember `if __name__...`)
- Look online, talk to each other, ask me etc.
- There will be an opportunity to share your code

Write a 'Weather' class with get/set methods for 'city' and 'description'
- (remember: you will also need `__init__` )

Your class should validate:
  - the value for 'city' is a non-empty string of three or more characters 
    - (e.g. if type(city)== str and len(city)>2:)
  - if city is missing or unacceptable, you should provide a sensible default 
    - (e.g. 'Newcastle')
  - 'description' must be a string, but it may be an empty string
  - decide if you will raise a TypeError or set a default for description

If you like, in your Weather class override `__str__` so the class prints nicely,
something like 'The weather in Newcastle is rainy'

Exercise the code by making instances of your Weather class with suitable values

### Optional (If Time)
* Add a class property for 'temperature', which must be a float or integer
* Decide how to handle invalid temperature values (e.g. raise an exception or set a default)
* There is a public API for weather. Here are the parts you will need

`url_dict = {
  'template':'http://api.openweathermap.org/data/2.5/weather?q={}&units={}&APPID={}',
  'city':'newcastle',
  'units':'metric',
  'key':'48f2d5e18b0d2bc50519b58cce6409f1'
}`

Here is a sample URL
`link = http://api.openweathermap.org/data/2.5/weather?q=newcastle&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'`

Use the 'requests' library to get the weather for a (valid) city, then populate a weather instance from the results

From the returned JSON, you can get the weather description like this:
- results['weather'][0]['description']
and the temperature like this
- results['main']['temp']
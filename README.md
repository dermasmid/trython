# Installation

`pip3 install function_error_handling`

# About
The main use for this package is when making requests with the requests module.
Sometimes the network might be unavailable, are the server (the endpiont) might be temporarily down,
We don't want our script to quit just because of that (although we can put everything in a loop and catch error's that will still lose the progress of the previous loop, and is a bit messy).

This is where *function_error_handling* comes in, it gives you two very approachable techniques to solve this.

From here on I'll be using `requests.get` as the function we want to add error handling to.


## Approach 1
Replacing `requests.get` with an alternitave error handled one.
```python
import requests
import function_error_handling
requests.get = function_error_handling.wrap(requests.get)
```
Now when you call `requests.get` and it throws an error, we will catch that and try to run the request again - without you even knowing.

## Approach 2
Decorating your own function.
```python
import requests
import function_error_handling

@function_error_handling.wrap()
def requests_get(url):
    return requests.get(url)
```
Now when you call `requests_get` the same logic will be applied.


# Options
The wrap function takes in a couple of arguments:

* `func`: (*callable*) This is the function that we are adding error handling to.
* `number_of_attempts`: (*int*) **default=5** The number of times you want to retry before finally raising the error.
* `time_to_sleep`: (*int*) **default=30** Time to sleep between retries.
* `errors_to_catch`: (*tuple*) **default=(Exception, )** Which errors you want to handle.
* `validator`: (*callable*)  **default=None** A function that will validate if the return of the function is valid, if the function throws an error or returns false - it will be treated as if the `func` thew an error.
* `callback`: (*callable*)  **default=None** A function to be called each time an exception occurs, this function should take the exception as an argument.



# More about validtators
Let's take another look at validators, because without them this whole thing is useless.
A very common reason that a script will quit is when you are hitting a api endpiont, and you expect a certain data type, and you go ahead and call some function and that data that will give you an error when it doesn't understand that data it got, without validators there's no way for us to know that.

That's when we create a validator - when we expect the result of a given function to be something, but might a times be something else entirely.
We create a function that takes in the func's return value and we check if it satisfies us, And if the validator function returns false or throws an error, then we retry, otherwise - we know we got the right data.

I have included some predefined validators which you can import like this: `from function_error_handling import validators`.
Feel free to make pr with some other helpful validators.

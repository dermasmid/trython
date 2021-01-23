# Installation

`pip3 install function_error_handling`

# Usage

```python
def function_that_might_throw_error():
    # stuff that is questionable
    pass

imoprt function_error_handling

function_that_might_throw_error = function_error_handling.wrap(function_that_might_throw_error)

function_that_might_throw_error()
```
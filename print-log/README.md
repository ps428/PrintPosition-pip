# Print Position
A cool python package to add the file name and line number in the print statements. This small tool can be very helpful in debugging big Python projects.

## Motivation
To debug the Python code present in multiple files, it becomes difficult to track down the print statement calls in the different files. This small pip package can be highly useful in such cases, one can simply use the custom print statement defined in this package and see the filename and line number of the print call.

## How to install?
Just install the package using the command:
```
pip3 install print_position
```

## Usage
Simply add this import statement on top of your python file to see the file name and line number of each print statement.
```
from printPosition.printPosition import printPosition as print 
```
A simple example is (test.py):
```
from printPosition.printPosition import printPosition as print 
print("Test on line 2 from test.py")
print("Test on line 3 from test.py")



print("Test on line 7 from test.py")
```
\
The output is shown as:

```
@file_name:line_number
print_data
```

I believe this would be very helpful in tracking down errors during debugging, **especially when you are working with someone else's code**.

# Contact me
To raise any **issues/requests** you may refer the issue page [here](https://github.com/ps428/PrintPosition-pip/issues).
\
You may **mail me** here on my [mail id](mailto:pranav.bhawan@gmail.com).
\
Feel free to **connect with me** on [my LinkedIn](https://www.linkedin.com/in/ps428).
\
Please do check out my other projects on my **GitHub** [here](http://www.github.com/ps428).
\
Also I have made many cool Firefox Add ons. They are pretty useful, you may want to check them out [here](https://addons.mozilla.org/en-US/firefox/user/17277929/).
\
\
If you like my work, you may want to [buy me a book here](https://www.buymeacoffee.com/ps428).
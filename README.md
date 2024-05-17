# CCalculator

just testing around combining c and python and profiling

obviously we can easily make this app more complex, add more functionalities, fix some edge cases

but my learning purpose for this is just to learn how to work with building lower level APIs and profile things. as sometimes we need to leverage perf capabilities of languages like C to combine with ease of development in python land

i used `ctypes` to call C functions from python

[https://docs.python.org/3/library/ctypes.html](https://docs.python.org/3/library/ctypes.html)

got to take note of the ctype data type conversion as well for runtime errors

# instructions

compile c code to a shared library

- lprofiler: gperftools
- lm: math library in c
- g: includes debug symbols for profiling so that gperftool's pprof can map memory addresses to source code

```
$ gcc -g -shared -o libcalculator.so -fPIC calculator.c -lprofiler -lm
```

start the flask web server

```
$ python app.py
```

to access app, go to

```
http://127.0.0.1:5000/
```

make some big calculations, then stop the app

```
ctrl + c
```

then generate profile analysis for C with [pprof](https://github.com/google/pprof), which is installed via gperftools (on mac: $ brew install gperftools), you need to have LLVM visualizer

```
$ pprof --text ./libcalculator.so profile.prof
```

once profile.prof is created, we can generate PDF visualizations for it via pprof too, but it also requires installing graphviz and ghostscript (for ps2pdf), both easily installed with homebrew on mac

```
$ pprof --pdf ./libcalculator.so profile.prof > profile.pdf
```

to verify if binary contains debug symbols

```
$ nm -g libcalculator.so

or

$ objdump -t libcalculator.so
```

profile analysis for python

```
well for every operation done on the app, profile analysis is already seen on the terminal that's running:

 $ python app.py
```

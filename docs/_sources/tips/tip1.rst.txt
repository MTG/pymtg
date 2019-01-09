Python tip of the week 1, timing
=================================
Sometimes you might want to count how long an operation takes to complete. Surround the call to the function with ``time.monotonic()``: https://docs.python.org/3/library/time.html#time.monotonic

.. code-block:: python

   start = time.monotonic()
   result = my_long_running_function()
   end = time.monotonic()
   total = end - start
   print('This operation took {:.2f} seconds'.format(total))

``monotonic()`` is guaranteed to always increase. Other tips suggest ``time.time()``, which will work most of the time, but this value could go backwards or skip forwards in some cases (daylight savings switchover, if you suspend your machine, if your operating system syncs the clock and makes a change...). Make the right choice and learn to use ``monotonic()``.

If you want to do a micro-benchmark to see how long a function takes to complete (for example if you're optimising it), use the timeit module: https://docs.python.org/3/library/timeit.html
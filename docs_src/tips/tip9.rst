Python tip of the week 9, CSV
============================================

Lots of people store data in CSV format. Unfortunately there's no one standard for CSV, 
which means that it's really easy to generate badly formatted data, or encounter files 
that are constructed badly. Be a good citizen and use a library to help you read and write CSV.

Never try and read or write csv files manually. You will get it wrong.

Don't do this:

.. code-block:: python

    data = open('myfile.csv').read()
    lines = data.split('\n')
    rows = lines[0].split(',')

or this

.. code-block:: python

    fp = open('myfile.csv', 'w')
    fp.write('%s,%s' % (myid, myvalue))

or this

.. code-block:: python

    fp.write('%s\n' % ','.join([some, data, here]))

Instead, you should use the csv module to read and write files: https://docs.python.org/3/library/csv.html

.. code-block:: python

    with open('myfile.csv') as fp:
        csvreader = csv.reader(fp)
        for line in csvreader:
            print(line[2])

    with open('myfile.csv', 'w') as fp:
        writer = csv.writer(fp)
        writer.writerow(['data', 'here'])
        writer.writerows( a list of lists, writing each one on a new line )

If you want to use a file separated with tabs instead of spaces, you can set the delimiter

.. code-block:: python

    reader = csv.reader(fp, delimiter='\t')

or specify a dialect, which also encodes rules about delimiters, quoting and escaping:

.. code-block:: python

    reader = csv.reader(fp, dialect=csv.excel_tab)

If your csv file has a header line, you can use this to generate dictionaries from your file::

    # myfile.csv
    id,filename,license
    1,test.mp3,cc0
    2,foo.wav,ccy-by

.. code-block:: python

    with open('myfile.csv') as fp:
        reader = csv.DictReader(fp)
        for line in reader:
            print(line['filename'])    #-> prints 'test.mp3', 'foo.wav'

To write dictionaries, specify the columns in the DictWriter constructor:

.. code-block:: python

    with open('myfile.csv', 'w') as fp:
        writer = csv.DictWriter(fp, fieldnames=['id', 'filename'])
        writer.writeheader()
        writer.writerow({'id': 1, 'filename': 'test.wav'})

Pandas also has methods for reading and writing csv files if you are already using it:

.. code-block:: python

    import pandas as pd
    df = pd.read_csv('myfile.csv')

Note that by default pandas requires all rows in your csv file to have the same number of columns, which might not always be the case.
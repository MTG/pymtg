import pkgutil

for _, modname, _ in pkgutil.iter_modules(__path__, prefix='pymtg.'):
    __import__(modname)

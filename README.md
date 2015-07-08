# autoserve

Double-click HTTP server for Windows

autoserve uses Python's BaseHTTPServer class to allow users access to
locations on disk from a browser without installing anything or placing
trust in closed source (and potentially unsafe) products.

## Running

1. Clone the Git repository
2. Copy/move the autoserve_dist_v0.1.zip file to target location
3. Extract the zip
4. Run autoserve.exe

## Usage

autoserve supports two arguments (optional):

```
autoserve.exe [<port> [directory]]

  port                Specify port to run HTTP server on (default 8000)
  directory           Specify directory to serve (default is one up from
                                                    the current working directory)
```

## Building

To build the autoserve executable, you should run the following command on a Windows
machine with Python2.7.10 (tested, other versions may work):

```
setup.py py2exe

```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

Developed by Aidan Marlin (aidan [dot] marlin [at] nccgroup [dot] trust)
while working at NCC Group.

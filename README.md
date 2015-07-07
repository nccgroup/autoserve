# autoserve

Double-click HTTP server for Windows

autoserve uses Python's BaseHTTPServer class to allow users access to
locations on disk from a browser without installing anything or placing
trust in closed source (and potentially unsafe) products.

## Installation

1. Clone the Git repository
2. Copy/move the autoserve_dist_v0.1.zip file to target location
3. Extract the zip
4. Run autoserve.exe

## Usage

autoserve supports two arguments (optional):

```
autoserve.exe [<port> <directory>]

  [port]                Specify port to run HTTP server on (default 8000)
  [directory]           Specify directory to serve (default is one up from
                                                    the current working directory)
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

## License

autoserve - Double-click HTTP server for Windows
Copyright (C) 2015 Aidan Marlin (aidan [dot] marlin [at] nccgroup [dot] com)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

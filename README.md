# OSC Client

An OpenStreetCam.org client in Python for ease in requesting publicly available resources from the platform.

Originally created as part of the following volunteer AI challenge: _Omdena + iRAP: Preventing Road Crashes and Saving Lives_ (https://omdena.com/projects/ai-road-safety/).

## Installation

```shell
pip install git+https://github.com/d33bs/osc_client@main#egg=osc_client
```

## Usage

### Simple Request Example
```python
from osc_client import OSC
osc = OSC()
photos_list = osc.get_photos_from_point(lat=34.94083565649461, lng=-82.8662492514243)
photos_list[0]
```

## Testing

Various tests may be found under the ./tests directory within this repo. See below for a straightforward example on running those tests. 

```shell
pip install pytest
pytest tests
```
import os
import tifffile
import functools
from typing import Mapping, Tuple, Union
import numpy as np
from starfish.experiment.builder import FetchedTile, TileFetcher
from starfish.types import Axes, Coordinates, Number


@functools.lru_cache(maxsize=1)
def cached_read_fn(file_path) -> np.ndarray:
    return tifffile.imread(file_path)

class ImageTile(FetchedTile):

    def __init__(self,
                 file_path: str,
                 coordinates: Mapping[Union[str, Coordinates], Union[Number, Tuple[Number, Number]]],
                 z: int) -> None:
        self.file_path = file_path
        self._coordinates = coordinates
        self.z = z

    @property
    def shape(self) -> Mapping[Axes, int]:
        raw_shape = self.tile_data().shape
        return {Axes.Y: raw_shape[0], Axes.X: raw_shape[1]}

    @property
    def coordinates(self) -> Mapping[Union[str, Coordinates], Union[Number, Tuple[Number, Number]]]:
        return self._coordinates

    def tile_data(self) -> np.ndarray:
        return tifffile.imread(self.file_path)

class ImageTileFetcher(TileFetcher):
    def __init__(self, input_dir: str, basename: str) -> None:
        self.input_dir = input_dir
        self.basename = basename # in the format R##S#
        self.coordinates = {
            Coordinates.X: (0.0, 0.1625),
            Coordinates.Y: (0.0, 0.1625),
            Coordinates.Z: (0.0, 0.4),
        }

    def get_tile(self, fov: int, r: int, ch: int, z: int) -> FetchedTile:
        basename = f"{self.basename}_CH{ch}_Z{z+1:03}.tif"
        print(f"Fetching tile {basename}")
        file_path = os.path.join(self.input_dir, basename)
        return ImageTile(file_path, self.coordinates, z)

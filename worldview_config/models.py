from datetime import datetime

from pydantic import BaseModel, Field, RootModel

class Projection(BaseModel):
    source: str
    matrixSet: str

class LayerConfig(BaseModel):
    id: str
    satellite: str
    instrument: str
    measurement: str
    discipline: str
    title: str
    group: str = Field(default="overlays")
    description: str = Field(default="")
    tags: list[str] = Field(default=[])
    format: str | None = Field(default=None)
    projections: dict[str, Projection] | None = Field(default=None)
    period: str | None = Field(default=None)
    type: str | None = Field(default=None)
    colormap_id: str | None = Field(default=None)
    start_date: datetime | None = Field(default=None)
    end_date: datetime | None = Field(default=None)
    temporal_start: datetime | None = Field(default=None)
    temporal_end: datetime | None = Field(default=None)
    date_interval: int | None = Field(default=None)
    ongoing: bool | None = Field(default=None)


class LayerConfigs(RootModel):
    root: list[LayerConfig]

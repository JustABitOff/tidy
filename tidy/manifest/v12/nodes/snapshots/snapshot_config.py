from typing import Optional, Dict, Any, Union, List

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v12.bases.hook import Hook
from tidy.manifest.v12.bases.docs import Docs
from tidy.manifest.v12.bases.contract import Contract
from tidy.manifest.v12.bases.enums import OnConfigurationChange
from tidy.manifest.v12.nodes.snapshots.snapshot_meta_column_names import (
    SnapshotMetaColumnNames,
)


class SnapshotConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_extra: Optional[Dict[str, Any]] = Field(None, alias="_extra")
    enabled: Optional[bool] = True
    alias: Optional[str] = None
    schema_: Optional[str] = Field(None, alias="schema")
    database: Optional[str] = None
    tags: Optional[Union[List[str], str]] = None
    meta: Optional[Dict[str, Any]] = None
    group: Optional[str] = None
    materialized: Optional[str] = "snapshot"
    incremental_strategy: Optional[str] = None
    batch_size: Optional[Any] = None
    lookback: Optional[Any] = 1
    begin: Optional[Any] = None
    persist_docs: Optional[Dict[str, Any]] = None
    post_hook: Optional[List[Hook]] = Field(None, alias="post-hook")
    pre_hook: Optional[List[Hook]] = Field(None, alias="pre-hook")
    quoting: Optional[Dict[str, Any]] = None
    column_types: Optional[Dict[str, Any]] = None
    full_refresh: Optional[bool] = None
    unique_key: Optional[Union[str, List[str]]] = None
    on_schema_change: Optional[str] = "ignore"
    on_configuration_change: Optional[OnConfigurationChange] = None
    grants: Optional[Dict[str, Any]] = None
    packages: Optional[List[str]] = None
    docs: Optional[Docs] = Field(None, title="Docs")
    contract: Optional[Contract] = Field(None, title="Contract")
    event_time: Optional[Any] = None
    concurrent_batches: Optional[Any] = None
    strategy: Optional[str] = None
    target_schema: Optional[str] = None
    target_database: Optional[str] = None
    updated_at: Optional[str] = None
    check_cols: Optional[Union[str, List[str]]] = None
    snapshot_meta_column_names: Optional[SnapshotMetaColumnNames] = Field(
        None, title="SnapshotMetaColumnNames"
    )
    dbt_valid_to_current: Optional[str] = None
